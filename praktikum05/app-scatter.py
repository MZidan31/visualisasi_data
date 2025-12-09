import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Konfigurasi Halaman Streamlit
st.set_page_config(page_title="Modul 5: Scatter Plot", layout="wide")

# ==========================================
# IDENTITAS KELOMPOK (SIDEBAR)
# ==========================================
st.sidebar.markdown("### Identitas Kelompok")
st.sidebar.caption("Praktikum 5 - Scatter Plot") # Dikoreksi dari Praktikum 3
st.sidebar.write("**Kelompok: 1**")
st.sidebar.markdown("""
1. MUHAMMAD ZIDAN - 0110222280
2. IQLIMA FASHA RIZQIA - 0110122006 
""")
st.sidebar.markdown("---")

# Sidebar untuk navigasi materi
st.sidebar.title("Navigasi Modul 5")
pilihan_modul = st.sidebar.radio(
    "Pilih Latihan:",
    ("1. Visualisasi Sederhana (Matplotlib)", "2. Analisis Data Interaktif (Pandas)")
)

# ==========================================
# BAGIAN A: Visualisasi Sederhana (Halaman 3 PDF)
# ==========================================
if pilihan_modul == "1. Visualisasi Sederhana (Matplotlib)":
    st.title('Visualisasi Hubungan Penjualan Es Krim dengan Suhu')
    st.markdown("Implementasi dasar Matplotlib di dalam Streamlit.")

    # Data dummy
    suhu = [20, 22, 24, 26, 28, 30, 32, 34, 36]
    penjualan = [50, 60, 70, 90, 100, 110, 130, 150, 180]
    
    # Data tambahan untuk kategori hari
    penjualan_kerja = [50, 60, 70, 80, 90, 100, 110, 120, 130]
    penjualan_akhir_pekan = [60, 70, 80, 100, 110, 120, 140, 160, 200]

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Scatter Plot Dasar")
        fig1, ax1 = plt.subplots()
        ax1.scatter(suhu, penjualan, color="blue")
        ax1.set_title('Hubungan Penjualan Es Krim dan Suhu')
        ax1.set_xlabel('Suhu (°C)')
        ax1.set_ylabel('Penjualan Es Krim')
        st.pyplot(fig1)

    with col2:
        st.subheader("Scatter Plot Kustom")
        fig2, ax2 = plt.subplots()
        ax2.scatter(suhu, penjualan, color='orange', s=100, edgecolor='black', alpha=0.7)
        ax2.set_title('Hubungan Penjualan Es Krim dan Suhu (Kustom)')
        ax2.set_xlabel('Suhu (°C)')
        ax2.set_ylabel('Penjualan Es Krim')
        ax2.grid(True)
        st.pyplot(fig2)

    st.subheader("Scatter Plot Multiple (Hari Kerja vs Akhir Pekan)")
    fig3, ax3 = plt.subplots(figsize=(10, 5))
    ax3.scatter(suhu, penjualan_kerja, color='green', label='Hari Kerja', s=80)
    ax3.scatter(suhu, penjualan_akhir_pekan, color='purple', label='Akhir Pekan', s=80)
    ax3.set_title('Penjualan Es Krim Berdasarkan Hari')
    ax3.set_xlabel('Suhu (°C)')
    ax3.set_ylabel('Penjualan Es Krim')
    ax3.legend()
    ax3.grid(True, linestyle='--', alpha=0.5)
    st.pyplot(fig3)

# ==========================================
# BAGIAN B: Analisis Data Interaktif (Halaman 4 PDF)
# ==========================================
elif pilihan_modul == "2. Analisis Data Interaktif (Pandas)":
    st.title("Analisis Penjualan Es Krim Berdasarkan Suhu")
    st.markdown("Menggunakan **Pandas** untuk manipulasi data dinamis.")

    # Data dummy (Koreksi: Sintaks Dictionary diperbaiki)
    data = {
        'Suhu': [20, 22, 24, 26, 28, 30, 32, 34, 36],
        'Penjualan_Cokelat': [50, 60, 70, 80, 90, 100, 110, 120, 130],
        'Penjualan_Vanila': [60, 70, 80, 90, 100, 110, 120, 130, 140],
        'Penjualan_Stroberi': [40, 50, 60, 70, 80, 90, 100, 110, 120],
        'Kelembapan': [60, 65, 70, 75, 80, 85, 90, 95, 100]
    }

    # Konversi data ke Dataframe
    df = pd.DataFrame(data)

    # Sidebar Pilihan
    st.sidebar.subheader("Pengaturan Parameter")
    jenis_eskrim = st.sidebar.selectbox(
        'Pilih Jenis Es Krim:', 
        ['Cokelat', 'Vanila', 'Stroberi']
    )

    # Logika Penentuan Data
    kolom_terpilih = f"Penjualan_{jenis_eskrim}"
    penjualan = df[kolom_terpilih]

    # Layout: Tabel di kiri, Grafik di kanan
    col_kiri, col_kanan = st.columns([1, 2])

    with col_kiri:
        st.subheader('Data Penjualan')
        # Menampilkan dataframe dengan highlight
        st.dataframe(df[['Suhu', 'Kelembapan', kolom_terpilih]])

    with col_kanan:
        st.subheader(f'Scatter Plot: {jenis_eskrim}')
        
        # Membuat Scatter Plot
        fig, ax = plt.subplots(figsize=(8, 5))
        
        # Plotting 4 Dimensi: x=Suhu, y=Penjualan, color=Kelembapan, size=Static
        scatter = ax.scatter(
            df['Suhu'], 
            penjualan, 
            c=df['Kelembapan'], 
            s=150, 
            cmap='coolwarm', 
            alpha=0.8,
            edgecolor='black'
        )
        
        ax.set_title(f'Hasil Penjualan {jenis_eskrim} vs Suhu & Kelembapan')
        ax.set_xlabel('Suhu (°C)')
        ax.set_ylabel(f'Penjualan {jenis_eskrim}')
        ax.grid(True, linestyle='--', alpha=0.3)
        
        # Menambahkan colorbar ke figure
        fig.colorbar(scatter, label='Kelembapan (%)')
        
        # Tampilkan scatter plot di Streamlit
        st.pyplot(fig)

    # Ringkasan Hubungan
    st.markdown("---")
    st.subheader("Analisis Hubungan")
    
    # Menghitung korelasi sederhana untuk insight tambahan
    korelasi = df['Suhu'].corr(penjualan)
    
    st.info(f"""
    Grafik di atas menunjukkan hubungan antara suhu, kelembapan, dan penjualan es krim rasa **{jenis_eskrim}**.
    
    **Insight Statistik:**
    Korelasi antara Suhu dan Penjualan {jenis_eskrim} adalah: **{korelasi:.2f}**. 
    (Nilai mendekati 1 menunjukkan hubungan positif yang sangat kuat: Semakin panas, semakin laris).
    """)