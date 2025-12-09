import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# KONFIGURASI HALAMAN
st.set_page_config(page_title="Praktikum 5 - Scatter Plot", layout="wide")

# IDENTITAS KELOMPOK
st.caption("Praktikum 5 - Scatter Plot")
st.write("Kelompok: 1")
st.markdown("""
* **MUHAMMAD ZIDAN** - 0110222280
* **IQLIMA FASHA RIZQIA** - 0110122006 
""")
st.markdown("---")

# PERSIAPAN DATA (DATASET)

# 1. Dataset Sederhana
# Catatan Profesor: Saya menambahkan satu nilai (100) di akhir 'penjualan' 
# karena jumlah data harus sama dengan 'suhu' (9 item) untuk menghindari error.
suhu = [20, 22, 24, 26, 28, 30, 32, 34, 36]
penjualan = [30, 40, 50, 60, 70, 80, 90, 95, 100] 

# 2. Dataset Tambahan (Multiple Plot)
penjualan_weekdays = [60, 70, 80, 90, 100, 110, 120, 130, 140]
penjualan_weekend = [50, 60, 70, 80, 90, 100, 110, 120, 130]

# 3. Data untuk Analisis (DataFrame)
# Catatan Profesor: Koma yang hilang pada dictionary sudah diperbaiki.
data = {
    'suhu' : [20, 22, 24, 26, 28, 30, 32, 34, 36],
    'penjualan_Cokelat' : [20, 25, 30, 35, 40, 45, 50, 55, 60],
    'penjualan_Vanila' : [45, 50, 55, 60, 65, 70, 75, 80, 85],
    'penjualan_Stroberi' : [35, 40, 45, 50, 55, 60, 65, 70, 75],
    'kelembapan' : [50, 60, 70, 80, 90, 100, 110, 120, 115]
}

# Konversi ke DataFrame
df = pd.DataFrame(data)

# SIDEBAR & ROUTING

st.sidebar.header("Pengaturan Visualisasi") # Diperbaiki dari st.sidebar() menjadi st.sidebar.header()

# Menu di Sidebar
option = st.sidebar.selectbox(
    "Pilih Jenis Scatter Plot",
    (
        "Basic Scatter Plot",
        "Kustomisasi Scatter Plot",
        "Multiple Scatter Plot",
        "Analisis Scatter Plot"
    )
)

# Judul Utama Dinamis
st.title(f"Visualisasi: {option}")

# LOGIKA VISUALISASI

# 1. BASIC SCATTER PLOT
if option == "Basic Scatter Plot":
    st.write("Grafik scatter plot sederhana menunjukkan hubungan suhu dan penjualan.")
    
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(suhu, penjualan, color='blue')
    ax.set_title('Hubungan Penjualan Es Krim dan Suhu')
    ax.set_xlabel('Suhu (°C)')
    ax.set_ylabel('Penjualan')
    st.pyplot(fig)

# 2. KUSTOMISASI SCATTER PLOT
elif option == "Kustomisasi Scatter Plot":
    st.write("Grafik dengan kustomisasi warna, ukuran, dan transparansi.")
    
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(suhu, penjualan, color='orange', s=100, edgecolor='black', alpha=0.7)
    ax.set_title('Hubungan Penjualan Es Krim dan Suhu (Kustom)')
    ax.set_xlabel('Suhu (°C)')
    ax.set_ylabel('Penjualan')
    ax.grid(True, linestyle='--', alpha=0.5)
    st.pyplot(fig)

# 3. MULTIPLE SCATTER PLOT
elif option == "Multiple Scatter Plot":
    st.write("Membandingkan penjualan pada Hari Kerja (Weekdays) vs Akhir Pekan (Weekend).")
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(suhu, penjualan_weekdays, color='green', label='Hari Kerja', s=80)
    ax.scatter(suhu, penjualan_weekend, color='red', label='Akhir Pekan', s=80)
    
    ax.set_title('Perbandingan Penjualan: Weekdays vs Weekend')
    ax.set_xlabel('Suhu (°C)')
    ax.set_ylabel('Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# 4. ANALISIS SCATTER PLOT (DATAFRAME)
elif option == "Analisis Scatter Plot":
    st.write("Analisis interaktif menggunakan data DataFrame.")
    
    # Sub-menu khusus untuk halaman analisis
    jenis_rasa = st.selectbox(
        "Pilih Varian Rasa Es Krim:",
        ["Cokelat", "Vanila", "Stroberi"]
    )
    
    # Menentukan kolom data berdasarkan pilihan
    kolom_y = f"penjualan_{jenis_rasa}"
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Data Mentah")
        st.dataframe(df[['suhu', kolom_y, 'kelembapan']])
        
    with col2:
        st.subheader("Grafik Analisis")
        fig, ax = plt.subplots(figsize=(8, 5))
        
        # Scatter plot 4 dimensi (x, y, warna=kelembapan)
        scatter = ax.scatter(
            df['suhu'], 
            df[kolom_y], 
            c=df['kelembapan'], 
            cmap='viridis', 
            s=120, 
            edgecolor='black',
            alpha=0.8
        )
        
        ax.set_title(f'Penjualan {jenis_rasa} vs Suhu & Kelembapan')
        ax.set_xlabel('Suhu (°C)')
        ax.set_ylabel(f'Penjualan {jenis_rasa}')
        ax.grid(True, linestyle='--', alpha=0.3)
        
        # Menambahkan colorbar
        cbar = fig.colorbar(scatter, ax=ax)
        cbar.set_label('Kelembapan')
        
        st.pyplot(fig)

    # Insight Singkat
    korelasi = df['suhu'].corr(df[kolom_y])
    st.info(f"Korelasi antara Suhu dan Penjualan {jenis_rasa}: {korelasi:.2f}")