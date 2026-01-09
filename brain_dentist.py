import streamlit as st

# Dictionary FAQ Dokter Gigi
faq_dokter_gigi = {
    "berapa kali harus sikat gigi": "Disarankan untuk menyikat gigi minimal 2 kali sehari, yaitu setelah sarapan dan sebelum tidur. Menyikat gigi yang benar memakan waktu sekitar 2-3 menit.",
    
    "kapan harus ke dokter gigi": "Disarankan untuk melakukan pemeriksaan rutin ke dokter gigi setiap 6 bulan sekali. Namun, jika ada keluhan seperti sakit gigi, gusi berdarah, atau masalah lainnya, segera kunjungi dokter gigi.",
    
    "bagaimana cara mencegah gigi berlubang": "Untuk mencegah gigi berlubang, sikat gigi 2 kali sehari dengan pasta gigi berfluoride, kurangi konsumsi makanan manis dan lengket, gunakan benang gigi (dental floss), dan lakukan pemeriksaan rutin ke dokter gigi.",
    
    "apa itu scaling": "Scaling adalah prosedur pembersihan karang gigi (tartar) yang menempel pada permukaan gigi dan di bawah garis gusi. Prosedur ini dilakukan untuk mencegah penyakit gusi dan kerusakan gigi.",
    
    "berapa biaya scaling": "Biaya scaling bervariasi tergantung klinik dan jumlah rahang. Umumnya untuk 1 rahang sekitar Rp 250.000 - Rp 400.000, dan untuk 2 rahang sekitar Rp 450.000 - Rp 700.000. Pelajar biasanya mendapat diskon.",
    
    "apa penyebab gigi sensitif": "Gigi sensitif dapat disebabkan oleh email gigi yang terkikis, gusi yang turun (resesi), gigi berlubang, atau penggunaan pasta gigi yang terlalu abrasif. Konsultasikan dengan dokter gigi untuk penanganan yang tepat.",
    
    "bagaimana cara merawat gigi anak": "Untuk anak-anak, ajarkan menyikat gigi sejak gigi pertama muncul. Gunakan sikat gigi khusus anak dan pasta gigi berfluoride sesuai usia. Batasi konsumsi permen dan minuman manis, serta ajak anak untuk rutin ke dokter gigi.",
    
    "apa itu gigi bungsu": "Gigi bungsu (wisdom tooth) adalah gigi geraham ketiga yang biasanya tumbuh pada usia 17-25 tahun. Gigi ini sering menimbulkan masalah karena tidak ada ruang yang cukup, sehingga perlu dicabut.",
    
    "kapan harus cabut gigi bungsu": "Gigi bungsu perlu dicabut jika menyebabkan nyeri, infeksi, merusak gigi lain, atau tumbuh tidak normal. Konsultasikan dengan dokter gigi untuk evaluasi yang tepat.",
    
    "apa itu kawat gigi": "Kawat gigi (behel) adalah alat ortodontik yang digunakan untuk merapikan posisi gigi dan memperbaiki susunan gigi yang tidak rapi. Pemasangan kawat gigi membutuhkan waktu 1-3 tahun tergantung kasus."
}


