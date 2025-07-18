# kalkulator_fisika_streamlit.py
import streamlit as st
from PIL import Image
import math

st.set_page_config(page_title="Kalkulator Fisika", layout="centered")

menu = st.sidebar.radio("🔍 **Navigasi**", ("🏠 Beranda", "🧮 Kalkulator", "❓ Kuis", "ℹ️ Tentang Aplikasi"))

# -----------------------------------
# BERANDA
# -----------------------------------
if menu == "🏠 Beranda":
    st.title("Kalkulator Fisika 📊")
    st.markdown("""
    Selamat datang di aplikasi Kalkulator Fisika! 

    Aplikasi ini dirancang khusus untuk membantu siswa ataupun mahasiswa memahami konsep dasar fisika melalui kalkulasi, konversi satuan, dan kuis interaktif. Gunakan menu di samping untuk menavigasi fitur.
    """)
    try:
        image = Image.open("fisika.jpg")  # Pastikan file ini ada di folder yang sama
        st.image(image, caption="Ilustrasi Fisika", width=350)  # Gunakan width agar proporsional
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
    st.title("❓ Kuis Fisika Tambahan: Gerak dan Gaya")
    st.write("Gunakan Kalkulator Fisika untuk membantu menjawab!")

    # Soal dan jawaban
    questions = [
        {
            "q": "Soal 1: Sebuah kapal laut berlayar dengan kecepatan konstan 15 m/s. Jika kapal tersebut menempuh jarak 900 meter, berapakah waktu yang dibutuhkan kapal tersebut (dalam detik)?",
            "options": ["A. 45 detik", "B. 50 detik", "C. 60 detik", "D. 75 detik"],
            "ans": 2,
            "penjelasan": "Waktu = Jarak / Kecepatan = 900 / 15 = 60 detik"
        },
        {
            "q": "Soal 2: Sebuah sepeda mulai bergerak dari kecepatan awal 5 m/s dan mengalami percepatan 2 m/s² selama 8 detik. Berapakah kecepatan akhirnya?",
            "options": ["A. 16 m/s", "B. 18 m/s", "C. 20 m/s", "D. 21 m/s"],
            "ans": 3,
            "penjelasan": "v = vo + a × t = 5 + (2 × 8) = 21 m/s"
        },
        {
            "q": "Soal 3: Sebuah mobil dari 10 m/s menjadi 20 m/s selama 5 detik. Jarak yang ditempuh?",
            "options": ["A. 75 m", "B. 80 m", "C. 85 m", "D. 90 m"],
            "ans": 0,
            "penjelasan": "s = ½ (vo + vt) × t = ½ (10 + 20) × 5 = 75 m"
        },
        {
            "q": "Soal 4: Sebuah benda 20 kg didorong dengan gaya 100 N. Percepatannya?",
            "options": ["A. 3 m/s²", "B. 4 m/s²", "C. 5 m/s²", "D. 6 m/s²"],
            "ans": 2,
            "penjelasan": "a = F / m = 100 / 20 = 5 m/s²"
        },
        {
            "q": "Soal 5: Bola 0.5 kg ditendang dan mengalami percepatan 40 m/s². Gaya tendangan?",
            "options": ["A. 10 N", "B. 15 N", "C. 20 N", "D. 25 N"],
            "ans": 2,
            "penjelasan": "F = m × a = 0.5 × 40 = 20 N"
        }
    ]

    if 'quiz_index' not in st.session_state:
        st.session_state.quiz_index = 0
        st.session_state.score = 0
        st.session_state.answers = []

    q = questions[st.session_state.quiz_index]
    st.markdown(f"### {q['q']}")
    selected = st.radio("Pilih jawaban Anda:", q["options"], key=f"quiz_q{st.session_state.quiz_index}")

    if st.button("Jawab"):
        benar = (selected == q["options"][q["ans"]])
        st.session_state.answers.append({
            "soal": q["q"],
            "jawaban": selected,
            "benar": benar,
            "penjelasan": q["penjelasan"],
            "kunci": q["options"][q["ans"]]
        })

        if benar:
            st.success("✅ Jawaban Benar!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Salah. Jawaban benar: {q['options'][q['ans']]}")

        st.info(f"📘 Penjelasan: {q['penjelasan']}")

        # Tombol untuk lanjut
        if st.session_state.quiz_index + 1 < len(questions):
            if st.button("➡️ Lanjut ke Soal Berikutnya"):
                st.session_state.quiz_index += 1
                st.experimental_rerun()
        else:
            st.markdown("---")
            st.success(f"🎉 Kuis selesai! Nilai kamu: {st.session_state.score} / {len(questions)}")
            st.markdown("### 📖 Ringkasan Jawaban dan Pembahasan:")
            for i, a in enumerate(st.session_state.answers):
                st.markdown(f"**Soal {i+1}**")
                st.write(a["soal"])
                st.write(f"✅ Jawaban kamu: {a['jawaban']}")
                if not a["benar"]:
                    st.write(f"📌 Jawaban benar: {a['kunci']}")
                st.write(f"📘 Penjelasan: {a['penjelasan']}")
                st.markdown("---")

            # Reset untuk coba lagi
            if st.button("🔁 Coba Lagi"):
                del st.session_state.quiz_index
                del st.session_state.score
                del st.session_state.answers
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
