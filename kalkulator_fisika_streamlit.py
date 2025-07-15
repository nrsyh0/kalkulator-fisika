# kalkulator_fisika_streamlit.py
# Jalankan: streamlit run kalkulator_fisika_streamlit.py
# -----------------------------------------------
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Kalkulator Fisika", layout="centered")

# ───────────────────────────────────────────────
# Sidebar ‑ navigasi
menu = st.sidebar.radio("Navigasi", ("Dashboard", "Kalkulator", "Kuis", "Tentang"))

# ───────────────────────────────────────────────
# DASHBOARD
# ───────────────────────────────────────────────
if menu == "Dashboard":
    st.title("🏠 Dashboard")
    st.write("Selamat datang di **Kalkulator Fisika Web**!")

    # tampilkan ilustrasi (upload gambar ini ke repo)
    try:
        img = Image.open("59789c64-09f8-4cb1-993c-df6bc87810fd.jpg")
        st.image(img, caption="Ilustrasi Fisika", use_column_width=True)
    except Exception:
        st.warning("Gambar ilustrasi belum tersedia.")

    st.markdown("""
    ### Fitur Aplikasi
    - **Kalkulator:** Hitung kinematika, dinamika, dan konversi satuan.
    - **Kuis:** Uji pemahaman dasar fisika.
    - **Tentang:** Info aplikasi & pembuat.
    """)
    st.info("Pilih fitur lewat sidebar di kiri.")

# ───────────────────────────────────────────────
# KALKULATOR
# ───────────────────────────────────────────────
elif menu == "Kalkulator":
    st.title("🧮 Kalkulator Fisika")
    tab1, tab2, tab3 = st.tabs(["Kinematika", "Dinamika", "Konversi Satuan"])

    # ===== KINEMATIKA =====
    with tab1:
        st.header("Kalkulator Kinematika")
        opsi = st.selectbox("Besaran yang ingin dihitung:",
                            ["Jarak (s)", "Kecepatan (v)", "Waktu (t)", "Percepatan (a)"])

        if opsi == "Jarak (s)":
            v = st.number_input("Kecepatan (m/s)", step=0.1)
            t = st.number_input("Waktu (s)", step=0.1)
            if st.button("Hitung Jarak"):
                st.success(f"Jarak = {v * t:.2f} m")

        elif opsi == "Kecepatan (v)":
            s = st.number_input("Jarak (m)", step=0.1)
            t = st.number_input("Waktu (s)", step=0.1)
            if t and st.button("Hitung Kecepatan"):
                st.success(f"Kecepatan = {s / t:.2f} m/s")

        elif opsi == "Waktu (t)":
            s = st.number_input("Jarak (m)", step=0.1)
            v = st.number_input("Kecepatan (m/s)", step=0.1)
            if v and st.button("Hitung Waktu"):
                st.success(f"Waktu = {s / v:.2f} s")

        elif opsi == "Percepatan (a)":
            v1 = st.number_input("Kecepatan awal v1 (m/s)", step=0.1)
            v2 = st.number_input("Kecepatan akhir v2 (m/s)", step=0.1)
            t  = st.number_input("Waktu (s)", step=0.1)
            if t and st.button("Hitung Percepatan"):
                st.success(f"Percepatan = {(v2 - v1) / t:.2f} m/s²")

    # ===== DINAMIKA =====
    with tab2:
        st.header("Kalkulator Dinamika")
        opsi = st.selectbox("Besaran yang ingin dihitung:",
                            ["Gaya (F)", "Tekanan (P)", "Energi Kinetik (Ek)"])

        if opsi == "Gaya (F)":
            m = st.number_input("Massa (kg)", step=0.1)
            a = st.number_input("Percepatan (m/s²)", step=0.1)
            if st.button("Hitung Gaya"):
                st.success(f"Gaya = {m * a:.2f} N")

        elif opsi == "Tekanan (P)":
            F = st.number_input("Gaya (N)", step=0.1)
            A = st.number_input("Luas (m²)", step=0.0001, format="%.4f")
            if A and st.button("Hitung Tekanan"):
                st.success(f"Tekanan = {F / A:.2f} Pa")

        elif opsi == "Energi Kinetik (Ek)":
            m = st.number_input("Massa (kg)", step=0.1)
            v = st.number_input("Kecepatan (m/s)", step=0.1)
            if st.button("Hitung Energi Kinetik"):
                st.success(f"Energi Kinetik = {0.5 * m * v**2:.2f} J")

    # ===== KONVERSI SATUAN (INTERAKTIF) =====
    with tab3:
        st.header("Konversi Satuan Interaktif")

        kategori = st.selectbox("Kategori:", ["Panjang", "Massa", "Waktu",
                                              "Tekanan", "Energi"])
        satuan = {
            "Panjang": {"m":1, "km":1e3, "cm":1e-2, "mm":1e-3,
                        "μm":1e-6, "nm":1e-9, "in":0.0254, "ft":0.3048},
            "Massa":   {"kg":1, "g":1e-3, "mg":1e-6, "lb":0.453592},
            "Waktu":   {"s":1, "min":60, "h":3600, "day":86400},
            "Tekanan": {"Pa":1, "kPa":1e3, "bar":1e5,
                        "atm":101325, "mmHg":133.322},
            "Energi":  {"J":1, "kJ":1e3, "cal":4.1868, "kWh":3.6e6}
        }

        nilai = st.number_input("Nilai:", step=0.1)
        satuan_dari = st.selectbox("Dari:", list(satuan[kategori].keys()))
        satuan_ke   = st.selectbox("Ke:",   list(satuan[kategori].keys()))

        if st.button("Konversi"):
            hasil = nilai * satuan[kategori][satuan_dari] / satuan[kategori][satuan_ke]
            st.success(f"Hasil: {hasil:.4f} {satuan_ke}")

