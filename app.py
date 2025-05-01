import streamlit as st
from datetime import datetime

# ------------------- KAR/İŞARET ORANI -------------------
MARKUP_RATE = 0.25
MARKUP = 1 + MARKUP_RATE

# ------------------- MALİYET SÖZLÜKLERİ -------------------
SEMAZEN_COSTS = {
    "Adana": 1000, "Maraş": 1700, "Niğde": 1700, "Osmaniye": 1500,
    "Tarsus": 1300, "Mersin": 1500, "Hatay": 1700, "Aksaray": 1900,
    "Nevşehir": 1900, "Malatya": 2500
}
DJ_COSTS = {"Adana": 1500, "Cevre": 2000, "Uzak": 2500}
PALYAÇO_PAKET1 = 3500
PALYAÇO_PAKET2 = {"Adana":1500, "Cevre":2000, "Uzak":3000}
SES1_BASE = 2500
SES2_BASE = 3500

# ------------------- YER SEÇİMİ -------------------
st.title("🎤 İsra Organizasyon Otomatik Teklif Hesaplayıcı")
sehir = st.selectbox("Etkinlik Yeri", list(SEMAZEN_COSTS.keys()))

# Bölge tespiti (DJ ve Palyaço 2 için)
if sehir == "Adana":
    region = "Adana"
elif sehir in SEMAZEN_COSTS and sehir != "Adana":
    region = "Cevre"
else:
    region = "Uzak"

# ------------------- DİNAMİK MALIYETLER -------------------
sem_cost = SEMAZEN_COSTS[sehir]
sunucu_cost = int((sem_cost * 2) * MARKUP)
sanatci_cost = int((sem_cost * 1.5) * MARKUP)
dj_cost     = int((DJ_COSTS[region]) * MARKUP)
ses1_cost   = int(SES1_BASE * MARKUP)
ses2_cost   = int(SES2_BASE * MARKUP)

# ------------------- ONAY KUTULARI (ÖNCE FİYATI GÖSTER) -------------------
# Sabit seçilenler
st.checkbox(f"✅ 1 Sunucu ({sunucu_cost} TL)", value=True, disabled=True)
st.checkbox(f"✅ 1 Sanatçı ({sanatci_cost} TL)", value=True, disabled=True)
st.checkbox(f"✅ 1 DJ ({dj_cost} TL)", value=True, disabled=True)

# İlahi Grubu Paket 1 altı
st.markdown("**Semazen Seçenekleri:**")
sem1 = st.checkbox(f"1 Semazen ({int(sem_cost*MARKUP):.0f} TL)")
sem2 = st.checkbox(f"2 Semazen ({int(sem_cost*2*MARKUP):.0f} TL)")
sem3 = st.checkbox(f"3 Semazen ({int(sem_cost*3*MARKUP):.0f} TL)")
sem4 = st.checkbox(f"4 Semazen ({int(sem_cost*4*MARKUP):.0f} TL)")

# Ses sistemleri
st.markdown("**Ses Sistemi Seçimi:**")
ss1 = st.checkbox(f"Ses Sistemi 1 ({ses1_cost} TL)")
ss2 = st.checkbox(f"Ses Sistemi 2 ({ses2_cost} TL)")

# Palyaço paketleri
pal1 = st.checkbox(f"Palyaço Paketi 1 ({int(PALYAÇO_PAKET1*MARKUP)} TL)")
pal2 = st.checkbox(f"Palyaço Paketi 2 ({int(PALYAÇO_PAKET2[region]*MARKUP)} TL)")

# Mehter
st.markdown("**Mehter Paketleri:**")
meh8  = st.checkbox(f"8 Kişilik Mehter ({int(sem_cost*1.75*8*MARKUP):.0f} TL kişi başı)")
meh12 = st.checkbox(f"12 Kişilik Mehter ({int(sem_cost*1.75*12*MARKUP):.0f} TL kişi başı)")
meh18 = st.checkbox(f"18 Kişilik Mehter ({int(sem_cost*1.75*18*MARKUP):.0f} TL kişi başı)")
meh24 = st.checkbox(f"24 Kişilik Mehter ({int(sem_cost*1.75*24*MARKUP):.0f} TL kişi başı)")
meh30 = st.checkbox(f"30 Kişilik Mehter ({int(sem_cost*1.75*30*MARKUP):.0f} TL kişi başı)")
meh32 = st.checkbox(f"32 Kişilik Mehter ({int(sem_cost*1.75*32*MARKUP):.0f} TL kişi başı)")

# ------------------- HESAPLA BUTONU -------------------
if st.button("💰 Teklifi Hesapla"):
    toplam = 0
    # Sunucu + Sanatçı + DJ
    toplam += sunucu_cost + sanatci_cost + dj_cost
    # Semazenler
    toplam += (1 if sem1 else 0 + 2 if sem2 else 0 + 3 if sem3 else 0 + 4 if sem4 else 0) * int(sem_cost*MARKUP)
    # Ses sistemi
    toplam += (ses1_cost if ss1 else 0) + (ses2_cost if ss2 else 0)
    # Palyaço
    toplam += (int(PALYAÇO_PAKET1*MARKUP) if pal1 else 0) + (int(PALYAÇO_PAKET2[region]*MARKUP) if pal2 else 0)
    # Mehter
    for cnt, sel in [(8,meh8),(12,meh12),(18,meh18),(24,meh24),(30,meh30),(32,meh32)]:
        if sel:
            toplam += cnt * int(sem_cost*1.75*MARKUP)
    st.subheader(f"✅ Genel Toplam: {toplam:.0f} TL + KDV")
