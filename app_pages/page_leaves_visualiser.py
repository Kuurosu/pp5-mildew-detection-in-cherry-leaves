import streamlit as st

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