# ───────────────────────────────────────────────
# KUIS
# ───────────────────────────────────────────────
elif menu == "Kuis":
    st.title("❓ Kuis Fisika")

    questions = [
        {
            "q": "Sebuah benda bergerak 2 m/s selama 5 s. Berapa jarak yang ditempuh?",
            "ops": ["2 m", "5 m", "10 m", "7,5 m"],
            "ans": 2
        },
        {
            "q": "Jika massa 2 kg mengalami percepatan 3 m/s², berapa gaya F?",
            "ops": ["6 N", "1,5 N", "5 N", "9 N"],
            "ans": 0
        },
        {
            "q": "1 atm setara dengan berapa mmHg?",
            "ops": ["76", "760", "101 325", "1"],
            "ans": 1
        }
    ]

    if "idx" not in st.session_state:
        st.session_state.idx = 0
        st.session_state.score = 0

    idx = st.session_state.idx
    if idx < len(questions):
        q = questions[idx]
        st.subheader(f"Soal {idx+1}")
        pilihan = st.radio(q["q"], q["ops"])
        if st.button("Kirim Jawaban"):
            if pilihan == q["ops"][q["ans"]]:
                st.success("Benar! 🎉")
                st.session_state.score += 1
            else:
                st.error(f"Salah. Jawaban benar: {q['ops'][q['ans']]}")
            st.session_state.idx += 1
            st.experimental_rerun()
    else:
        st.success(f"Kuis selesai! Skor: {st.session_state.score}/{len(questions)}")
        if st.button("Ulangi Kuis"):
            st.session_state.idx = 0
            st.session_state.score = 0
            st.experimental_rerun()

# ───────────────────────────────────────────────
# TENTANG
# ───────────────────────────────────────────────
else:
    st.title("ℹ️ Tentang Aplikasi")
    st.markdown("""
    **Kalkulator Fisika Web** dibuat oleh **Aisyah**  
    untuk membantu belajar dan menghitung konsep dasar fisika.

    **Teknologi:** Python · Streamlit  
    **Lisensi:** MIT
    """)
    st.markdown("---")
    st.subheader("Kontribusi")
    st.write("Silakan fork repo GitHub‑nya, lakukan perubahan, lalu pull request.")
