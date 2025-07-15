# kalkulator_fisika_streamlit.py
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Kalkulator Fisika", layout="centered")

menu = st.sidebar.radio("Navigasi", ("Dashboard", "Kalkulator", "Kuis", "Tentang"))

# -----------------------------------
# DASHBOARD
# -----------------------------------
if menu == "Dashboard":
    st.title("🏠 Dashboard")
    st.write("Selamat datang di **Kalkulator Fisika Web**!")

    try:
        image = Image.open("fisika.jpg")  # Pastikan file ini ada di folder yang sama
        st.image(image, use_column_width=300)
    except:
        st.warning("Gambar tidak ditemukan atau gagal dimuat.")

    st.markdown("""
    ### Fitur Aplikasi
    - **Kalkulator:** Hitung kinematika, dinamika, dan konversi satuan.
    - **Kuis:** Uji pemahaman dasar fisika.
    - **Tentang:** Informasi mengenai aplikasi dan pembuatnya.
    """)
    st.info("Gunakan menu di sidebar untuk membuka fitur.")


# -----------------------------------
# KALKULATOR
# -----------------------------------
elif menu == "Kalkulator":
    st.title("🧮 Kalkulator Fisika")
    tab1, tab2, tab3 = st.tabs(["Kinematika", "Dinamika", "Konversi Satuan"])

    # KINEMATIKA
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

    # DINAMIKA
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

    # KONVERSI SATUAN
    with tab3:
        st.header("📏 Konversi Satuan Fisika")
        jenis = st.selectbox("Jenis Konversi", ["Energi", "Tekanan", "Panjang", "Waktu"])

        if jenis == "Energi":
            val = st.number_input("Nilai Energi", step=0.1)
            satuan = {
                "joule": 1,
                "kjoule": 1e3,
                "kalori": 4.184,
                "kwh": 3.6e6,
                "BTU": 1055
            }
        elif jenis == "Tekanan":
            val = st.number_input("Nilai Tekanan", step=0.1)
            satuan = {
                "pa": 1,
                "kpa": 1e3,
                "atm": 101325,
                "bar": 1e5,
                "mmhg": 133.322
            }
        elif jenis == "Panjang":
            val = st.number_input("Nilai Panjang", step=0.1)
            satuan = {
                "meter": 1,
                "km": 1e3,
                "cm": 1e-2,
                "mm": 1e-3,
                "inch": 0.0254,
                "ft": 0.3048
            }
        else:
            val = st.number_input("Nilai Waktu", step=0.1)
            satuan = {
                "detik": 1,
                "menit": 60,
                "jam": 3600,
                "hari": 86400
            }

        from_unit = st.selectbox("Dari", satuan.keys())
        to_unit = st.selectbox("Ke", satuan.keys())

        if st.button("Konversi"):
            hasil = val * satuan[from_unit] / satuan[to_unit]
            st.success(f"Hasil: {hasil:.4f} {to_unit}")

# -----------------------------------
# KUIS
# -----------------------------------
elif menu == "Kuis":
    st.title("❓ Kuis Fisika")

    questions = [
        {
            "q": "Sebuah benda bergerak 2 m/s selama 5 detik. Jarak?",
            "options": ["2 m", "5 m", "10 m", "7,5 m"],
            "ans": 2
        },
        {
            "q": "Massa 2 kg, percepatan 3 m/s². Gaya?",
            "options": ["6 N", "1,5 N", "5 N", "9 N"],
            "ans": 0
        },
        {
            "q": "1 atm berapa mmHg?",
            "options": ["76", "760", "101325", "1"],
            "ans": 1
        },
        {
            "q": "1 km = ... meter?",
            "options": ["10", "100", "1000", "10000"],
            "ans": 2
        },
        {
            "q": "Kecepatan = ...?",
            "options": ["Jarak x Waktu", "Jarak / Waktu", "Waktu / Jarak", "Gaya x Massa"],
            "ans": 1
        },
        {
            "q": "Energi Kinetik = ...?",
            "options": ["mv", "0.5mv²", "ma", "mv²"],
            "ans": 1
        },
        {
            "q": "1 kWh = ... joule?",
            "options": ["3600", "3.6e6", "1000", "36000"],
            "ans": 1
        },
        {
            "q": "Satuan SI gaya?",
            "options": ["Joule", "Watt", "Pascal", "Newton"],
            "ans": 3
        },
        {
            "q": "1 kaki = ... meter?",
            "options": ["0.3048", "0.3", "1.0", "2.54"],
            "ans": 0
        },
        {
            "q": "1 jam = ... detik?",
            "options": ["3600", "60", "1800", "1000"],
            "ans": 0
        },
    ]

    if "quiz_idx" not in st.session_state:
        st.session_state.quiz_idx = 0
        st.session_state.quiz_score = 0

    if st.session_state.quiz_idx < len(questions):
        q = questions[st.session_state.quiz_idx]
        st.subheader(f"Soal {st.session_state.quiz_idx + 1}")
        choice = st.radio(q["q"], q["options"])
        if st.button("Kirim Jawaban"):
            if choice == q["options"][q["ans"]]:
                st.success("Benar!")
                st.session_state.quiz_score += 1
            else:
                st.error(f"Salah. Jawaban: {q['options'][q['ans']]}")
            st.session_state.quiz_idx += 1
            st.experimental_rerun()
    else:
        st.success(f"Kuis selesai! Skor: {st.session_state.quiz_score}/{len(questions)}")
        if st.button("Ulangi"):
            st.session_state.quiz_idx = 0
            st.session_state.quiz_score = 0
            st.experimental_rerun()

# -----------------------------------
# TENTANG
# -----------------------------------
else:
    st.title("ℹ️ Tentang Aplikasi")
    st.markdown("""
    **Kalkulator Fisika Web** dibuat oleh **Aisyah** untuk membantu pelajar memahami konsep dasar fisika secara interaktif.

    **Fitur:**
    - Perhitungan Kinematika, Dinamika
    - Konversi Satuan
    - Kuis Fisika Interaktif

    **Teknologi:**
    - Python
    - Streamlit
    """)
