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
if menu == "❓ Kuis":
    st.title("❓ Kuis Fisika Tambahan: Gerak dan Gaya")
    st.info("💡 Gunakan Kalkulator Fisika untuk membantu menjawab soal-soal berikut.")

    # Data soal
    questions = [
        {
            "q": "Sebuah kapal laut berlayar dengan kecepatan konstan 15 m/s. Jika kapal tersebut menempuh jarak 900 meter, Berapakah waktu yang dibutuhkan kapal tersebut (dalam detik)?",
            "options": ["A. 45 detik", "B. 50 detik", "C. 60 detik", "D. 75 detik"],
            "ans": 2,
            "explanation": "Waktu = Jarak / Kecepatan = 900 / 15 = 60 detik."
        },
        {
            "q": "Sebuah sepeda mulai bergerak dari kecepatan awal 5 m/s dan mengalami percepatan konstan 2 m/s² selama 8 detik. Berapakah kecepatan akhirnya?",
            "options": ["A. 16 m/s", "B. 18 m/s", "C. 20 m/s", "D. 21 m/s"],
            "ans": 3,
            "explanation": "v = v₀ + a.t = 5 + 2×8 = 21 m/s."
        },
        {
            "q": "Sebuah mobil bergerak dengan kecepatan awal 10 m/s. Setelah 5 detik, kecepatannya menjadi 20 m/s. Berapakah jarak yang ditempuh selama 5 detik itu?",
            "options": ["A. 75 m", "B. 80 m", "C. 85 m", "D. 90 m"],
            "ans": 0,
            "explanation": "S = ½(v₀ + v)t = ½(10+20)×5 = 75 m."
        },
        {
            "q": "Sebuah benda bermassa 20 kg didorong dengan gaya sebesar 100 N. Berapa percepatannya?",
            "options": ["A. 3 m/s²", "B. 4 m/s²", "C. 5 m/s²", "D. 6 m/s²"],
            "ans": 2,
            "explanation": "a = F/m = 100/20 = 5 m/s²."
        },
        {
            "q": "Seorang atlet menendang bola bermassa 0,5 kg sehingga bola tersebut bergerak dengan percepatan 40 m/s². Berapa besar gaya yang diberikan?",
            "options": ["A. 10 N", "B. 15 N", "C. 20 N", "D. 25 N"],
            "ans": 2,
            "explanation": "F = m.a = 0.5 × 40 = 20 N."
        },
    ]

    # Inisialisasi session state
    if 'quiz_index' not in st.session_state:
        st.session_state.quiz_index = 0
        st.session_state.score = 0
        st.session_state.show_result = False

    q = questions[st.session_state.quiz_index]

    st.markdown(f"### Soal {st.session_state.quiz_index + 1}:")
    st.markdown(q["q"])

    pilihan = st.radio("Pilih jawaban:", q["options"], key=st.session_state.quiz_index)

    if st.button("Jawab"):
        benar = q["options"][q["ans"]]
        if pilihan == benar:
            st.success(f"✅ Benar!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Salah. Jawaban benar: {benar}")

        with st.expander("📘 Penjelasan"):
            st.write(q["explanation"])

        st.session_state.show_result = True

    if st.session_state.show_result:
        if st.session_state.quiz_index < len(questions) - 1:
            if st.button("➡️ Soal Selanjutnya"):
                st.session_state.quiz_index += 1
                st.session_state.show_result = False
                st.experimental_rerun()
        else:
            st.success(f"🎉 Kuis selesai! Skor akhir kamu: {st.session_state.score} dari {len(questions)}")
            if st.button("🔁 Ulangi Kuis"):
                st.session_state.quiz_index = 0
                st.session_state.score = 0
                st.session_state.show_result = False
                st.experimental_rerun()

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
