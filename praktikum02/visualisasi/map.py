import streamlit as st
import pandas as pd
import numpy as np

# Judul di modul salah ('Map )'), diganti agar benar
st.title('Map')

st.write("Kelompok 1")
st.markdown("""
- MUHAMMAD ZIDAN (0110222124)
- IQLIMA FASHA RIZQIA (0110122006)
""")

#Defining Latitude and Longitude
locate_map = pd.DataFrame(
np.random.randn(50, 2)/[10,10] + [15.4589, 75.0078],
columns = ['latitude', 'longitude'])

#Map Function
st.map(locate_map)