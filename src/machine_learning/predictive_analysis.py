import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
from src.data_management import load_pkl_file

def plot_predictions_probabilities(pred_proba, pred_class):
  """
  Plot prediction probability results.

  Args:
      pred_proba (float): Predicted probability.
      pred_class (str): Predicted class label.

  """
  # Create a DataFrame to store the probabilities per class
  prob_per_class = pd.DataFrame(
      data=[0, 0],
      index={'Healthy': 0, 'Infected': 1}.keys(),
      columns=['Probability']
  )

  # Assign the predicted probability to the corresponding class label
  prob_per_class.loc[pred_class] = pred_proba

  # Calculate the complementary probability for the other class label
  for x in prob_per_class.index.to_list():
      if x not in pred_class:
          prob_per_class.loc[x] = 1 - pred_proba

  # Round the probabilities to three decimal places
  prob_per_class = prob_per_class.round(3)
  prob_per_class['Diagnostic'] = prob_per_class.index

  # Create a bar chart using Plotly Express
  fig = px.bar(
      prob_per_class,
      x='Diagnostic',
      y=prob_per_class['Probability'],
      range_y=[0, 1],
      width=600,
      height=300,
      template='seaborn'
  )

  # Display the chart using Streamlit
  st.plotly_chart(fig)


def resize_input_image(img, version):
  """
  Reshape image to average image size.

  Args:
      img (PIL.Image): Input image.
      version (str): Model version.

  Returns:
      np.ndarray: Resized and normalized image.

  """
  # Load the image shape from a pickled file
  image_shape = load_pkl_file(file_path=f"outputs/{version}/image_shape.pkl")

  # Resize the image to the average image size using PIL's resize function
  img_resized = img.resize((image_shape[1], image_shape[0]), Image.ANTIALIAS)

  # Expand the dimensions of the resized image and normalize its values
  my_image = np.expand_dims(img_resized, axis=0) / 255

  return my_image

def load_model_and_predict(my_image, version):
  """
  Load and perform machine learning prediction on live images.

  Args:
      my_image (np.ndarray): Resized and normalized image.
      version (str): Model version.

  Returns:
      tuple: Prediction probability and predicted class label.

  """
  # Load the pre-trained model
  model = load_model(f"outputs/{version}/powdery_mildew_model.h5")

  # Perform prediction on the input image
  pred_proba = model.predict(my_image)[0, 0]

  # Map the class labels to their corresponding indices
  target_map = {v: k for k, v in {'Healthy': 0, 'Infected': 1}.items()}

  # Determine the predicted class based on the prediction probability
  pred_class = target_map[pred_proba < 0.5]
  if pred_class == target_map[1]:
      pred_proba = 1 - pred_proba

  # Display the predicted class label
  st.write(f"The predictive analysis indicates the sample leaf is **{pred_class.lower()}**")

  return pred_proba, pred_class