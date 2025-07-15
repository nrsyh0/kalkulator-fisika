# kalkulator_fisika_streamlit.py
# Jalankan: streamlit run kalkulator_fisika_streamlit.py
# ------------------------------------------------------
import streamlit as st
from PIL import Image

# ──────────────────────────────────────────────
# KONFIGURASI & CSS GLOBAL
# ──────────────────────────────────────────────
st.set_page_config(page_title="Kalkulator Fisika", layout="wide")

st.markdown("""
<style>
[data-testid=stSidebar] {background:#F0F2F6;}
.stButton>button{background:#0059ff;color:#fff;border:none;border-radius:6px;padding:0.5rem 1.25rem;}
.stButton>button:hover{background:#004be0;}
h2,h3,h4{color:#0059ff;}
footer{visibility:hidden;}
</style>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────────
# SIDEBAR
# ──────────────────────────────────────────────
st.sidebar.title("📑 Menu")
menu = st.sidebar.radio("", ("Dashboard", "Kalkulator", "Kuis", "Tentang"))

# ──────────────────────────────────────────────
# DASHBOARD
# ──────────────────────────────────────────────
if menu == "Dashboard":
    st.title("🏠 Dashboard")
    st.write("Selamat datang di **Kalkulator Fisika Web**!")

    col1, col2 = st.columns([1, 2])
    with col1:
        try:
            img = Image.open("fisika.jpg")
            st.image(img, caption="Ilustrasi Fisika", width=300)
        except Exception:
            st.warning("Gambar 'fisika.jpg' belum di‑upload.")
    with col2:
        st.markdown("""
        ### Fitur Aplikasi
        - **Kalkulator**: kinematika, dinamika, konversi  \n
        - **Kuis**: latihan soal fisika  \n
        - **Tentang**: info aplikasi
        """)
        st.info("Pilih fitur lewat sidebar di kiri.")

# ──────────────────────────────────────────────
# KALKULATOR
# ──────────────────────────────────────────────
elif menu == "Kalkulator":
    st.title("🧮 Kalkulator Fisika")
    tab1, tab2, tab3 = st.tabs(["📏 Kinematika", "⚙️ Dinamika", "🔄 Konversi"])

    # === KINEMATIKA ===
    with tab1:
        st.header("Kalkulator Kinematika")
        o = st.selectbox("Besaran:", ["Jarak (s)", "Kecepatan (v)", "Waktu (t)", "Percepatan (a)"], key="kin_sel")
        if o == "Jarak (s)":
            v = st.number_input("Kecepatan (m/s)", key="kin_v")
            t = st.number_input("Waktu (s)", key="kin_t")
            if st.button("Hitung", key="btn_s"):
                st.success(f"Jarak = {v*t:.2f} m")
        elif o == "Kecepatan (v)":
            s = st.number_input("Jarak (m)", key="kin_s2")
            t = st.number_input("Waktu (s)", key="kin_t2")
            if st.button("Hitung", key="btn_v") and t:
                st.success(f"Kecepatan = {s/t:.2f} m/s")
        elif o == "Waktu (t)":
            s = st.number_input("Jarak (m)", key="kin_s3")
            v = st.number_input("Kecepatan (m/s)", key="kin_v3")
            if st.button("Hitung", key="btn_t") and v:
                st.success(f"Waktu = {s/v:.2f} s")
        else:
            v1 = st.number_input("v₁ (m/s)", key="kin_v1")
            v2 = st.number_input("v₂ (m/s)", key="kin_v2")
            t  = st.number_input("Δt (s)", key="kin_t4")
            if st.button("Hitung", key="btn_a") and t:
                st.success(f"a = {(v2-v1)/t:.2f} m/s²")

    # === DINAMIKA ===
    with tab2:
        st.header("Kalkulator Dinamika")
        d = st.selectbox("Besaran:", ["Gaya (F)", "Tekanan (P)", "Energi Kinetik (Ek)"], key="dyn_sel")
        if d == "Gaya (F)":
            m = st.number_input("Massa (kg)", key="dyn_m")
            a = st.number_input("Percepatan (m/s²)", key="dyn_a")
            if st.button("Hitung", key="btn_f"):
                st.success(f"F = {m*a:.2f} N")
        elif d == "Tekanan (P)":
            F = st.number_input("Gaya (N)", key="dyn_F")
            A = st.number_input("Luas (m²)", key="dyn_A")
            if st.button("Hitung", key="btn_p") and A:
                st.success(f"P = {F/A:.2f} Pa")
        else:
            m = st.number_input("Massa (kg)", key="dyn_m2")
            v = st.number_input("Kecepatan (m/s)", key="dyn_v2")
            if st.button("Hitung", key="btn_ek"):
                st.success(f"Ek = {0.5*m*v**2:.2f} J")

    # === KONVERSI ===
    with tab3:
        st.header("Konversi Satuan")
        kat = st.selectbox("Kategori", ["Panjang","Massa","Waktu","Energi","Tekanan"], key="conv_kat")
        tbl = {
            "Panjang":{"m":1,"km":1000,"cm":1e-2,"mm":1e-3,"in":0.0254,"ft":0.3048},
            "Massa":{"kg":1,"g":1e-3,"mg":1e-6,"lb":0.453592},
            "Waktu":{"s":1,"min":60,"h":3600,"day":86400},
            "Energi":{"J":1,"kJ":1e3,"cal":4.184,"kWh":3.6e6},
            "Tekanan":{"Pa":1,"kPa":1e3,"bar":1e5,"atm":101325,"mmHg":133.322}
        }
        val = st.number_input("Nilai:", key="conv_val")
        f = st.selectbox("Dari", tbl[kat].keys(), key="conv_f")
        t = st.selectbox("Ke", tbl[kat].keys(), key="conv_t")
        if st.button("Konversi", key="btn_conv"):
            out = val * tbl[kat][f] / tbl[kat][t]
            st.success(f"Hasil: {out:.4f} {t}")

# ──────────────────────────────────────────────
# KUIS
# ──────────────────────────────────────────────
elif menu == "Kuis":
    st.title("❓ Kuis Fisika")
    qbank = [
        ("Satuan SI gaya adalah ...", ["Newton","Joule","Pascal","Watt"], 0),
        ("1 km = ... m", ["10","100","1 000","10 000"], 2),
        ("Rumus Ek?", ["mv","mv²","0.5mv²","2mv²"], 2),
        ("1 kWh = ... J", ["3600","3.6e6","1e6","1000"], 1),
        ("Tekanan = ...", ["F/A","F·A","A/F","m·a"], 0),
    ]

    if "q_idx" not in st.session_state:
        st.session_state.q_idx = 0
        st.session_state.q_scr = 0

    if st.session_state.q_idx < len(qbank):
        q, opt, ans = qbank[st.session_state.q_idx]
        st.subheader(f"Soal {st.session_state.q_idx+1}")
        choose = st.radio(q, opt, key=f"r{st.session_state.q_idx}")
        if st.button("Jawab", key=f"btn_q{st.session_state.q_idx}"):
            if choose == opt[ans]:
                st.success("Benar!")
                st.session_state.q_scr += 1
            else:
                st.error(f"Salah. Jawaban: {opt[ans]}")
            st.session_state.q_idx += 1
            st.experimental_rerun()
    else:
        st.success(f"Kuis selesai! Skor: {st.session_state.q_scr}/{len(qbank)}")
        if st.button("Ulangi", key="btn_qreset"):
            st.session_state.q_idx = 0
            st.session_state.q_scr = 0
            st.experimental_rerun()

# ──────────────────────────────────────────────
# TENTANG
# ──────────────────────────────────────────────
else:
    st.title("ℹ️ Tentang Aplikasi")
    st.markdown("""
    **Kalkulator Fisika Web** dibuat oleh **Aisyah**  
    untuk membantu belajar konsep fisika secara interaktif.

    **Fitur**
    - Kalkulator Kinematika & Dinamika  
    - Konversi Satuan  
    - Kuis Fisika  

    **Teknologi**: Python • Streamlit
    """)
