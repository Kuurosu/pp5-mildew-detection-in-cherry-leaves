import streamlit as st

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
  load_model_and_predict,
  resize_input_image,
  plot_predictions_probabilities
  )

def page_powdery_mildew_detector_body():
  st.write("yo")