import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n\n"
        f"Powdery mildew is a parasitic fungal disease caused by Podosphaera clandestina "
        f"in cherry trees. It appears as a layer of spores on leaf surfaces, primarily "
        f"affecting new growth. The disease can hinder plant growth, infect fruit, and "
        f"lead to significant crop losses.\n\n"
        f"During our examination, we carefully analyzed infected and healthy leaves. "
        f"Infected leaves display visual indicators like light-green circular lesions and "
        f"subtle white cotton-like growth. These symptoms extend to fruit, impacting yield "
        f"and quality.\n\n"
        f"Our research sheds light on identifying and understanding the implications of "
        f"powdery mildew in cherry trees."
        )

    