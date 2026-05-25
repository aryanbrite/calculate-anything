import streamlit as st
from datetime import date
at=date.today()
dat=str(at)
st.set_page_config(
    page_title="Calculate",
    page_icon="💡",
)

st.title("Calculate")
col1, col2=st.columns(2,gap="xxsmall")
with col2:
    st.write("Hi, This project is made on Streamlit. A python framework. Expolre to find the things you can find !")
    st.write("On the left side of the screen you will find the menu of all the calculators.")
with col1:
    st.image("https://www.nicepng.com/png/full/952-9528838_anime-animal-transparent-background.png", width=240)
st.write("How likely you would reccomend this app to your friend ?")
st.feedback("stars")
st.write(dat)