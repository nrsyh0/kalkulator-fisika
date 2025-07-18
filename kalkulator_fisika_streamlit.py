import streamlit as st
from PIL import Image
import random

st.set_page_config(page_title="KalkuFisik", layout="wide")

st.markdown("""
    <style>
    .main {
        background-color: #FDF6EC;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
menu = st.sidebar.radio("🔍 **Navigasi**", ("🏠 Beranda", "🧮 Kalkulator", "❓ Kuis", "ℹ️ Tentang Aplikasi", "👨‍👩‍👧‍👦 Tentang Kami"))

if menu == "🏠 Beranda":
    st.title("🏠 Selamat Datang di Aplikasi Kalkulator & Kuis Fisika")
    st.image("fisika.jpg", use_container_width="centered")
    st.markdown("""
    ## 👋 Halo!
    Selamat datang di aplikasi interaktif untuk belajar Fisika dengan cara yang seru dan menyenangkan.
    
    Aplikasi ini dirancang khusus untuk membantu siswa ataupun mahasiswa memahami konsep dasar fisika melalui kalkulasi, konversi satuan, dan kuis interaktif. Pilih menu di sebelah kiri untuk mulai menggunakan kalkulator dan mencoba kuis.
    """)

elif menu == "🧮 Kalkulator":
    st.title("🧮 Kalkulator Fisika")
    tab1, tab2, tab3 = st.tabs(["Kinematika", "Dinamika", "Konversi Satuan"])

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
    with tab3:
        st.header("📏 Konversi Satuan Fisika")
        jenis = st.selectbox("Jenis Konversi", ["Energi", "Tekanan", "Panjang", "Waktu", "Volume", "Berat"])

        satuan_dict = {
            "Energi": {"joule": 1, "kjoule": 1e3, "kalori": 4.184, "kwh": 3.6e6, "BTU": 1055},
            "Tekanan": {"pa": 1, "kpa": 1e3, "atm": 101325, "bar": 1e5, "mmhg": 133.322},
            "Panjang": {"meter": 1, "km": 1e3, "cm": 1e-2, "mm": 1e-3, "inch": 0.0254, "ft": 0.3048},
            "Waktu": {"detik": 1, "menit": 60, "jam": 3600, "hari": 86400},
            "Volume": {"liter": 1, "ml": 1e-3, "m³": 1000},
            "Berat": {"gram": 1, "kg": 1000, "mg": 0.001},
        }

        val = st.number_input(f"Nilai {jenis}", step=0.1)
        from_unit = st.selectbox("Dari", satuan_dict[jenis].keys(), key="from_"+jenis)
        to_unit = st.selectbox("Ke", satuan_dict[jenis].keys(), key="to_"+jenis)

        if st.button("Konversi"):
            hasil = val * satuan_dict[jenis][from_unit] / satuan_dict[jenis][to_unit]
            st.success(f"Hasil: {hasil:.4f} {to_unit}")

# KUIS
# -----------------------------------
elif menu == "❓ Kuis":
    st.title("❓ Kuis Fisika Tambahan: Gerak dan Gaya")
    st.markdown("💡 **Petunjuk**: Gunakan Kalkulator Fisika untuk membantu menyelesaikan soal berikut.")

    questions = [
        {
            "q": "Soal 1: Kapal laut berlayar dengan kecepatan 15 m/s menempuh jarak 900 meter. Waktu yang dibutuhkan?",
            "options": ["A. 45 detik", "B. 50 detik", "C. 60 detik", "D. 75 detik"],
            "ans": 2,
            "explanation": "Waktu = Jarak / Kecepatan = 900 / 15 = 60 detik."
        },
        {
            "q": "Soal 2: Sepeda mulai dari 5 m/s dengan percepatan 2 m/s² selama 8 detik. Kecepatan akhirnya?",
            "options": ["A. 16 m/s", "B. 18 m/s", "C. 20 m/s", "D. 21 m/s"],
            "ans": 3,
            "explanation": "v = v₀ + a×t = 5 + (2×8) = 21 m/s."
        },
        {
            "q": "Soal 3: Mobil dari 10 m/s jadi 20 m/s dalam 5 detik. Jarak yang ditempuh?",
            "options": ["A. 75 m", "B. 80 m", "C. 85 m", "D. 90 m"],
            "ans": 0,
            "explanation": "s = ½(v₀ + v)t = ½(10+20)×5 = 75 m."
        },
        {
            "q": "Soal 4: Benda 20 kg didorong dengan gaya 100 N. Berapa percepatannya?",
            "options": ["A. 3 m/s²", "B. 4 m/s²", "C. 5 m/s²", "D. 6 m/s²"],
            "ans": 2,
            "explanation": "a = F / m = 100 / 20 = 5 m/s²."
        },
        {
            "q": "Soal 5: Bola 0,5 kg ditendang dengan percepatan 40 m/s². Gaya tendangan?",
            "options": ["A. 10 N", "B. 15 N", "C. 20 N", "D. 25 N"],
            "ans": 2,
            "explanation": "F = m × a = 0.5 × 40 = 20 N."
        },
    ]

    for idx, q in enumerate(questions):
        st.markdown(f"### {q['q']}")
        choice = st.radio("Pilih jawaban Anda:", q["options"], key=f"quiz{idx}")
        if st.button(f"Jawab Soal {idx+1}"):
            if choice == q["options"][q["ans"]]:
                st.success("✅ Jawaban Anda benar!")
            else:
                st.error(f"❌ Jawaban Anda salah. Jawaban benar: {q['options'][q['ans']]}")
            with st.expander("📘 Penjelasan"):
                st.markdown(q["explanation"])

elif menu == "ℹ️ Tentang Aplikasi":
    st.title("ℹ️ Tentang Aplikasi")
    st.markdown("""
    ## 🎯 Tujuan Aplikasi
    Aplikasi ini dirancang untuk membantu pelajar memahami konsep dasar Fisika melalui:
    - 💡 Kalkulator interaktif
    - 📝 Kuis pilihan ganda
    - 🔁 Konversi satuan fisika

    ## 📘 Materi Kalkulator
    **Kinematika:**
    - Menghitung jarak, kecepatan, waktu, dan percepatan.

    **Dinamika:**
    - Menghitung gaya, tekanan, dan energi kinetik.

    **Konversi:**
    - Panjang, waktu, energi, tekanan, berat, dan volume.

    ## ❓ Kuis Fisika
    Berisi soal-soal pilihan ganda tentang:
    - Gaya normal di bidang datar dan miring
    - Percepatan benda yang ditarik gaya
    - Kinematika (gerak vertikal, jatuh bebas)

    ## 🧾 Cara Penggunaan
    - Gunakan sidebar untuk berpindah antar fitur.
    - Isi nilai input, tekan tombol "Hitung".
    - Di kuis, pilih jawaban dan lihat hasilnya langsung.
    """)

elif menu == "👨‍👩‍👧‍👦 Tentang Kami":
    st.title("👨‍👩‍👧‍👦 Tentang Kami")

    st.markdown("""
    ### 📚 Kelompok 9 - Kelas 1D Analis Kimia

    Kami adalah mahasiswa dari **Politeknik AKA Bogor**, Program Studi **Analis Kimia**, kelas **1D**.  
    Aplikasi ini adalah hasil kolaborasi dalam proyek pembelajaran interaktif untuk mata kuliah Bahasa Inggrisg\-9 dan Fisika.

    ---
    #### 👥 Anggota Kelompok:
    """)

    st.markdown("""
    | Nama Lengkap                           | NIM       |
    |----------------------------------------|-----------|
    | 🧑‍🔬 Asyafarel Meldy Putra             | 2460334   |
    | 🎶 Gleen Fredly Manurung               | 2460379   |
    | 🌸 Nur Aisyah                          | 2460474   |
    | ✨ Vidya Fitriani Dwi Saputri          | 2460531   |
    | 💡 Muhammad Revan Fallaq               | 2460428   |
    """)

    st.markdown("""
    ---
    Kami berharap aplikasi ini membantu dalam memahami konsep dasar fisika melalui pendekatan interaktif yang seru dan mudah dipahami 😊
    """)
