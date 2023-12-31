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

    st.warning(
        f"**Project Dataset**\n\n"
        f"The project dataset comprises a collection of meticulously captured "
        f"images of cherry leaves. It consists of 2104 images of healthy leaves "
        f"and an equal number of images depicting leaves affected by powdery "
        f"mildew. Each leaf was individually photographed against a neutral "
        f"background to ensure accurate representation.\n\n"
        f"This comprehensive dataset forms the foundation for our analysis and "
        f"model development, enabling us to explore the visual characteristics "
        f"and patterns associated with healthy and affected leaves. By leveraging "
        f"this dataset, we aim to develop a robust model for powdery mildew "
        f"detection in cherry trees, contributing to effective disease management "
        f"strategies and crop protection measures."
    )

    st.success(
        f"The project encompasses three key business requirements:\n\n"
        f"1 - Conduct a comprehensive visual analysis to accurately differentiate "
        f"between a healthy leaf and an infected leaf affected by powdery mildew.\n\n"
        f"2 - Develop a robust prediction model capable of accurately determining "
        f"whether a given leaf is infected by powdery mildew or remains unaffected.\n\n"
        f"3 - Provide an easily accessible platform to download prediction reports "
        f"containing the results of the examined leaves, aiding in further analysis "
        f"and decision-making processes."
    )

    st.write(
        f"For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/kuurosu/pp5-mildew-detection-in-cherry-leaves#readme).")