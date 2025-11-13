import streamlit as st

st.write("Kelompok 1")
st.markdown("""
- MUHAMMAD ZIDAN (0110222124)
- IQLIMA FASHA RIZQIA (0110122006)
""")

#Sidebar
st.sidebar.title("Sidebar")
st.sidebar.radio("Are you a New User", ["Yes", "No"])
st.sidebar.slider("Select a Number", 0,10)