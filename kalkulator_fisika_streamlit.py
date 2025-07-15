# kalkulator_fisika_streamlit.py
import streamlit as st
from PIL import Image
import math

st.set_page_config(page_title="Kalkulator Fisika", layout="centered")

menu = st.sidebar.radio("Navigasi", ("Dashboard", "Kalkulator", "Kuis", "Tentang"))

# -----------------------------------
# DASHBOARD
# -----------------------------------
if menu == "Dashboard":
    st.title("\U0001F3E0 Dashboard")
    st.write("Selamat datang di **Kalkulator Fisika Web**!")

    try:
        image = Image.open("fisika.jpg")
        st.image(image, caption="Ilustrasi Fisika", use_column_width=True)
    except:
        st.warning("Gambar tidak ditemukan atau gagal dimuat.")

    st.markdown("""
    ### Fitur Aplikasi
    - **Kalkulator:** Hitung kinematika, dinamika, dan konversi satuan.
    - **Kuis:** Uji pemahaman dasar fisika.
    - **Tentang:** Informasi materi dan cara penggunaan.
    """)
    st.info("Gunakan menu di sidebar untuk membuka fitur.")

# -----------------------------------
# KALKULATOR
# -----------------------------------
elif menu == "Kalkulator":
    st.title("\U0001F9EE Kalkulator Fisika")
    tab1, tab2, tab3 = st.tabs(["Kinematika", "Dinamika", "Konversi Satuan"])

    # KINEMATIKA
    with tab1:
        st.header("Kalkulator Kinematika")
        kin_mode = st.selectbox("Pilih yang ingin dihitung:", ["Jarak (s)", "Kecepatan (v)", "Waktu (t)", "Percepatan (a)"])
        if kin_mode == "Jarak (s)":
            v = st.number_input("Kecepatan (m/s)", step=0.1)
            t = st.number_input("Waktu (s)", step=0.1)
            if st.button("Hitung", key="s"):
                st.success(f"Jarak = {v * t:.2f} meter")
        elif kin_mode == "Kecepatan (v)":
            s = st.number_input("Jarak (m)", step=0.1)
            t = st.number_input("Waktu (s)", step=0.1)
            if t != 0 and st.button("Hitung", key="v"):
                st.success(f"Kecepatan = {s / t:.2f} m/s")
        elif kin_mode == "Waktu (t)":
            s = st.number_input("Jarak (m)", step=0.1)
            v = st.number_input("Kecepatan (m/s)", step=0.1)
            if v != 0 and st.button("Hitung", key="t"):
                st.success(f"Waktu = {s / v:.2f} detik")
        elif kin_mode == "Percepatan (a)":
            v1 = st.number_input("Kecepatan awal v1 (m/s)", step=0.1)
            v2 = st.number_input("Kecepatan akhir v2 (m/s)", step=0.1)
            t = st.number_input("Waktu (s)", step=0.1)
            if t != 0 and st.button("Hitung", key="a"):
                st.success(f"Percepatan = {(v2 - v1) / t:.2f} m/s²")

    # DINAMIKA
    with tab2:
        st.header("Kalkulator Dinamika")
        dyn_mode = st.selectbox("Pilih yang ingin dihitung:", ["Gaya (F)", "Tekanan (P)", "Energi Kinetik (Ek)"])
        if dyn_mode == "Gaya (F)":
            m = st.number_input("Massa (kg)", step=0.1)
            a = st.number_input("Percepatan (m/s²)", step=0.1)
            if st.button("Hitung", key="F"):
                st.success(f"Gaya = {m * a:.2f} Newton")
        elif dyn_mode == "Tekanan (P)":
            F = st.number_input("Gaya (N)", step=0.1)
            A = st.number_input("Luas (m²)", step=0.01)
            if A != 0 and st.button("Hitung", key="P"):
                st.success(f"Tekanan = {F / A:.2f} Pascal")
        elif dyn_mode == "Energi Kinetik (Ek)":
            m = st.number_input("Massa (kg)", step=0.1)
            v = st.number_input("Kecepatan (m/s)", step=0.1)
            if st.button("Hitung", key="Ek"):
                st.success(f"Energi Kinetik = {0.5 * m * v**2:.2f} Joule")

    # KONVERSI
    with tab3:
        st.header("\U0001F4CF Konversi Satuan")
        jenis = st.selectbox("Jenis Konversi", ["Energi", "Tekanan", "Panjang", "Waktu"])

        satuan_dict = {
            "Energi": {"joule": 1, "kjoule": 1e3, "kalori": 4.184, "kwh": 3.6e6, "BTU": 1055},
            "Tekanan": {"pa": 1, "kpa": 1e3, "atm": 101325, "bar": 1e5, "mmhg": 133.322},
            "Panjang": {"meter": 1, "km": 1e3, "cm": 1e-2, "mm": 1e-3, "inch": 0.0254, "ft": 0.3048},
            "Waktu": {"detik": 1, "menit": 60, "jam": 3600, "hari": 86400},
        }

        val = st.number_input(f"Nilai {jenis}", step=0.1)
        satuan = satuan_dict[jenis]
        from_unit = st.selectbox("Dari", satuan.keys(), key=f"from_{jenis}")
        to_unit = st.selectbox("Ke", satuan.keys(), key=f"to_{jenis}")

        if st.button("Konversi", key=f"konversi_{jenis}"):
            hasil = val * satuan[from_unit] / satuan[to_unit]
            st.success(f"Hasil: {hasil:.4f} {to_unit}")

