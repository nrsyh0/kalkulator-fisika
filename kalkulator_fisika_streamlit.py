# kalkulator_fisika_streamlit.py
import streamlit as st
from PIL import Image
import math

st.set_page_config(page_title="Kalkulator Fisika", layout="centered")
st.markdown("""
    <style>
        .stApp {
            background-color: #f5f5fa;
            font-family: 'Segoe UI', sans-serif;
        }
        h1, h2, h3 {
            color: #003366;
        }
        .sidebar .sidebar-content {
            background-color: #ddeeff;
        }
    </style>
""", unsafe_allow_html=True)

menu = st.sidebar.radio("Navigasi", ("Dashboard", "Kalkulator", "Kuis", "Tentang"))

# -------------------- DASHBOARD --------------------
if menu == "Dashboard":
    st.title("🏠 Dashboard")
    st.write("Selamat datang di **Kalkulator Fisika Interaktif**!")

    try:
        image = Image.open("fisika.jpg")
        st.image(image, caption="Ilustrasi Fisika", use_column_width=True)
    except:
        st.warning("Gambar tidak ditemukan.")

    st.markdown("""
    ### Fitur:
    - 💡 **Kalkulator Fisika**: Kinematika, Dinamika, Konversi Satuan
    - 🧠 **Kuis Interaktif**: Uji pemahaman konsep
    - 📘 **Tentang**: Penjelasan fitur dan materi
    """)

# -------------------- KALKULATOR --------------------
elif menu == "Kalkulator":
    st.title("🧮 Kalkulator Fisika")
    tab1, tab2, tab3 = st.tabs(["Kinematika", "Dinamika", "Konversi Satuan"])

    # Kinematika
    with tab1:
        st.header("Kinematika")
        opsi = st.selectbox("Pilih perhitungan:", ["Jarak (s)", "Kecepatan (v)", "Waktu (t)", "Percepatan (a)"])
        if opsi == "Jarak (s)":
            v = st.number_input("Kecepatan (m/s)", step=0.1)
            t = st.number_input("Waktu (s)", step=0.1)
            if st.button("Hitung", key="s"):
                st.success(f"Jarak = {v * t:.2f} meter")
        elif opsi == "Kecepatan (v)":
            s = st.number_input("Jarak (m)", step=0.1)
            t = st.number_input("Waktu (s)", step=0.1)
            if st.button("Hitung", key="v") and t != 0:
                st.success(f"Kecepatan = {s / t:.2f} m/s")
        elif opsi == "Waktu (t)":
            s = st.number_input("Jarak (m)", step=0.1)
            v = st.number_input("Kecepatan (m/s)", step=0.1)
            if st.button("Hitung", key="t") and v != 0:
                st.success(f"Waktu = {s / v:.2f} detik")
        elif opsi == "Percepatan (a)":
            v1 = st.number_input("Kecepatan awal v1 (m/s)", step=0.1)
            v2 = st.number_input("Kecepatan akhir v2 (m/s)", step=0.1)
            t = st.number_input("Waktu (s)", step=0.1)
            if st.button("Hitung", key="a") and t != 0:
                st.success(f"Percepatan = {(v2 - v1) / t:.2f} m/s²")

    # Dinamika
    with tab2:
        st.header("Dinamika")
        opsi = st.selectbox("Pilih perhitungan:", ["Gaya (F)", "Tekanan (P)", "Energi Kinetik (Ek)"])
        if opsi == "Gaya (F)":
            m = st.number_input("Massa (kg)", step=0.1)
            a = st.number_input("Percepatan (m/s²)", step=0.1)
            if st.button("Hitung", key="f"):
                st.success(f"Gaya = {m * a:.2f} Newton")
        elif opsi == "Tekanan (P)":
            F = st.number_input("Gaya (N)", step=0.1)
            A = st.number_input("Luas (m²)", step=0.01)
            if A != 0 and st.button("Hitung", key="p"):
                st.success(f"Tekanan = {F / A:.2f} Pascal")
        elif opsi == "Energi Kinetik (Ek)":
            m = st.number_input("Massa (kg)", step=0.1)
            v = st.number_input("Kecepatan (m/s)", step=0.1)
            if st.button("Hitung", key="ek"):
                st.success(f"Energi Kinetik = {0.5 * m * v ** 2:.2f} Joule")

    # Konversi
    with tab3:
        st.header("Konversi Satuan")
        jenis = st.selectbox("Jenis Konversi", ["Energi", "Tekanan", "Panjang", "Waktu"])
        satuan_dict = {
            "Energi": {"joule": 1, "kjoule": 1e3, "kalori": 4.184, "kwh": 3.6e6},
            "Tekanan": {"pa": 1, "kpa": 1e3, "atm": 101325, "bar": 1e5},
            "Panjang": {"m": 1, "km": 1e3, "cm": 1e-2, "inch": 0.0254},
            "Waktu": {"detik": 1, "menit": 60, "jam": 3600, "hari": 86400},
        }
        val = st.number_input(f"Nilai {jenis}", step=0.1)
        satuan = satuan_dict[jenis]
        dari = st.selectbox("Dari", satuan.keys())
        ke = st.selectbox("Ke", satuan.keys())
        if st.button("Konversi", key="konv"):
            hasil = val * satuan[dari] / satuan[ke]
            st.success(f"Hasil: {hasil:.4f} {ke}")

