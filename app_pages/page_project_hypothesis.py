import streamlit as st

def page_project_hypothesis_body():

  st.write("### Hypothesis 1 and Validation")

  st.success(
    f"Infected leaves possess noticeable and unique features that clearly \n"
    f"differentiate them from healthy leaves, enabling easy visual \n"
    f"identification."
    )
  
  st.info(
    f"We hypothesise that cherry leaves affected by powdery mildew exhibit distinctive characteristics. "
    f"Typically, the initial indication is the presence of a light-green, circular lesion on the leaf's surface, "
    f"followed by the emergence of a subtle white cotton-like growth in the affected region."
    )
  
  st.warning(
    f"The model has successfully discerned these distinctions and acquired the capacity to differentiate and generalise, resulting in precise predictions."
    f" A robust model possesses the capability to make predictions on new data beyond the training set, without relying heavily on specific instances."
    f" By capturing the underlying patterns between features and labels rather than memorising the exact relationships within the training dataset,"
    f" the model can reliably infer future observations based on the general patterns observed."
    )
