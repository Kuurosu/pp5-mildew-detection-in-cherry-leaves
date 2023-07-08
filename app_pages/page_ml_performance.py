import streamlit as st
import matplotlib.pyplot as plt

def page_ml_performance_metrics():
  version = 'v1'

  st.write("### Train, Validation and Test Set: Labels Frequencies")

  labels_distribution = plt.imread(f"outputs/{version}/label_distribution.png")
  st.image(labels_distribution, caption='Labels Distribution on Train, Validation and Test Sets')
  st.write("---")