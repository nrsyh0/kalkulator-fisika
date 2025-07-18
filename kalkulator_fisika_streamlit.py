# kalkulator_fisika_streamlit.py
import streamlit as st
from PIL import Image
import math

st.set_page_config(page_title="Kalkulator Fisika", layout="centered")
st.markdown("""
    <style>
    .block-container {
        padding-top: 2rem;
    }
    .stRadio > div > label {
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

menu = st.sidebar.radio("🔍 **Navigasi**", ("🏠 Beranda", "🧮 Kalkulator", "❓ Kuis", "ℹ️ Tentang Aplikasi"))

# -----------------------------------
# BERANDA
# -----------------------------------
if menu == "🏠 Beranda":
    st.title("📊 Kalkulator Fisika")
    st.markdown("""
    Selamat datang di aplikasi Kalkulator Fisika! 🎓⚙️

    Aplikasi ini membantu siswa dan mahasiswa memahami konsep dasar fisika melalui kalkulasi, konversi satuan, dan kuis interaktif.
    """)
    try:
        image = Image.open("fisika.jpg")
        st.image(image, caption="Ilustrasi Fisika", width=300)
    except:
        st.warning("Gambar tidak ditemukan atau gagal dimuat.")

    st.markdown("""
    ### 🔧 Fitur Utama:
    - 📐 **Kalkulator Kinematika & Dinamika**
    - 🔁 **Konversi Satuan**
    - 🧠 **Kuis Fisika Interaktif**
    - 📘 **Penjelasan Materi Fisika**
    - 📩 **Hubungi Kami**
    """)

# -----------------------------------
# KALKULATOR
# -----------------------------------
elif menu == "🧮 Kalkulator":
    st.title("🧮 Kalkulator Fisika")
    tab1, tab2, tab3 = st.tabs(["📐 Kinematika", "⚙️ Dinamika", "📏 Konversi Satuan"])

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
if menu == "Kuis":
    st.title("❓ Kuis Fisika Interaktif")

    questions = [
        {
            "q": "Sebuah benda bermassa 10 kg diletakkan di atas lantai datar. Berapakah gaya normalnya?",
            "options": ["0 N", "10 N", "98 N", "100 N"],
            "ans": 2,
            "explanation": "Gaya normal pada bidang datar = berat = m × g = 10 × 9.8 = 98 N"
        },
        {
            "q": "Sebuah benda bergerak dengan kecepatan awal 10 m/s selama 20 detik hingga berhenti. Perlambatannya?",
            "options": ["0.5 m/s²", "1 m/s²", "2 m/s²", "0.25 m/s²"],
            "ans": 0,
            "explanation": "a = (v_t - v_0) / t = (0 - 10) / 20 = -0.5 m/s²"
        },
        {
            "q": "Benda dijatuhkan dari ketinggian 20 meter. Waktu jatuhnya?",
            "options": ["1 s", "2 s", "3 s", "4 s"],
            "ans": 1,
            "explanation": "t = √(2h/g) = √(40/10) = √4 = 2 s"
        },
        {
            "q": "Benda dilempar vertikal ke atas dengan kecepatan 20 m/s. Waktu ke titik tertinggi?",
            "options": ["1 s", "2 s", "3 s", "4 s"],
            "ans": 1,
            "explanation": "t = v/g = 20/10 = 2 s"
        },
    ]

    if "quiz_index" not in st.session_state:
        st.session_state.quiz_index = 0
        st.session_state.score = 0
        st.session_state.next_clicked = False

    q = questions[st.session_state.quiz_index]

    st.subheader(f"Soal {st.session_state.quiz_index + 1}")
    pilihan = st.radio(q["q"], q["options"], key=st.session_state.quiz_index)

    if not st.session_state.next_clicked:
        if st.button("Jawab"):
            jawaban_benar = q["options"][q["ans"]]
            if pilihan == jawaban_benar:
                st.success("✅ Benar!")
                st.session_state.score += 1
            else:
                st.error(f"❌ Salah. Jawaban benar: {jawaban_benar}")
            with st.expander("📘 Penjelasan"):
                st.write(q["explanation"])
            st.session_state.next_clicked = True

    if st.session_state.next_clicked:
        if st.session_state.quiz_index < len(questions) - 1:
            if st.button("➡️ Soal Selanjutnya"):
                st.session_state.quiz_index += 1
                st.session_state.next_clicked = False
        else:
            st.success(f"🎉 Kuis selesai! Skor kamu: {st.session_state.score} dari {len(questions)}")
            if st.button("🔁 Ulangi Kuis"):
                st.session_state.quiz_index = 0
                st.session_state.score = 0
                st.session_state.next_clicked = False

# -----------------------------------
# TENTANG
# -----------------------------------
else:
    st.title("ℹ️ Tentang Aplikasi")
    st.markdown("""
    ### 🎓 Tujuan Aplikasi
    Membantu pelajar memahami dan menghitung konsep fisika secara **interaktif** dan **visual**.

    ---
    ### 🔍 Materi KALKULATOR

    #### Kinematika
    - **Jarak (s)**: s = v × t
    - **Kecepatan (v)**: v = s / t
    - **Waktu (t)**: t = s / v
    - **Percepatan (a)**: a = (v2 - v1) / t

    #### Dinamika
    - **Gaya (F)**: F = m × a
    - **Tekanan (P)**: P = F / A
    - **Energi Kinetik**: Ek = 0.5 × m × v²

    #### Konversi Satuan
    - Energi (Joule, Kalori, kWh, dll)
    - Tekanan (Pa, atm, mmHg, dll)
    - Panjang (meter, km, inch, dll)
    - Waktu (detik, menit, jam, hari)

    ---
    ### ❓ Tentang Kuis
    Berisi **soal pilihan ganda** dari materi kinematika, dinamika, dan konversi satuan. Cocok untuk latihan mandiri.

    ---
    ### 🛠️ Cara Menggunakan
    1. Pilih menu di **sidebar kiri**.
    2. Gunakan **Kalkulator** sesuai topik.
    3. Ikuti **Kuis** untuk menguji pemahamanmu.

    ---
    ### 📩 Hubungi Kami
    Silakan tinggalkan pesan Anda pada kolom berikut.
    """)

    with st.form("hubungi"):
        email = st.text_input("Email Anda")
        pesan = st.text_area("Pesan Anda")
        submitted = st.form_submit_button("Kirim")
        if submitted:
            st.success("✅ Pesan berhasil dikirim!")