# -------------------- KUIS --------------------
elif menu == "Kuis":
    st.title("❓ Kuis Fisika")
    
    soal = [
        {"q": "Sebuah benda bermassa 10 kg di lantai datar. Gaya normal?", "a": "98 N"},
        {"q": "Benda 10 kg di bidang miring 53°. Gaya normal?", "a": "~59 N"},
        {"q": "Kecepatan awal 10 m/s, berhenti dalam 20 s. Perlambatan dan jarak?", "a": "0.5 m/s² dan 100 m"},
        {"q": "Benda jatuh bebas dari 20 m. Waktu dan kecepatan saat jatuh?", "a": "2 s dan 20 m/s"},
    ]

    if "idx" not in st.session_state:
        st.session_state.idx = 0
        st.session_state.score = 0

    if st.session_state.idx < len(soal):
        st.subheader(f"Soal {st.session_state.idx + 1}")
        q = soal[st.session_state.idx]
        st.write(q["q"])
        jawaban = st.text_input("Jawabanmu:", key=f"jawaban_{st.session_state.idx}")
        if st.button("Kirim Jawaban", key=f"kirim_{st.session_state.idx}"):
            if jawaban.strip().lower() in q["a"].lower():
                st.success("Benar!")
                st.session_state.score += 1
            else:
                st.error(f"Salah. Jawaban: {q['a']}")
            st.session_state.idx += 1
            st.experimental_rerun()
    else:
        st.success(f"Skor akhir: {st.session_state.score}/{len(soal)}")
        if st.button("Ulangi Kuis"):
            st.session_state.idx = 0
            st.session_state.score = 0
            st.experimental_rerun()

# -------------------- TENTANG --------------------
else:
    st.title("ℹ️ Tentang Aplikasi")
    st.markdown("""
    ## 📘 Deskripsi Aplikasi
    Aplikasi ini adalah alat bantu belajar fisika interaktif.

    ### 🧮 Kinematika
    - Menghitung **jarak**, **kecepatan**, **waktu**, dan **percepatan**.

    ### 💥 Dinamika
    - Menghitung **gaya**, **tekanan**, dan **energi kinetik**.

    ### 🔄 Konversi Satuan
    - Konversi **energi**, **tekanan**, **panjang**, dan **waktu** antar satuan umum.

    ### ❓ Kuis
    - Soal-soal konsep kinematika, gaya normal, dan gerak vertikal.
    - Melatih logika dan pemahaman rumus.

    ## 🔧 Cara Menggunakan Aplikasi
    1. Pilih menu dari sidebar: Dashboard, Kalkulator, Kuis, atau Tentang.
    2. Masukkan nilai yang diminta sesuai konteks.
    3. Klik tombol "Hitung" atau "Konversi".
    4. Buka halaman Kuis dan jawab pertanyaan.

    ## 📩 Hubungi Kami
    Silakan tinggalkan pesan Anda:
    - Email: **aisyah@example.com**
    - Instagram: **@aisyah_fisika**
    """)
