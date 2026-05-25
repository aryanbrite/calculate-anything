import streamlit as st
st.set_page_config(layout="wide")
col1, col2, col3, col4=st.columns(4, gap="xxsmall")
with col1:
    st.image("https://static.vecteezy.com/system/resources/thumbnails/068/360/341/small/cute-cartoon-brown-cat-peeking-over-line-illustration-kawaii-cat-sticker-hand-drawn-cartoon-free-png.png",width=200)
with col2:    
    st.title("BMI Calculator")