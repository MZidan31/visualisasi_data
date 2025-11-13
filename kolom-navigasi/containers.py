import streamlit as st
import numpy as np

st.title("Container")

st.write("Kelompok 1")
st.markdown("""
- MUHAMMAD ZIDAN (0110222124)
- IQLIMA FASHA RIZQIA (0110122006)
""")

with st.container():
    st.write("Element Inside Contianer")
    #Defining Chart Element
    st.line_chart(np.random.randn(40, 4))
st.write("Element Outside Container")