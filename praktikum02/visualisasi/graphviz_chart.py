import streamlit as st
import graphviz as graphviz

st.title('Graphviz')

st.write("Kelompok 1")
st.markdown("""
- MUHAMMAD ZIDAN (0110222124)
- IQLIMA FASHA RIZQIA (0110122006)
""")

#Creating graph object
# Kode di modul kurang tanda kutip, ditambahkan ''' agar bisa run
st.graphviz_chart('''
digraph {
"Training Data" -> "ML Algorithm"
"ML Algorithm" -> "Model"
"Model" -> "Result Forecasting"
"New Data" -> "Model"
}
''')