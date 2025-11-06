#import library yang dibutuhkan
import streamlit as st

# Bag 1: Text Elemen
# header - untuk membuat tulisan header
st.header("Ini Header") # membuat header
st.subheader("Ini Sub Header") # buat subjudul
st.text("Ini teks biasa tanpa format") # buat teks polos
st.markdown("**ini teks bold** dan *ini teks italic*") # markdown untuk memformat teks bold/italic
st.caption("Ini Caption") # teks kecil dibawah elemen (bisa untuk penjelasan/detail/definisi)
st.title("Ini judul") # buat judul

#Just Trial / Demo
st.title("Praktikum 1 Visualisasi Data") # ini judul praktikum hari ini
st.subheader("Bagian 1: Teks Elemen")
st.markdown("""
            1. Muhammad Zidan - 0110222280
            2. Iqlima Fasha Rizqia - 0110122006
            """)

#Bag 2: Menampilkan rumus (LaTex)
st.header("Displaying LaTeX")
st.latex(r''' \cos^2\theta = 1-2\sin^2\theta ''') # rumus trigonometri
st.latex(r''' (a+b)^2 = a^2 + b^2 + 2ab ''') # rumus binominal

#Bag 3: Menampilkan Kode Program
st.header("Displaying Code")
st.subheader("Python Code")

#Simpan ke Variabel
code = '''
def hello :
    print("Hello, Streamlit!")
    '''
# st.code() tampilkan potongan kode dengan format rapi
st.code(code, language='python')

st.subheader("Java Code")
st.code("""
        public class GFG {
            public static void main{string arg[]} {
                system.out.printIn("Hello World!") ;
            }
        }
        """, language='java')
# fungsi st.code() bisa untuk bahasa pemrograman lain

st.subheader("Javascript Code")
st.code("""
        <script>
        try {
            addalert("Welcome Guest"); // kesalahan ketik (addalert) sengaja dibuat untuk menimbulkan error
        }
        catch(err) {
            document.getElementById("demo").innerHTML = err.message; // menampilkan pesan error di elemen HTML dengan id 'demo'
        }
        </script>
        """, language='javascript')
# Kode hanya contoh bagaimana menangani error (exception) di JavaScript
# Hasilnya tidak dijalankan di streamlit, hanya display contoh kode