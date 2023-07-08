import streamlit as st
import matplotlib.pyplot as plt

def page_ml_performance_metrics():
  version = 'v1'

  st.write("### Train, Validation and Test Set: Labels Frequencies")

  labels_distribution = plt.imread(f"outputs/{version}/label_distribution.png")
  st.image(labels_distribution, caption='Labels Distribution on Train, Validation and Test Sets')
  st.write("---")
  
  st.write("### Model History")
  col1, col2 = st.columns(2)
  with col1: 
    model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
    st.image(model_acc, caption='Model Training Accuracy')
  with col2:
    model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
    st.image(model_loss, caption='Model Training Losses')
  st.write("---")
  