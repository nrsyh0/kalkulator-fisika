# kalkulator_fisika_streamlit.py
# Aplikasi Streamlit dengan halaman Dashboard, Kalkulator, Kuis, dan Tentang
# Jalankan: streamlit run kalkulator_fisika_streamlit.py
# ------------------------------------------------------
import streamlit as st

st.set_page_config(page_title="Kalkulator Fisika", layout="centered")

# Sidebar Navigation
menu = st.sidebar.radio("Navigasi", ("Dashboard", "Kalkulator", "Kuis", "Tentang"))

# ------------------------------------------------------
# DASHBOARD
# ------------------------------------------------------
if menu == "Dashboard":
    st.title("🏠 Dashboard")
    st.write("Selamat datang di **Kalkulator Fisika Web**!")
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
        st.header("Konversi Satuan Fisika")
        jenis = st.selectbox("Jenis yang ingin dikonversi:", ["Energi", "Tekanan"])

        val = st.number_input("Nilai yang ingin dikonversi:", step=0.1)

        energi_satuan = {"joule":1, "kjoule":1e3, "kwh":3.6e6, "kalori":4.184}
        tekanan_satuan = {"pa":1, "kpa":1e3, "bar":1e5, "atm":101325, "mmhg":133.322}

        if jenis == "Energi":
            satuan_from = st.selectbox("Dari:", list(energi_satuan.keys()), key="from_energy")
            satuan_to = st.selectbox("Ke:", list(energi_satuan.keys()), key="to_energy")
            faktor = energi_satuan
        else:
            satuan_from = st.selectbox("Dari:", list(tekanan_satuan.keys()), key="from_press")
            satuan_to = st.selectbox("Ke:", list(tekanan_satuan.keys()), key="to_press")
            faktor = tekanan_satuan

        if st.button("Konversi"):
            try:
                hasil = val * faktor[satuan_from] / faktor[satuan_to]
                st.success(f"Hasil: {hasil:.4f} {satuan_to}")
            except:
                st.error("Terjadi kesalahan dalam konversi.")

# ------------------------------------------------------
# KUIS
# ------------------------------------------------------
elif menu == "Kuis":
    st.title("❓ Kuis Fisika")

    # Daftar soal
    questions = [
        {
            "q": "Sebuah benda bergerak dengan kecepatan 2 m/s selama 5 detik. Berapa jarak yang ditempuh?",
            "options": ["2 m", "5 m", "10 m", "7,5 m"],
            "ans": 2,
        },
        {
            "q": "Jika massa 2 kg mengalami percepatan 3 m/s², berapa gaya (F) yang bekerja?",
            "options": ["6 N", "1,5 N", "5 N", "9 N"],
            "ans": 0,
        },
        {
            "q": "1 atm setara dengan berapa mmHg?",
            "options": ["76", "760", "101,325", "1"],
            "ans": 1,
        },
    ]

    # Inisialisasi session state
    if "quiz_started" not in st.session_state:
        st.session_state.quiz_started = False
        st.session_state.current_q = 0
        st.session_state.score = 0

    if not st.session_state.quiz_started:
        st.write("Klik tombol di bawah untuk memulai kuis 3 soal.")
        if st.button("Mulai Kuis"):
            st.session_state.quiz_started = True
            st.session_state.current_q = 0
            st.session_state.score = 0
    else:
        idx = st.session_state.current_q
        if idx < len(questions):
            q = questions[idx]
            st.subheader(f"Soal {idx + 1}")
            choice = st.radio(q["q"], q["options"], key=f"q{idx}")
            if st.button("Kirim Jawaban"):
                if choice == q["options"][q["ans"]]:
                    st.success("Benar! 😊")
                    st.session_state.score += 1
                else:
                    st.error(f"Salah. Jawaban yang benar: {q['options'][q['ans']]}")
                st.session_state.current_q += 1
                st.experimental_rerun()
        else:
            st.success(f"Kuis selesai! Skor akhir kamu: {st.session_state.score} / {len(questions)}")
            if st.button("Ulangi Kuis"):
                st.session_state.quiz_started = False
                st.session_state.current_q = 0
                st.session_state.score = 0

# ------------------------------------------------------
# TENTANG
# ------------------------------------------------------
else:  # menu == "Tentang"
    st.title("ℹ️ Tentang Aplikasi")
    st.markdown("""
    **Kalkulator Fisika Web** dibuat oleh **Aisyah** untuk memudahkan siswa mempelajari dan menghitung konsep dasar fisika.

    **Teknologi yang digunakan:**
    - Python 3
    - Streamlit

    **Lisensi**: MIT
    """)
    st.markdown("---")
    st.subheader("Cara Berkontribusi")
    st.write("Silakan fork repo di GitHub, lakukan perubahan, lalu buat pull request.")