def cari_jawaban(pertanyaan_user):
    """
    Mencari jawaban berdasarkan kata kunci dari pertanyaan user.
    
    Args:
        pertanyaan_user (str): Pertanyaan yang diajukan user
    
    Returns:
        str: Jawaban yang sesuai atau pesan jika tidak ditemukan
    """
    pertanyaan_user = pertanyaan_user.lower().strip()
    
    # Kata-kata umum yang tidak spesifik (untuk diabaikan dalam perhitungan)
    kata_umum = {"apa", "itu", "adalah", "bagaimana", "berapa", "kapan", "dimana", "kenapa", "mengapa"}
    
    # Cek exact match dulu (paling akurat)
    if pertanyaan_user in faq_dokter_gigi:
        return faq_dokter_gigi[pertanyaan_user]
    
    # Cari yang paling cocok berdasarkan jumlah kata yang cocok
    best_match = None
    max_kata_cocok = 0
    
    kata_kunci_user = set(pertanyaan_user.split()) - kata_umum  # Hapus kata umum
    
    for pertanyaan, jawaban in faq_dokter_gigi.items():
        kata_kunci_pertanyaan = set(pertanyaan.split()) - kata_umum  # Hapus kata umum
        
        # Hitung kata yang cocok (tidak termasuk kata umum)
        kata_cocok = kata_kunci_pertanyaan.intersection(kata_kunci_user)
        jumlah_cocok = len(kata_cocok)
        
        # Prioritaskan yang memiliki lebih banyak kata cocok
        if jumlah_cocok > max_kata_cocok and jumlah_cocok >= 1:
            max_kata_cocok = jumlah_cocok
            best_match = jawaban
    
    if best_match:
        return best_match
    
    # Jika tidak ditemukan, cek kata kunci umum
    kata_kunci_umum = {
        "kawat gigi": "Kawat gigi (behel) adalah alat ortodontik yang digunakan untuk merapikan posisi gigi dan memperbaiki susunan gigi yang tidak rapi. Pemasangan kawat gigi membutuhkan waktu 1-3 tahun tergantung kasus.",
        "behel": "Kawat gigi (behel) adalah alat ortodontik yang digunakan untuk merapikan posisi gigi dan memperbaiki susunan gigi yang tidak rapi. Pemasangan kawat gigi membutuhkan waktu 1-3 tahun tergantung kasus.",
        "scaling": "Scaling adalah prosedur pembersihan karang gigi. Biaya scaling untuk 1 rahang sekitar Rp 250.000 dan 2 rahang sekitar Rp 450.000.",
        "sikat gigi": "Sikat gigi minimal 2 kali sehari setelah makan dan sebelum tidur. Gunakan pasta gigi berfluoride dan sikat selama 2-3 menit.",
        "gigi berlubang": "Gigi berlubang dapat dicegah dengan menyikat gigi rutin, mengurangi makanan manis, dan pemeriksaan rutin ke dokter gigi.",
        "gigi sensitif": "Gigi sensitif dapat disebabkan oleh email yang terkikis atau gusi yang turun. Konsultasikan dengan dokter gigi untuk penanganan yang tepat.",
        "dokter gigi": "Disarankan untuk melakukan pemeriksaan rutin ke dokter gigi setiap 6 bulan sekali.",
        "biaya": "Biaya perawatan gigi bervariasi. Untuk scaling, 1 rahang sekitar Rp 250.000 dan 2 rahang sekitar Rp 450.000. Pelajar mendapat diskon 25%.",
    }
    
    for kata, jawaban in kata_kunci_umum.items():
        if kata in pertanyaan_user:
            return jawaban
    
    return None


# ====== Konfigurasi Halaman ======
st.set_page_config(
    page_title="Chatbot FAQ Dokter Gigi - M. Arif Aulia",
    page_icon="🦷",
    layout="centered"
)

