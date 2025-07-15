# kalkulator_fisika_streamlit.py
import streamlit as st
from PIL import Image
import math

st.set_page_config(page_title="Kalkulator Fisika", layout="centered")

menu = st.sidebar.radio("🔍 **Navigasi**", ("🏠 Dashboard", "🧮 Kalkulator", "❓ Kuis", "ℹ️ Tentang Aplikasi"))

# -----------------------------------
# DASHBOARD
# -----------------------------------
if menu == "🏠 Dashboard":
    st.title("Kalkulator Fisika 📊")
    st.markdown("""
    Selamat datang di aplikasi **Kalkulator Fisika Interaktif**! 🎉

    Aplikasi ini dirancang khusus untuk membantu siswa memahami konsep dasar fisika melalui kalkulasi, konversi satuan, dan kuis interaktif. Gunakan menu di samping untuk menavigasi fitur.
    """)

    try:
        image = Image.open("fisika.jpg")
        st.image(image, caption="Ilustrasi Fisika", use_column_width=False, width=500)
    except:
        st.warning("Gambar tidak ditemukan atau gagal dimuat.")

    st.markdown("""
    ### 🔧 Fitur Utama:
    - 📐 Kalkulator Kinematika & Dinamika
    - 🔁 Konversi Satuan
    - 🧠 Kuis Fisika Pilihan Ganda
    - 📘 Penjelasan Materi
    - 📩 Hubungi Kami
    """)

# -----------------------------------
# KALKULATOR
# -----------------------------------
elif menu == "🧮 Kalkulator":
    st.title("🧮 Kalkulator Fisika")
    tab1, tab2, tab3 = st.tabs(["Kinematika", "Dinamika", "Konversi Satuan"])

    # KINEMATIKA
    with tab1:
        st.header("📐 Kalkulator Kinematika")
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

    # DINAMIKA
    with tab2:
        st.header("⚙️ Kalkulator Dinamika")
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

    # KONVERSI SATUAN
    with tab3:
        st.header("📏 Konversi Satuan Fisika")
        jenis = st.selectbox("Jenis Konversi", ["Energi", "Tekanan", "Panjang", "Waktu"])

        satuan_dict = {
            "Energi": {"joule": 1, "kjoule": 1e3, "kalori": 4.184, "kwh": 3.6e6, "BTU": 1055},
            "Tekanan": {"pa": 1, "kpa": 1e3, "atm": 101325, "bar": 1e5, "mmhg": 133.322},
            "Panjang": {"meter": 1, "km": 1e3, "cm": 1e-2, "mm": 1e-3, "inch": 0.0254, "ft": 0.3048},
            "Waktu": {"detik": 1, "menit": 60, "jam": 3600, "hari": 86400},
        }

        val = st.number_input(f"Nilai {jenis}", step=0.1)
        from_unit = st.selectbox("Dari", satuan_dict[jenis].keys(), key="from_"+jenis)
        to_unit = st.selectbox("Ke", satuan_dict[jenis].keys(), key="to_"+jenis)

        if st.button("Konversi"):
            hasil = val * satuan_dict[jenis][from_unit] / satuan_dict[jenis][to_unit]
            st.success(f"Hasil: {hasil:.4f} {to_unit}")

# -----------------------------------
# KUIS
# -----------------------------------
elif menu == "❓ Kuis":
    st.title("🧠 Kuis Fisika - Pilihan Ganda")

    questions = [
        {
            "q": "Sebuah benda bermassa 10 kg diletakkan di atas permukaan datar. Gaya normalnya?",
            "options": ["10 N", "100 N", "9.8 N", "98 N"],
            "ans": 3
        },
        {
            "q": "Sebuah benda jatuh dari ketinggian 20 m. Waktu jatuhnya?",
            "options": ["2 s", "4 s", "3 s", "6 s"],
            "ans": 0
        },
        {
            "q": "Benda dilempar vertikal ke atas dengan v = 20 m/s. Waktu sampai titik tertinggi?",
            "options": ["1 s", "2 s", "3 s", "4 s"],
            "ans": 1
        }
    ]

    if "quiz_idx" not in st.session_state:
        st.session_state.quiz_idx = 0
        st.session_state.quiz_score = 0

    if st.session_state.quiz_idx < len(questions):
        q = questions[st.session_state.quiz_idx]
        st.subheader(f"Soal {st.session_state.quiz_idx + 1}")
        choice = st.radio(q["q"], q["options"], key=st.session_state.quiz_idx)
        if st.button("Kirim Jawaban"):
            if choice == q["options"][q["ans"]]:
                st.success("✅ Benar!")
                st.session_state.quiz_score += 1
            else:
                st.error(f"❌ Salah. Jawaban: {q['options'][q['ans']]}")
            st.session_state.quiz_idx += 1
            st.experimental_rerun()
    else:
        st.success(f"Kuis selesai! Skor: {st.session_state.quiz_score}/{len(questions)}")
        if st.button("Ulangi Kuis"):
            st.session_state.quiz_idx = 0
            st.session_state.quiz_score = 0
            st.experimental_rerun()

# -----------------------------------
# TENTANG APLIKASI
# -----------------------------------
else:
    st.title("📘 Tentang Aplikasi")
    st.markdown("""
    ### 🧪 Materi yang Tercakup
    - **Kinematika:** Percepatan, Kecepatan, Jarak, dan Waktu
    - **Dinamika:** Gaya, Tekanan, dan Energi Kinetik
    - **Konversi Satuan:** Panjang, Waktu, Tekanan, Energi

    ### 🧠 Tentang Kuis Fisika
    Kuis ini terdiri dari soal pilihan ganda berbasis konsep dasar fisika. Tujuannya untuk melatih pemahaman dan memperkuat konsep belajar.

    ### 📚 Cara Menggunakan Aplikasi
    1. Pilih menu fitur di sidebar kiri
    2. Masukkan nilai sesuai satuan yang diminta
    3. Klik tombol **Hitung** untuk melihat hasilnya
    4. Gunakan menu kuis untuk uji kemampuanmu!

    ### 📩 Hubungi Kami
    Silakan tinggalkan pesan Anda jika ada saran atau pertanyaan:
    """)
    email = st.text_input("Email Anda")
    pesan = st.text_area("Pesan Anda")
    if st.button("Kirim Pesan"):
        st.success("Pesan berhasil dikirim. Terima kasih telah menghubungi kami!")
