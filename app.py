
import streamlit as st
from datetime import datetime

# ------------------- ÜCRETLER -------------------
SES_SISTEMI = {
    "1": 2500,
    "2": 3500,
    "3": 1000  # palyaço
}
PALYACO_PAKET_1 = 3500
PALYACO_PAKET_2 = {"Adana": 1500, "Çevre": 2000, "Uzak": 3000}
DJ_UCRETI = {"Adana": 1500, "Çevre": 2000, "Uzak": 2500}
SANATCI = {"Adana": 2000, "Çevre": 2500, "Uzak": 3000}
SUNUCU = {"Adana": 2000, "Çevre": 2500, "Uzak": 3000}
ARAC = 2000
YEMEK_KISI_BASI = 350

SEMAZENLER = {
    "Adana": 1000, "Maraş": 1700, "Niğde": 1700, "Osmaniye": 1500, "Tarsus": 1300, "Mersin": 1500,
    "Hatay": 1700, "Aksaray": 1900, "Nevşehir": 1900, "Karaisalı": 1300, "Hozan": 1500,
    "Ceyhan": 1300, "İmamoğlu": 1300, "Malatya": 2500, "Elbistan": 1900
}

st.title("🎤 İsra Organizasyon Otomatik Teklif Hesaplayıcı")
st.write("Aşağıdan etkinlik bilgilerini girin. Sistem sizin için toplam fiyatı hesaplasın.")

etkinlik = st.selectbox("Etkinlik Türü", ["İlahi Grubu", "Semazen Ekibi", "Palyaço", "Mehter"])
sehir = st.selectbox("Etkinlik Yeri", list(SEMAZENLER.keys()))
semazen_sayisi = st.slider("Semazen Sayısı", 0, 3, 0)
palyaço_paketi = st.radio("Palyaço Paketi Var mı?", ["Yok", "Paket 1", "Paket 2"])
ses_sistemi = st.radio("Ses Sistemi Türü", ["1", "2", "Yok"])
dj_var = st.checkbox("DJ Gerekli mi?")
katilimci_sayisi = st.number_input("Toplam Kişi (araç+yemek hesaplanır)", min_value=1, max_value=20, value=5)
tarih = st.date_input("Etkinlik Tarihi", value=datetime.now())

if st.button("💰 Teklifi Hesapla"):
    toplam = 0
    bolge = "Adana" if sehir == "Adana" else ("Çevre" if sehir in SEMAZENLER else "Uzak")
    toplam += SUNUCU[bolge] + SANATCI[bolge]
    toplam += semazen_sayisi * SEMAZENLER.get(sehir, 1500)
    if ses_sistemi in SES_SISTEMI:
        toplam += SES_SISTEMI[ses_sistemi]
    if palyaço_paketi == "Paket 1":
        toplam += PALYACO_PAKET_1
    elif palyaço_paketi == "Paket 2":
        toplam += PALYACO_PAKET_2[bolge]
    if dj_var:
        toplam += DJ_UCRETI[bolge]
    toplam += ARAC
    toplam += katilimci_sayisi * YEMEK_KISI_BASI
    kar = toplam * 0.2
    genel_toplam = toplam + kar

    st.subheader("📄 Teklif Özeti")
    st.write(f"""
- **Yer:** {sehir}
- **Etkinlik Türü:** {etkinlik}
- **Semazen Sayısı:** {semazen_sayisi}
- **DJ:** {"Var" if dj_var else "Yok"}
- **Palyaço Paketi:** {palyaço_paketi}
- **Ses Sistemi:** {ses_sistemi if ses_sistemi != "Yok" else "Yok"}
- **Yemek + Araç Dahil**

### ✅ Toplam (KDV Hariç): {genel_toplam:.2f} TL

📌 Kapora için IBAN:
**TR80 0001 0009 3070 3253 8850 03**
Ziraat Bankası Yusuf Koçak
""")

