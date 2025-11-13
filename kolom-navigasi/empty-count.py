import streamlit as st
import time

st.write("Kelompok 1")
st.markdown("""
- MUHAMMAD ZIDAN (0110222124)
- IQLIMA FASHA RIZQIA (0110122006)
""")

#Empty Container
with st.empty():
    for seconds in range(5):
        st.write(f" {seconds} seconds have passed")
        time.sleep(1)
    st.write(" Times up!")