# ====== Custom CSS ======
st.markdown(
    """
    <style>
    /* Background gradient */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        color: #f5f5f5;
        font-family: "Segoe UI", system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Main container */
    .chatbot-card {
        background: rgba(15, 17, 32, 0.95);
        border-radius: 24px;
        padding: 32px 36px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        margin-bottom: 24px;
    }

    .title-text {
        font-size: 2.5rem;
        font-weight: 800;
        letter-spacing: 0.02em;
        text-align: center;
        margin-bottom: 0.3rem;
        background: linear-gradient(135deg, #ffffff 0%, #e0e7ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .subtitle-text {
        font-size: 1.05rem;
        text-align: center;
        color: #d0d4ff;
        margin-bottom: 2rem;
        opacity: 0.9;
    }

    /* Chat message styling */
    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 16px 20px;
        border-radius: 18px 18px 4px 18px;
        margin: 12px 0;
        color: white;
        font-weight: 500;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        max-width: 85%;
        margin-left: auto;
        margin-right: 0;
    }

    .bot-message {
        background: rgba(34, 197, 94, 0.15);
        border: 1px solid rgba(34, 197, 94, 0.3);
        padding: 18px 22px;
        border-radius: 18px 18px 18px 4px;
        margin: 12px 0;
        color: #bbf7d0;
        font-weight: 500;
        max-width: 85%;
        margin-left: 0;
        margin-right: auto;
        line-height: 1.6;
    }

    .error-message {
        background: rgba(239, 68, 68, 0.15);
        border: 1px solid rgba(239, 68, 68, 0.3);
        padding: 18px 22px;
        border-radius: 18px;
        margin: 12px 0;
        color: #fecaca;
        font-weight: 500;
        max-width: 85%;
    }

    /* Input styling */
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.1) !important;
        border: 2px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 12px !important;
        color: white !important;
        padding: 12px 16px !important;
        font-size: 1rem !important;
    }

    .stTextInput > div > div > input:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.2) !important;
    }

    .stTextInput > div > div > input::placeholder {
        color: rgba(255, 255, 255, 0.5) !important;
    }

    /* Button styling */
    div.stButton > button {
        width: 100%;
        border-radius: 12px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        font-weight: 700;
        font-size: 1rem;
        letter-spacing: 0.03em;
        padding: 14px 24px;
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
        transition: all 0.2s ease;
    }

    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 28px rgba(102, 126, 234, 0.5);
    }

    div.stButton > button:active {
        transform: translateY(0);
    }

    /* Info box */
    .info-box {
        background: rgba(59, 130, 246, 0.15);
        border: 1px solid rgba(59, 130, 246, 0.3);
        border-radius: 12px;
        padding: 16px 20px;
        margin: 16px 0;
        color: #bfdbfe;
        font-size: 0.9rem;
        line-height: 1.6;
    }

    /* FAQ list */
    .faq-item {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        padding: 12px 16px;
        margin: 8px 0;
        border-left: 3px solid #667eea;
        transition: all 0.2s ease;
    }

    .faq-item:hover {
        background: rgba(255, 255, 255, 0.08);
        transform: translateX(4px);
    }

    /* Footer */
    .footer-text {
        text-align: center;
        margin-top: 2rem;
        font-size: 0.9rem;
        color: rgba(255, 255, 255, 0.7);
        opacity: 0.8;
    }

    /* Scrollbar styling */
    .stApp::-webkit-scrollbar {
        width: 8px;
    }

    .stApp::-webkit-scrollbar-track {
        background: rgba(0, 0, 0, 0.1);
    }

    .stApp::-webkit-scrollbar-thumb {
        background: rgba(102, 126, 234, 0.5);
        border-radius: 4px;
    }

    .stApp::-webkit-scrollbar-thumb:hover {
        background: rgba(102, 126, 234, 0.7);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ====== Header ======
st.markdown('<div class="title-text">🦷 Chatbot FAQ Dokter Gigi</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">Website oleh <b>M. Arif Aulia</b> | Tanyakan apapun tentang kesehatan gigi</div>', unsafe_allow_html=True)

# ====== Inisialisasi Session State ======
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "show_faq_list" not in st.session_state:
    st.session_state.show_faq_list = False

# ====== Main Container ======
container = st.container()
with container:
    st.markdown('<div class="chatbot-card">', unsafe_allow_html=True)

    # Info box
    st.markdown(
        '<div class="info-box">💡 <b>Tips:</b> Ketik pertanyaan Anda di bawah, atau klik tombol "Lihat Daftar Pertanyaan" untuk melihat pertanyaan yang tersedia.</div>',
        unsafe_allow_html=True
    )

    # Tampilkan chat history
    if st.session_state.chat_history:
        st.markdown("### 💬 Riwayat Percakapan")
        for item in st.session_state.chat_history:
            if item["type"] == "user":
                st.markdown(f'<div class="user-message">👤 <b>Anda:</b><br>{item["content"]}</div>', unsafe_allow_html=True)
            elif item["type"] == "bot":
                st.markdown(f'<div class="bot-message">🦷 <b>Chatbot:</b><br>{item["content"]}</div>', unsafe_allow_html=True)
            elif item["type"] == "error":
                st.markdown(f'<div class="error-message">❌ {item["content"]}</div>', unsafe_allow_html=True)

    # Input form
    st.markdown("---")
    pertanyaan_user = st.text_input(
        "💬 Masukkan pertanyaan Anda:",
        placeholder="Contoh: Berapa kali harus sikat gigi?",
        key="input_pertanyaan"
    )

    col1, col2 = st.columns([2, 1])
    
    with col1:
        if st.button("🔍 Cari Jawaban", use_container_width=True):
            if pertanyaan_user.strip():
                pertanyaan_user_lower = pertanyaan_user.lower().strip()
                
                # Cek perintah khusus
                if pertanyaan_user_lower in ['daftar', 'list', 'help', 'pertanyaan']:
                    st.session_state.show_faq_list = not st.session_state.show_faq_list
                    st.session_state.chat_history.append({
                        "type": "user",
                        "content": pertanyaan_user
                    })
                else:
                    # Cari jawaban
                    jawaban = cari_jawaban(pertanyaan_user)
                    
                    # Simpan ke history
                    st.session_state.chat_history.append({
                        "type": "user",
                        "content": pertanyaan_user
                    })
                    
                    if jawaban:
                        st.session_state.chat_history.append({
                            "type": "bot",
                            "content": jawaban
                        })
                    else:
                        st.session_state.chat_history.append({
                            "type": "error",
                            "content": "Maaf, saya belum memiliki jawaban untuk pertanyaan tersebut. Silakan coba pertanyaan lain atau lihat daftar pertanyaan yang tersedia."
                        })
                
                st.rerun()
            else:
                st.warning("⚠️ Silakan masukkan pertanyaan terlebih dahulu!")
    
    with col2:
        if st.button("📋 Daftar Pertanyaan", use_container_width=True):
            st.session_state.show_faq_list = not st.session_state.show_faq_list
            st.rerun()

    # Tampilkan daftar FAQ
    if st.session_state.show_faq_list:
        st.markdown("---")
        st.markdown("### 📋 Daftar Pertanyaan yang Tersedia:")
        for idx, pertanyaan in enumerate(faq_dokter_gigi.keys(), 1):
            st.markdown(
                f'<div class="faq-item">{idx}. {pertanyaan.capitalize()}</div>',
                unsafe_allow_html=True
            )

    st.markdown("</div>", unsafe_allow_html=True)

# ====== Footer ======
st.markdown('<div class="footer-text">Terima kasih sudah berkunjung!  | Jaga kesehatan gigi Anda! 🦷</div>', unsafe_allow_html=True)
