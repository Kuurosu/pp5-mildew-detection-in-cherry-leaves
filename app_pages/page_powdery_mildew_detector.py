import streamlit as st

from src.data_management import download_dataframe_as_csv


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