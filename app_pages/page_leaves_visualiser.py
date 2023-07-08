import streamlit as st
import matplotlib.pyplot as plt

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

    