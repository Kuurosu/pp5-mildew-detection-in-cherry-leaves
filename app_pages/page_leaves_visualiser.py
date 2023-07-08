import streamlit as st
import matplotlib.pyplot as plt
import os
import seaborn as sns
import random
import itertools
from matplotlib.image import imread

def page_leaves_visualiser_body():
  st.write("### Leaves Visualiser")
  st.info(
    f"A study was conducted to visually differentiate cherry leaves affected by powdery mildew "
    f"from healthy ones. The goal was to develop a reliable method for accurately identifying "
    f"powdery mildew presence on cherry leaves, aiding in effective disease detection and management."
    )
  
  st.warning(
    f"We suspect cherry leaves affected by powdery mildew exhibit distinct visual characteristics. "
    f"The initial symptom is a light-green, circular lesion on either leaf surface, followed by "
    f"the development of a subtle white cotton-like growth in the infected area.\n\n"
    f"In the context of machine learning, it is necessary to prepare the images before feeding them "
    f"into the model for optimal feature extraction and training.\n\n"
    f"Image normalisation is crucial when working with an image dataset, as it ensures consistency "
    f"in pixel values. To normalise an image, the mean and standard deviation of the entire dataset "
    f"are calculated using a mathematical formula that takes into account the properties of an image."
    )
  
  version = 'v1'
  if st.checkbox("Difference between average and variability image"):
    avg_powdery_mildew = plt.imread(f"outputs/{version}/avg_var_powdery_mildew.png")
    avg_uninfected = plt.imread(f"outputs/{version}/avg_var_healthy.png")

    st.warning(
      f"Upon observing the average and variability images, we did not identify "
      f"clear visual patterns that would allow for intuitive differentiation. "
      f"However, leaves affected by powdery mildew exhibited distinct white stripes "
      f"in the central region."
      )

    st.image(avg_powdery_mildew, caption='Affected Leaf - Average and Variability')
    st.image(avg_uninfected, caption='Healthy Leaf - Average and Variability')
    st.write("---")
    
  if st.checkbox("Differences between average infected and healthy leaves were examined"):
    diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")

    st.warning(
      f"Upon careful examination of the study, we have observed that it did not reveal "
      f"discernible patterns that would allow for intuitive differentiation between the "
      f"two entities in question. Despite our extensive analysis, no distinctive visual "
      f"characteristics or features were identified to facilitate easy differentiation."
      )
    st.image(diff_between_avgs, caption='Difference between average images')
  
  if st.checkbox("Image Montage"): 
      st.write("To refresh the montage, click on the 'Create Montage' button")
      
      my_data_dir = 'inputs/cherry-leaves-dataset/cherry-leaves/'
      labels = os.listdir(my_data_dir+ '/validation')
      label_to_display = st.selectbox(label="Select label", options=labels, index=0)
      
      if st.button("Create Montage"):      
        montage(dir_path= my_data_dir + '/validation',
                label_to_display=label_to_display,
                nrows=8, ncols=3, figsize=(10,25))
      
def montage(dir_path, label_to_display, nrows, ncols, figsize=(15, 10)):
  """
  Creates a montage of images from a specified label in the given directory.
  The montage is displayed using subplots.

  Args:
      dir_path (str): The path to the directory containing the images.
      label_to_display (str): The label of the images to display.
      nrows (int): The number of rows in the montage.
      ncols (int): The number of columns in the montage.
      figsize (tuple, optional): The size of the figure. Defaults to (15, 10).

  Returns:
      None
  """

  sns.set_style("white")
  labels = os.listdir(dir_path)

  # Check if the specified label exists in the directory
  if label_to_display in labels:

      images_list = os.listdir(dir_path + '/' + label_to_display)
      
      # Check if the requested montage size is greater than the number of available images
      if nrows * ncols < len(images_list):
          img_idx = random.sample(images_list, nrows * ncols)
      else:
          print(f"Decrease nrows or ncols to create your montage.\n"
                f"There are {len(images_list)} images in your subset.\n"
                f"You requested a montage with {nrows * ncols} spaces")
          return

      # Create a list of axes indices based on nrows and ncols
      list_rows = range(0, nrows)
      list_cols = range(0, ncols)
      plot_idx = list(itertools.product(list_rows, list_cols))

      # Create a Figure and display images
      fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
      for x in range(0, nrows * ncols):
          img = imread(dir_path + '/' + label_to_display + '/' + img_idx[x])
          img_shape = img.shape
          axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
          axes[plot_idx[x][0], plot_idx[x][1]].set_title(f"Width {img_shape[1]}px x Height {img_shape[0]}px")
          axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
          axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
      plt.tight_layout()

      st.pyplot(fig=fig)

  else:
      print("The label you selected doesn't exist.")
      print(f"The existing options are: {labels}")
