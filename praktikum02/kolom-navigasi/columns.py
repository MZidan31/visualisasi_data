import streamlit as st
st.title("Columns")
st.write("Kelompok 1")
st.markdown("""
- MUHAMMAD ZIDAN (0110222124)
- IQLIMA FASHA RIZQIA (0110122006)
""")

#Defining Columns
col1, col2 = st.columns(2)

#Inserting Elements in column 1
col1.write("First Column")
col1.image("./assets/badak.jpg")

#Inserting Elements in column 2
col2.write("Second Column")
col2.image("./assets/badak.jpg")