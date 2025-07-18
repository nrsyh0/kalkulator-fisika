import streamlit as st
from PIL import Image
import math

st.set_page_config(page_title="Kalkulator & Kuis Fisika", layout="centered")
st.title("🔬 Kalkulator & Kuis Fisika 🎓")

menu = st.sidebar.radio("📚 Navigasi", ["Dashboard", "Kalkulator", "Kuis", "Tentang Aplikasi"])

# -----------------------------------
# DASHBOARD
# -----------------------------------
if menu == "Dashboard":
    st.header("👋 Selamat datang di Aplikasi Kalkulator & Kuis Fisika")
    try:
        image = Image.open("fisika.jpg")
        st.image(image, use_container_width=True)
    except:
        st.warning("Gambar tidak ditemukan atau gagal dimuat.")
    st.markdown("""
    ### 🧠 Fitur Utama:
    - 🔢 Kalkulator Fisika (Kinematika, Dinamika, Konversi Satuan)
    - ❓ Kuis Interaktif untuk menguji pemahaman
    - 📘 Penjelasan materi dan cara penggunaan
    """)

# -----------------------------------
# KALKULATOR
# -----------------------------------
elif menu == "Kalkulator":
    kategori = st.selectbox("Pilih kategori kalkulator:", ["Kinematika", "Dinamika", "Konversi Satuan"])

    if kategori == "Kinematika":
        st.subheader("📌 Kinematika")
        sub = st.selectbox("Pilih perhitungan:", ["Jarak", "Kecepatan", "Waktu", "Percepatan"])

        if sub == "Jarak":
            v = st.number_input("Kecepatan (m/s):", value=0.0)
            t = st.number_input("Waktu (s):", value=0.0)
            if st.button("Hitung Jarak"):
                s = v * t
                st.success(f"Jarak = {s} meter")

        elif sub == "Kecepatan":
            s = st.number_input("Jarak (m):", value=0.0)
            t = st.number_input("Waktu (s):", value=0.0)
            if st.button("Hitung Kecepatan"):
                if t != 0:
                    v = s / t
                    st.success(f"Kecepatan = {v} m/s")
                else:
                    st.error("Waktu tidak boleh 0")

        elif sub == "Waktu":
            s = st.number_input("Jarak (m):", value=0.0)
            v = st.number_input("Kecepatan (m/s):", value=0.0)
            if st.button("Hitung Waktu"):
                if v != 0:
                    t = s / v
                    st.success(f"Waktu = {t} detik")
                else:
                    st.error("Kecepatan tidak boleh 0")

        elif sub == "Percepatan":
            v_akhir = st.number_input("Kecepatan Akhir (m/s):", value=0.0)
            v_awal = st.number_input("Kecepatan Awal (m/s):", value=0.0)
            t = st.number_input("Waktu (s):", value=0.0)
            if st.button("Hitung Percepatan"):
                if t != 0:
                    a = (v_akhir - v_awal) / t
                    st.success(f"Percepatan = {a} m/s²")
                else:
                    st.error("Waktu tidak boleh 0")

    elif kategori == "Dinamika":
        st.subheader("📌 Dinamika")
        sub = st.selectbox("Pilih perhitungan:", ["Gaya", "Tekanan", "Energi Kinetik"])

        if sub == "Gaya":
            m = st.number_input("Massa (kg):", value=0.0)
            a = st.number_input("Percepatan (m/s²):", value=0.0)
            if st.button("Hitung Gaya"):
                f = m * a
