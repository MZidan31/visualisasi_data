# Import Library
import streamlit as st 
import pandas as pd     # kelola data dalam bentuk tabel
import numpy as np      # kelola data numerik acak
import altair as alt    # kelola chart interaktif 

st.title("Praktikum 1 Visualisasi Data") # ini judul praktikum hari ini
st.subheader("Bagian 2: Data Elemen")
st.markdown("""
            Kelompok 1  :
            - Muhammad Zidan       - 0110222280
            - Iqlima Fasha Rizqia  - 0110122006
            """)

# Data Frame
st.subheader("DataFrame")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range (10))
)

# Display Data Frame
st.dataframe(df)

# Highlight Nilai Minimum
st.subheader("Highlight Minimum Value di DataFrame")

# Highlight nilai terkecil disetiap kolom dataframe
# Axis=0 bekerja perkolom
st.dataframe(df.style.highlight_min(axis=0))

# Tabel Statis
st.subheader("Tabel Statis")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range (10))
)
# Display Tabel Statis
st.table(df)

# Metrics: Komponen tampilan angka penting
st.subheader("Metrics")
st.metric(label="Temperature", value="31 °C", delta="1.2 °C") # Kenaikan 1.2 °C

# Metrics sesuai delta_color
# delta-color

# "Normal" (default) : naik -> Hijau & turun -> Merah

# Definisikan Variabel Metrics
col1, col2, col3 = st.columns(3)

# Menampilkan Indikator Data
col1.metric("Curah Hujan", "100 cm", "10 cm")
col2.metric(label="Populasi", value="123 Miliar", delta="1 Miliar", delta_color="inverse")
col3.metric(label="Pelanggan", value=100, delta=10, delta_color="off")

st.metric(label="speed", value=None, delta=0)
st.metric("Tress", "91456", "-1132649")