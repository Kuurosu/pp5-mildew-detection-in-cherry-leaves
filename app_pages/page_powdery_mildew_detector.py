import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
  load_model_and_predict,
  resize_input_image,
  plot_predictions_probabilities
  )


def page_powdery_mildew_detector_body():
  """
  Generate the body of the powdery mildew detector page.

  """
  # Display information about the page
  st.info("Upload images of cherry leaves to determine their powdery mildew status and generate a comprehensive report on the examined leaves.")

  # Provide a link to download the dataset
  st.write("You can download a set of infected and healthy leaves for live prediction from [here](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves).")

  st.write("---")

  # Prompt for uploading cherry leaf pictures
  st.write("**Please upload clear pictures of cherry leaves. You may select more than one.**")
  images_buffer = st.file_uploader(' ', type='jpeg', accept_multiple_files=True)
  
  if images_buffer is not None:
    # Create an empty DataFrame to store the analysis report
    df_report = pd.DataFrame([])

    # Iterate over each uploaded image
    for image in images_buffer:
      # Open the image and display its details
      img_pil = Image.open(image)
      st.info(f"Cherry Leaf Sample: **{image.name}**")
      img_array = np.array(img_pil)
      st.image(img_pil, caption=f"Image Size: {img_array.shape[1]}px width x {img_array.shape[0]}px height")

      # Specify the version for the analysis
      version = 'v1'

      # Resize the input image for the analysis
      resized_img = resize_input_image(img=img_pil, version=version)

      # Perform model prediction on the resized image
      pred_proba, pred_class = load_model_and_predict(resized_img, version=version)

      # Plot the prediction probabilities
      plot_predictions_probabilities(pred_proba, pred_class)

      # Append the analysis results to the report DataFrame
      new_row = pd.DataFrame({"Name": [image.name], 'Result': [pred_class]})
      df_report = pd.concat([df_report, new_row], ignore_index=True)

  # Display the analysis report and provide download link for the CSV file
  if not df_report.empty:
      st.success("Analysis Report")
      st.table(df_report)
      st.markdown(download_dataframe_as_csv(df_report), unsafe_allow_html=True)