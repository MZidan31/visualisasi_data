import streamlit as st
from PIL import Image

img = Image.open("D:/VISUALISASI_DATA/assets/badak.jpg")
st.title("Padding")

st.write("Kelompok 1")
st.markdown("""
- MUHAMMAD ZIDAN (0110222124)
- IQLIMA FASHA RIZQIA (0110122006)
""")

#Defining Padding with columns
col1, padding, col2 = st.columns((10,2,10))
with col1:
    col1.image(img)
with col2:
    col2.image(img)