# kalkulator_fisika_streamlit.py
# Jalankan: streamlit run kalkulator_fisika_streamlit.py
# ------------------------------------------------------
import streamlit as st
from PIL import Image

# ──────────────────────────────────────────────────────
# KONFIGURASI HALAMAN
# ──────────────────────────────────────────────────────
st.set_page_config(page_title="Kalkulator Fisika", layout="wide")

# ──────────────────────────────────────────────────────
# CSS GLOBAL (sidebar, tombol, font, dll.)
# ──────────────────────────────────────────────────────
st.markdown("""
<style>
/* Sidebar */
[data-testid=stSidebar] {
    background-color: #F0F2F6;
}
/* Judul sidebar */
[data-testid=stSidebar] .css-ng1t4o {      /* Streamlit v1.32+ class */
    font-size: 1.25rem;
    font-weight: 700;
}
/* Tombol utama */
.stButton>button {
    background-color:#0059ff;
    color:white;
    border:none;
    padding:0.5rem 1.25rem;
    border-radius:6px;
}
.stButton>button:hover {
    background-color:#004be0;
}
/* Heading warna biru */
h2,h3,h4 { color:#0059ff; }
/* Hilangkan footer Streamlit default */
footer {visibility:hidden;}
</style>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────────────────
# SIDEBAR NAVIGASI
# ──────────────────────────────────────────────────────
st.sidebar.title("📑 Menu")
menu = st.sidebar.radio(
    "",
    ("Dashboard", "Kalkulator", "Kuis", "Tentang"),
    index=0,
    format_func=lambda x: f"🏠 {x}" if x=="Dashboard" else f"🧮 {x}" if x=="Kalkulator"
                          else f"❓ {x}" if x=="Kuis" else "ℹ️ Tentang")

# ──────────────────────────────────────────────────────
# DASHBOARD
# ──────────────────────────────────────────────────────
if menu == "Dashboard":
    st.title("🏠 Dashboard")

    col1, col2 = st.columns([1, 2])
    with col1:
        try:
            img = Image.open("fisika.jpg")   # ganti nama file jika berbeda
            st.image(img, caption="Ilustrasi Fisika", width=300)
        except Exception:
            st.warning("Gambar 'fisika.jpg' belum di‑upload.")
    with col2:
        st.markdown("""
        ### Fitur Aplikasi
        - **Kalkulator**: hitung kinematika, dinamika, konversi satuan  
        - **Kuis**: soal pilihan ganda fisika  
        - **Tentang**: info aplikasi & pengembang  
        """)
        st.info("Gunakan menu di sidebar untuk memilih fitur.")

# ──────────────────────────────────────────────────────
# KALKULATOR
# ──────────────────────────────────────────────────────
elif menu == "Kalkulator":
    st.title("🧮 Kalkulator Fisika")

    tab1, tab2, tab3 = st.tabs(["📏 Kinematika", "⚙️ Dinamika", "🔄 Konversi"])

    # === KINEMATIKA ===
    with tab1:
        st.header("Kalkulator Kinematika")
        opsi = st.selectbox("Besaran:", ["Jarak (s)", "Kecepatan (v)", "Waktu (t)", "Percepatan (a)"])
        if opsi == "Jarak (s)":
            v = st.number_input("Kecepatan (m/s)", step=0.1)
            t = st.number_input("Waktu (s)", step=0.1)
            if st.button("Hitung"):
                st.success(f"Jarak = {v*t:.2f} m")
        elif opsi == "Kecepatan (v)":
            s = st.number_input("Jarak (m)")
            t = st.number_input("Waktu (s)")
            if st.button("Hitung") and t:
                st.success(f"Kecepatan = {s/t:.2f} m/s")
        elif opsi == "Waktu (t)":
            s = st.number_input("Jarak (m)")
            v = st.number_input("Kecepatan (m/s)")
            if st.button("Hitung") and v:
                st.success(f"Waktu = {s/v:.2f} s")
        else:
            v1 = st.number_input("v₁ (m/s)")
            v2 = st.number_input("v₂ (m/s)")
            t  = st.number_input("Δt (s)")
            if st.button("Hitung") and t:
                st.success(f"Percepatan = {(v2-v1)/t:.2f} m/s²")

    # === DINAMIKA ===
    with tab2:
        st.header("Kalkulator Dinamika")
        opsi = st.selectbox("Besaran:", ["Gaya (F)", "Tekanan (P)", "Energi Kinetik (Ek)"])
        if opsi == "Gaya (F)":
            m = st.number_input("Massa (kg)")
            a = st.number_input("Percepatan (m/s²)")
            if st.button("Hitung"):
                st.success(f"Gaya = {m*a:.2f} N")
        elif opsi == "Tekanan (P)":
            F = st.number_input("Gaya (N)")
            A = st.number_input("Luas (m²)")
            if st.button("Hitung") and A:
                st.success(f"Tekanan = {F/A:.2f} Pa")
        else:
            m = st.number_input("Massa (kg)")
            v = st.number_input("Kecepatan (m/s)")
            if st.button("Hitung"):
                st.success(f"Ek = {0.5*m*v**2:.2f} J")

    # === KONVERSI ===
    with tab3:
        st.header("Konversi Satuan")
        kategori = st.selectbox("Kategori", ["Panjang", "Massa", "Waktu", "Energi", "Tekanan"])
        data = {
            "Panjang": {"m":1,"km":1e3,"cm":1e-2,"mm":1e-3,"in":0.0254,"ft":0.3048},
            "Massa":   {"kg":1,"g":1e-3,"mg":1e-6,"lb":0.453592},
            "Waktu":   {"s":1,"min":60,"h":3600,"day":86400},
            "Energi":  {"J":1,"kJ":1e3,"cal":4.184,"kWh":3.6e6},
            "Tekanan": {"Pa":1,"kPa":1e3,"bar":1e5,"atm":101325,"mmHg":133.322}
        }
        val = st.number_input("Nilai:")
        satuan_from = st.selectbox("Dari", data[kategori].keys())
        satuan_to   = st.selectbox("Ke",   data[kategori].keys())
        if st.button("Konversi"):
            out = val * data[kategori][satuan_from] / data[kategori][satuan_to]
            st.success(f"Hasil: {out:.4f} {satuan_to}")

# ──────────────────────────────────────────────────────
# KUIS
# ──────────────────────────────────────────────────────
elif menu == "Kuis":
    st.title("❓ Kuis Fisika")
    soal = [
        ("Satuan SI gaya adalah ...", ["Newton","Joule","Pascal","Watt"], 0),
        ("1 km = ... m", ["10","100","1 000","10 000"], 2),
        ("Rumus Ek?", ["mv","mv²","0.5mv²","2mv²"], 2),
        ("1 kWh = ... J", ["3600","3.6e6","1e6","1000"], 1),
        ("Tekanan = ...", ["F/A","F·A","A/F","m·a"], 0),
    ]  # tambah sampai 20 jika perlu

    if "idx" not in st.session_state:
        st.session_state.idx = 0
        st.session_state.score = 0

    if st.session_state.idx < len(soal):
        q, opts, ans = soal[st.session_state.idx]
        st.subheader(f"Soal {st.session_state.idx+1}")
        choice = st.radio(q, opts)
        if st.button("Kirim"):
            if choice == opts[ans]:
                st.success("Benar!")
                st.session_state.score += 1
            else:
                st.error(f"Salah. Jawaban: {opts[ans]}")
            st.session_state.idx += 1
            st.experimental_rerun()
    else:
        st.success(f"Kuis selesai! Skor: {st.session_state.score}/{len(soal)}")
        if st.button("Ulangi"):
            st.session_state.idx = 0
            st.session_state.score = 0
            st.experimental_rerun()

# ──────────────────────────────────────────────────────
# TENTANG
# ──────────────────────────────────────────────────────
else:
    st.title("ℹ️ Tentang Aplikasi")
    st.markdown("""
    **Kalkulator Fisika Web** dibuat oleh **Aisyah**  
    untuk membantu belajar konsep fisika melalui kalkulator & kuis interaktif.

    - **Teknologi**: Python • Streamlit  
    - **Lisensi** : MIT
    """)
