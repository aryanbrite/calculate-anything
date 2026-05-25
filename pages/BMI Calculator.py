import streamlit as st
st.set_page_config(
    page_title="BMI Calclulator",
    page_icon="💡",
)

col1, col2=st.columns([3,10], gap="xsmall", vertical_alignment="center")
with col1:
    st.image("images/favpng_7d1161465538a1c0897ab46880a7ca8b.png",width=150)
with col2:    
    st.title("BMI Calculator")


st.slider("weight",0,200)
import streamlit as st

theme = st.segmented_control(
    "",
    ["Kg", "Pounds"]
)