# -----------------------------------
# KUIS
# -----------------------------------
elif menu == "Kuis":
    st.title("❓ Kuis Fisika")

    questions = [
        {"q": "Sebuah benda bermassa 10 kg di lantai. Gaya normal?", "options": ["0 N", "10 N", "98 N", "100 N"], "ans": 2},
        {"q": "Benda 10 kg di bidang miring 53°. Gaya normal?", "options": ["0 N", "98 N", "59 N", "49 N"], "ans": 2},
        {"q": "Benda ditarik gaya 100 N, sudut 37°. Gaya normal?", "options": ["98 N", "80 N", "40 N", "50 N"], "ans": 1},
        {"q": "Benda ditarik gaya 100 N, sudut 37°. Percepatan?", "options": ["10 m/s²", "8 m/s²", "6 m/s²", "4 m/s²"], "ans": 1},
        {"q": "Benda 10 m/s, berhenti 20 s. Perlambatan?", "options": ["0.5", "1", "2", "0.25"], "ans": 1},
        {"q": "Jarak yang ditempuh benda sebelumnya?", "options": ["100 m", "200 m", "150 m", "250 m"], "ans": 0},
        {"q": "Benda jatuh dari 20 m. Waktu jatuh?", "options": ["1 s", "2 s", "3 s", "4 s"], "ans": 1},
        {"q": "Kecepatan saat menyentuh tanah?", "options": ["10", "20", "15", "5"], "ans": 1},
        {"q": "Benda dilempar 20 m/s ke atas. Waktu ke puncak?", "options": ["1 s", "2 s", "3 s", "4 s"], "ans": 1},
        {"q": "Tinggi maksimum lemparan?", "options": ["10", "20", "30", "40"], "ans": 3},
    ]

    if "quiz_idx" not in st.session_state:
        st.session_state.quiz_idx = 0
        st.session_state.quiz_score = 0

    if st.session_state.quiz_idx < len(questions):
        q = questions[st.session_state.quiz_idx]
        st.subheader(f"Soal {st.session_state.quiz_idx + 1}")
        choice = st.radio(q["q"], q["options"], key=st.session_state.quiz_idx)
        if st.button("Kirim Jawaban", key=f"btn_{st.session_state.quiz_idx}"):
            if choice == q["options"][q["ans"]]:
                st.success("✅ Benar!")
                st.session_state.quiz_score += 1
            else:
                st.error(f"❌ Salah. Jawaban yang benar: {q['options'][q['ans']]}")
            st.session_state.quiz_idx += 1
            st.experimental_rerun()
    else:
        st.success(f"🎉 Kuis selesai! Skor akhir: {st.session_state.quiz_score}/{len(questions)}")
        if st.button("🔁 Ulangi Kuis"):
            st.session_state.quiz_idx = 0
            st.session_state.quiz_score = 0
            st.experimental_rerun()

# -----------------------------------
# TENTANG
# -----------------------------------
else:
    st.title("ℹ️ Tentang Aplikasi")
    with st.expander("📌 Tentang Kinematika"):
        st.markdown("""
        Kinematika mempelajari gerak benda tanpa memperhatikan penyebabnya.
        - **Jarak:** total lintasan yang ditempuh.
        - **Kecepatan:** perubahan posisi terhadap waktu.
        - **Percepatan:** perubahan kecepatan tiap satuan waktu.
        """)
    with st.expander("📌 Tentang Dinamika"):
        st.markdown("""
        Dinamika mempelajari gaya dan gerak:
        - **Gaya (F = m × a)**: dorongan/tarikan pada benda.
        - **Tekanan (P = F / A)**: gaya per satuan luas.
        - **Energi Kinetik (Ek = 0.5 × m × v²)**: energi karena gerak.
        """)
    with st.expander("📌 Konversi Satuan"):
        st.markdown("""
        Konversi membantu mengganti satuan:
        - Energi: joule, kalori, kWh, dll.
        - Tekanan: Pa, atm, mmHg, bar
        - Panjang: meter, cm, km, inch
        - Waktu: detik, menit, jam
        """)
    with st.expander("📌 Tentang Kuis"):
        st.markdown("""
        Kuis berisi soal-soal fisika dasar seperti kinematika, gaya, percepatan, dan konversi satuan.
        Tujuannya untuk menguji dan memperkuat pemahaman konsep fisika.
        """)
    with st.expander("📌 Cara Menggunakan Aplikasi"):
        st.markdown("""
        1. Pilih menu kalkulator sesuai kebutuhan.
        2. Masukkan data numerik seperti massa, kecepatan, dll.
        3. Klik tombol "Hitung" untuk melihat hasil.
        4. Masuk ke Kuis untuk latihan soal.
        """)
    with st.expander("📬 Hubungi Kami"):
        st.text_input("Email Anda")
        st.text_area("Pesan Anda")
        if st.button("Kirim Pesan"):
            st.success("Terima kasih, pesan Anda telah dikirim!")
