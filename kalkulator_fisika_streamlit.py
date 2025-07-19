import streamlit as st

# Sidebar navigasi
menu = st.sidebar.radio("Navigasi", ["🏠 Dashboard", "🧮 Kalkulator Fisika", "🧠 Kuis Fisika", "ℹ️ Tentang Aplikasi", "👨‍👩‍👧‍👦 Tentang Kami"])

# ================= HALAMAN DASHBOARD ====================
if menu == "🏠 Dashboard":
    st.title("📊 Dashboard Aplikasi Fisika")
    st.markdown("Selamat datang di aplikasi kalkulator dan kuis fisika interaktif! Gunakan sidebar untuk mulai belajar.")

# ================= HALAMAN KALKULATOR ====================
elif menu == "🧮 Kalkulator Fisika":
    st.title("🧮 Kalkulator Fisika")
    st.markdown("(Fitur kalkulator bisa kamu tambahkan di sini)")

# ================= HALAMAN KUIS ====================
elif menu == "🧠 Kuis Fisika":
    st.title("🧠 Kuis Fisika Pilihan Ganda")
    st.markdown("Jawab pertanyaan di bawah ini satu per satu. Cek langsung penjelasan setelah menjawab! 🚀")

    questions = [
        {
            "q": "Sebuah benda diam kemudian bergerak dipercepat hingga kecepatannya 20 m/s dalam waktu 4 sekon. Berapa percepatan benda tersebut?",
            "options": ["5 m/s²", "10 m/s²", "20 m/s²", "2 m/s²"],
            "ans": 0,
            "explanation": "Gunakan rumus percepatan: a = (v2 - v1) / t = (20 - 0) / 4 = 5 m/s²"
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

    if "score" not in st.session_state:
        st.session_state.score = 0
    if "answered" not in st.session_state:
        st.session_state.answered = [False] * len(questions)

    for idx, q in enumerate(questions):
        st.markdown(f"### Soal {idx + 1}: {q['q']}")
        choice = st.radio("Pilih jawaban Anda:", q["options"], key=f"quiz{idx}")

        if st.button(f"Jawab Soal {idx + 1}", key=f"btn{idx}") and not st.session_state.answered[idx]:
            st.session_state.answered[idx] = True

            if choice == q["options"][q["ans"]]:
                st.success("✅ Jawaban Anda benar!")
                st.session_state.score += 1
            else:
                st.error(f"❌ Jawaban Anda salah. Jawaban benar: {q['options'][q['ans']]}")

            with st.expander("📘 Penjelasan"):
                st.markdown(q["explanation"])

    if all(st.session_state.answered):
        st.info(f"🏁 Kuis selesai! Skor akhir kamu: {st.session_state.score} dari {len(questions)}")

# ================= HALAMAN TENTANG APLIKASI ====================
elif menu == "ℹ️ Tentang Aplikasi":
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

    ### 🔍 Cara Menggunakan Aplikasi
    - Navigasikan menu di sidebar untuk memilih fitur.
    - Masukkan data sesuai kebutuhan di tiap kalkulator.
    - Klik tombol "Hitung" untuk melihat hasil perhitungan.
    - Gunakan halaman kuis untuk mencoba soal-soal fisika dasar.

    ---
    ### 📩 Hubungi Kami
    Silakan tinggalkan pesan Anda pada kolom berikut jika ada saran. 
    """)

    with st.form("hubungi"):
        email = st.text_input("Email Anda")
        pesan = st.text_area("Pesan Anda")
        submitted = st.form_submit_button("Kirim")
        if submitted:
            st.success("✅ Pesan berhasil dikirim!")

# ================= HALAMAN TENTANG KAMI ====================
elif menu == "👨‍👩‍👧‍👦 Tentang Kami":
    st.title("👨‍👩‍👧‍👦 Tentang Kami")

    st.markdown("""
    ### 📚 Kelompok 9 - Kelas 1D Analis Kimia

    Kami adalah mahasiswa dari **Politeknik AKA Bogor**, Program Studi **Analis Kimia**, kelas **1D**.  
    Aplikasi ini adalah hasil proyek pembelajaran interaktif untuk mata kuliah Logika dan Pemrograman Komputer.

    ---
    #### 👥 Anggota Kelompok:
    """)

    st.markdown("""
    | Nama Lengkap                           | NIM       |
    |----------------------------------------|-----------|
    | 🧑‍🔬 Asyafarel Meldy Putra               | 2460334   |
    | 🎶 Gleen Fredly Manurung               | 2460379   |
    | 💡 Muhammad Revan Fallaq               | 2460428   |
    | 🌸 Nur Aisyah                          | 2460474   |
    | ✨ Vidya Fitriani Dwi Saputri          | 2460531   |
    """)

    st.markdown("""
    ---
    Kami berharap aplikasi ini membantu dalam memahami konsep dasar fisika melalui pendekatan interaktif yang seru dan mudah dipahami 😊
    """)
