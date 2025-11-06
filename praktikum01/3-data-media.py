import streamlit as st 
# Pustaka 'base64' diimpor di kode asli, tetapi tidak digunakan di sini.
# Saya meninggalkannya karena mungkin akan digunakan untuk fungsi lain seperti background.
import base64 

# --- Bagian 1: Informasi Praktikum dan Tim ---

# Menampilkan judul utama aplikasi
st.title("Praktikum 1 Visualisasi Data") 

# Menampilkan subjudul untuk bagian saat ini
st.subheader("Bagian 3: Data Media")

# Menampilkan informasi anggota kelompok menggunakan format Markdown
st.markdown("""
Kelompok 1 :
- Muhammad Zidan - 0110222280
- Iqlima Fasha Rizqia - 0110122006
""")

# --- Bagian 2: Menampilkan Satu Gambar (Single Image Display) ---

# Memberikan judul untuk bagian tampilan satu gambar
st.write("---")
st.write("Displaying an Images (Gambar Tunggal)")

# Menampilkan satu gambar menggunakan path absolut yang ditentukan
# Catatan: Pastikan file 'badak.jpg' benar-benar ada di path ini saat menjalankan script.
st.image("D:/VISUALISASI_DATA/praktikum01/assets/badak.jpg")

# Memberikan atribusi (sumber) gambar tersebut
st.write("Sumber Gambar: Wediao.com")

# --- Bagian 3: Menampilkan Banyak Gambar Secara Vertikal ---

st.write("---")
st.write("Displaying Multiple Images (Versi Vertikal)")
# Memberikan label untuk versi tampilan
st.write("Vertical Version")

# Mendefinisikan list (array) yang berisi path ke berbagai file gambar
# Variabel ini didefinisikan tetapi tidak digunakan dalam tampilan vertikal di bawah (hanya path tunggal yang digunakan).
animal_images_vertical = [
    'D:/VISUALISASI_DATA/praktikum01/assets/kakatua.jpg',
    'D:/VISUALISASI_DATA/praktikum01/assets/kucing.jpg',
    'D:/VISUALISASI_DATA/praktikum01/assets/badak.jpg',
    'D:/VISUALISASI_DATA/praktikum01/assets/orangutan.jfif',
]

# Menampilkan gambar satu per satu secara berurutan (akan tampil vertikal secara default)
# Setiap gambar diberi lebar (width) yang berbeda
st.image('D:/VISUALISASI_DATA/praktikum01/assets/kakatua.jpg', width=90, caption="Kakatua")
st.image('D:/VISUALISASI_DATA/praktikum01/assets/kucing.jpg', width=190, caption="Kucing")
st.image('D:/VISUALISASI_DATA/praktikum01/assets/badak.jpg', width=130, caption="Badak")
st.image('D:/VISUALISASI_DATA/praktikum01/assets/orangutan.jfif', width=150, caption="Orangutan")

# Memberikan atribusi (sumber) gambar
st.write("Sumber Gambar : Google.com")


# --- Bagian 4: Menampilkan Banyak Gambar Secara Horizontal ---

st.write("---")
st.write("Displaying Multiple Images (Versi Horizontal)")
# Memberikan label untuk versi tampilan
st.write("Horizontal Version")

# Mendefinisikan list (array) path gambar untuk ditampilkan secara horizontal.
# Catatan: List ini mendefinisikan ulang list dari bagian sebelumnya, yang mungkin kurang efisien
# namun dipertahankan sesuai struktur kode asli.
animal_images_horizontal = [
    'D:/VISUALISASI_DATA/praktikum01/assets/kakatua.jpg',
    'D:/VISUALISASI_DATA/praktikum01/assets/kucing.jpg',
    'D:/VISUALISASI_DATA/praktikum01/assets/badak.jpg',
    'D:/VISUALISASI_DATA/praktikum01/assets/orangutan.jfif',
]

# Streamlit secara otomatis menampilkan semua gambar dalam list sebagai satu baris horizontal
# jika list tersebut berisi path file (atau objek gambar PIL).
# 'width=150' mengatur lebar maksimum untuk setiap gambar dalam baris.
st.image(animal_images_horizontal, width=150)

# Memberikan atribusi (sumber) gambar
st.write("Sumber Gambar : Google.com")

# -------------------

import streamlit as st
from PIL import Image
import base64

# --- Bagian Pertama: Menampilkan dan Mengubah Ukuran Gambar ---

# Memuat gambar asli dari path yang ditentukan
# Pastikan file "animal1.jpg" ada di lokasi "D:/" saat menjalankan script.
original_image = Image.open("D:/VISUALISASI_DATA/praktikum01/assets/badak.jpg") 

# Menampilkan judul untuk gambar asli
st.title("Original Image")

# Menampilkan gambar asli di aplikasi Streamlit
st.image(original_image)

# Komentar: Mengubah Ukuran Gambar menjadi 600x400
# Mengubah ukuran gambar menggunakan metode .resize() dari PIL
resized_image = original_image.resize((600, 400)) 

# Menampilkan judul untuk gambar yang telah diubah ukurannya
st.title("Resized Image")

# Menampilkan gambar yang telah diubah ukurannya di aplikasi Streamlit
st.image(resized_image)

# --- Bagian Kedua: Menetapkan Gambar sebagai Latar Belakang (Background) ---

# Fungsi untuk mengatur gambar lokal sebagai latar belakang aplikasi Streamlit
def add_local_background_image_(image_path):
    # Membuka file gambar dalam mode binary ('rb')
    with open(image_path, "rb") as image:
        # Mengkodekan konten gambar ke dalam format base64
        encoded_string = base64.b64encode(image.read())
    
    # Menampilkan kredit gambar
    st.write("Image Courtesy: google")

    # Menggunakan st.markdown dengan unsafe_allow_html=True untuk menyuntikkan CSS kustom
    st.markdown(
    f"""
    <style>
    .stApp {{
        # Mengatur gambar base64 sebagai background-image menggunakan URL data
        # .decode() mengubah byte base64 menjadi string yang dapat digunakan dalam CSS
        background-image: url(data:image/jpeg;base64,{encoded_string.decode()});
        background-size: cover; # Memastikan gambar menutupi seluruh latar belakang
    }}
    </style>
    """,
    unsafe_allow_html=True # Mengizinkan penggunaan HTML/CSS yang disuntikkan
    )

    st.write("Gambar badak diatas sudah ditampilkan dengan ukuran asli dan ukuran yang sudah di edit")


# Memanggil fungsi untuk menetapkan gambar sebagai latar belakang
# Gambar latar belakang menggunakan file "animal1.jpg" dari lokasi "D:/"
# Catatan: Variabel 'image_path' dalam fungsi ini tidak secara langsung menggunakan 'original_image' dari PIL,
# melainkan jalur filenya ('D:/animal1.jpg').
add_local_background_image_("D:/VISUALISASI_DATA/praktikum01/assets/badak.jpg")

# Menambahkan spasi agar konten lain terlihat jelas di atas latar belakang
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("--- Ini Badak Teman-teman, Bukan Si Roza! ---")