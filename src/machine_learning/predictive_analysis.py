import pandas as pd
import plotly.express as px
import streamlit as st

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