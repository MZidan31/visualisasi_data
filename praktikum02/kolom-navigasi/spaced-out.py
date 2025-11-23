import streamlit as st
from PIL import Image
img = Image.open("D:/VISUALISASI_DATA/assets/badak.jpg")

st.title("Spaced-Out Columns")
#Defining two rows
st.write("Kelompok 1")
st.markdown("""
- MUHAMMAD ZIDAN (0110222124)
- IQLIMA FASHA RIZQIA (0110122006)
""")

for _ in range(2):
    # Defining no. of columns with size
    cols = st.columns((3, 1, 2, 1))
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)

    