# kalkulator_fisika_streamlit.py
# Aplikasi Streamlit dengan halaman Dashboard, Kalkulator, Kuis, dan Tentang
# Jalankan: streamlit run kalkulator_fisika_streamlit.py
# ------------------------------------------------------
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Kalkulator Fisika", layout="centered")

# Sidebar Navigation
menu = st.sidebar.radio("Navigasi", ("Dashboard", "Kalkulator", "Kuis", "Tentang"))

# ------------------------------------------------------
# DASHBOARD
# ------------------------------------------------------
if menu == "Dashboard":
    st.title("🏠 Dashboard")
    st.write("Selamat datang di **Kalkulator Fisika Web**!")

    # Tambahkan gambar dari file lokal
    try:
        image = Image.open("59789c64-09f8-4cb1-993c-df6bc87810fd.jpg")
        st.image(image, caption="Ilustrasi Fisika", use_column_width=True)
    except:
        st.warning("Gambar tidak ditemukan atau gagal dimuat.")

    st.markdown("""
    ### Fitur Aplikasi
    - **Kalkulator:** Hitung kinematika, dinamika, dan konversi satuan.
    - **Kuis:** Uji pemahaman dasar fisika.
    - **Tentang:** Informasi mengenai aplikasi dan pembuatnya.
    """)
    st.info("Gunakan menu di sidebar untuk membuka fitur.")

# ------------------------------------------------------
# KALKULATOR
# ------------------------------------------------------
elif menu == "Kalkulator":
    st.title("🧮 Kalkulator Fisika")
    tab1, tab2, tab3 = st.tabs(["Kinematika", "Dinamika", "Konversi Satuan"])

    # ---------------- KINEMATIKA ----------------
    with tab1:
        st.header("Kalkulator Kinematika")
        kin_mode = st.selectbox("Pilih yang ingin dihitung:", ["Jarak (s)", "Kecepatan (v)", "Waktu (t)", "Percepatan (a)"])
        if kin_mode == "Jarak (s)":
            v = st.number_input("Kecepatan (m/s)", step=0.1)
            t = st.number_input("Waktu (s)", step=0.1)
            if st.button("Hitung Jarak"):
                st.success(f"Jarak = {v * t:.2f} meter")
        elif kin_mode == "Kecepatan (v)":
            s = st.number_input("Jarak (m)", step=0.1)
            t = st.number_input("Waktu (s)", step=0.1)
            if t != 0 and st.button("Hitung Kecepatan"):
                st.success(f"Kecepatan = {s / t:.2f} m/s")
        elif kin_mode == "Waktu (t)":
            s = st.number_input("Jarak (m)", step=0.1)
            v = st.number_input("Kecepatan (m/s)", step=0.1)
            if v != 0 and st.button("Hitung Waktu"):
                st.success(f"Waktu = {s / v:.2f} detik")
        elif kin_mode == "Percepatan (a)":
            v1 = st.number_input("Kecepatan awal v1 (m/s)", step=0.1)
            v2 = st.number_input("Kecepatan akhir v2 (m/s)", step=0.1)
            t = st.number_input("Waktu (s)", step=0.1)
            if t != 0 and st.button("Hitung Percepatan"):
                st.success(f"Percepatan = {(v2 - v1) / t:.2f} m/s²")

    # ---------------- DINAMIKA ----------------
    with tab2:
        st.header("Kalkulator Dinamika")
        dyn_mode = st.selectbox("Pilih yang ingin dihitung:", ["Gaya (F)", "Tekanan (P)", "Energi Kinetik (Ek)"])
        if dyn_mode == "Gaya (F)":
            m = st.number_input("Massa (kg)", step=0.1)
            a = st.number_input("Percepatan (m/s²)", step=0.1)
            if st.button("Hitung Gaya"):
                st.success(f"Gaya = {m * a:.2f} Newton")
        elif dyn_mode == "Tekanan (P)":
            F = st.number_input("Gaya (N)", step=0.1)
            A = st.number_input("Luas (m²)", step=0.01)
            if A != 0 and st.button("Hitung Tekanan"):
                st.success(f"Tekanan = {F / A:.2f} Pascal")
        elif dyn_mode == "Energi Kinetik (Ek)":
            m = st.number_input("Massa (kg)", step=0.1)
            v = st.number_input("Kecepatan (m/s)", step=0.1)
            if st.button("Hitung Energi Kinetik"):
                st.success(f"Energi Kinetik = {0.5 * m * v**2:.2f} Joule")

    # ---------------- KONVERSI SATUAN ----------------
    with tab3:
        st.header("📏 Konversi Satuan Fisika Umum")
        st.write("Silakan lihat konversi berbagai satuan umum dalam fisika.")

        with open("konversi_satuan.txt", "r", encoding="utf-8") as f:
            st.markdown(f.read())

# ------------------------------------------------------
# KUIS
# ------------------------------------------------------
elif menu == "Kuis":
    # ... (tetap seperti sebelumnya)
    pass

# ------------------------------------------------------
# TENTANG
# ------------------------------------------------------
else:
    # ... (tetap seperti sebelumnya)
    pass
