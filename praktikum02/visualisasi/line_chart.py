import streamlit as st
import pandas as pd
import numpy as np

st.title("Line Chart")
st.write("Kelompok : 1")
st.markdown("""
            - Muhammad Zidan (0110222280)
            - Fasha (NIM)
            """)

df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=["C1", "C2", "C3", "C4"]
)

st.line_chart(df)