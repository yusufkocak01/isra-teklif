import streamlit as st
from datetime import datetime

# -----------------------------------
# 💰 İşaret Oranı
MARKUP = 1.25  # %25 kar

# -----------------------------------
# 📋 Sabit Maliyetler
SEMAZENLER = {
    "Adana": 1000, "Seyhan": 1000, "Yüreğir": 1000, "Çukurova": 1000, "Sarıçam": 1000,
    "Ceyhan": 1300, "Karataş": 1350, "İmamoğlu": 1300, "Kozan": 1500, "Karaisalı": 1300,
    "Pozantı": 1700, "Aladağ": 1700, "Tufanbeyli": 1700, "Saimbeyli": 1700, "Feke": 1700,
    "Antakya": 1700, "İskenderun": 1700, "Reyhanlı": 1700, "Kırıkhan": 1700, "Dörtyol": 1700,
    "Erzin": 1700, "Belen": 1700, "Samandağ": 1700, "Altınözü": 1700, "Hassa": 1700,
    "Payas": 1700, "Yayladağı": 1700,
    "Merkez (Onikişubat)": 1700, "Dulkadiroğlu": 1700, "Elbistan": 1900, "Afşin": 1900,
    "Türkoğlu": 1700, "Pazarcık": 1900, "Andırın": 1900, "Göksun": 1900, "Ekinözü": 1900,
    "Nurhak": 1900,
    "Şahinbey": 1700, "Şehitkamil": 1700, "Nizip": 1900, "Araban": 1900, "Karkamış": 1900,
    "Yavuzeli": 1900, "Oğuzeli": 1900, "Islahiye": 1700, "Nurdağı": 1700,
    "Merkez": 1900,  # Kilis
    "Kadirli": 1700, "Düziçi": 1700, "Bahçe": 1700, "Hasanbeyli": 1700,
    "Toprakkale": 1700, "Sumbas": 1700,
    "Bor": 1700, "Ulukışla": 1700, "Çamardı": 1700, "Altunhisar": 1700, "Çiftlik": 1700,
    "Ortaköy": 1900, "Eskil": 1900, "Gülağaç": 1900, "Güzelyurt": 1900,
    "Sarıyahşi": 1900, "Ağaçören": 1900
}
DJ_COSTS    = {"Adana":1500, "Cevre":2000, "Uzak":2500}
PALYAÇO_1   = 3500
PALYAÇO_2   = {"Adana":1500, "Cevre":2000, "Uzak":3000}
SES1_COST   = 2500
SES2_COST   = 3500

# -----------------------------------
# 📱 Arayüz
st.title("🎤 İsra Organizasyon Teklif Hesaplayıcı")
st.markdown("### 📍 Konum Seçimi (şehir + ilçe)")
# Şehir
sehir = st.checkbox("Adana", value=True, key="city_Adana") and "Adana" or None
# İlçeler
ilceler = [c for c in SEMAZENLER if c != "Adana"]
selected_ilce = None
for ilce in ilceler:
    if st.checkbox(f"  {ilce}", key=f"ilce_{ilce}"):
        selected_ilce = ilce
        break
location = selected_ilce or sehir

# Bölge türü
if location == "Adana":
    region = "Adana"
elif location in SEMAZENLER:
    region = "Cevre"
else:
    region = "Uzak"

# Temel maliyetler
sem_cost   = SEMAZENLER.get(location, 1000)
sunucu_cost   = int(sem_cost * 1.5 * MARKUP)
sanatci_cost  = int(sem_cost * 1.5 * MARKUP)
dj_cost       = int(DJ_COSTS[region] * MARKUP)
ses1_cost     = int(SES1_COST * MARKUP)
ses2_cost     = int(SES2_COST * MARKUP)

st.markdown("### ✅ Temel Ekipman ve Personel")
st.checkbox(f"✅ 1 Sunucu ({sunucu_cost} TL)", value=True, disabled=True)
st.checkbox(f"✅ 1 Sanatçı ({sanatci_cost} TL)", value=True, disabled=True)
st.checkbox(f"✅ 1 DJ ({dj_cost} TL)", value=True, disabled=True)

st.markdown("### 🎶 İlahi Grubu Paket (Semazen)")
s1 = st.checkbox(f"1 Semazen ({int(sem_cost*MARKUP)} TL)")
s2 = st.checkbox(f"2 Semazen ({int(sem_cost*2*MARKUP)} TL)")
s3 = st.checkbox(f"3 Semazen ({int(sem_cost*3*MARKUP)} TL)")
s4 = st.checkbox(f"4 Semazen ({int(sem_cost*4*MARKUP)} TL)")

st.markdown("### 🔊 Ses Sistemi")
st.checkbox(f"✅ Ses Sistemi 1 ({ses1_cost} TL): 4 Hoparlör, 1 Mikser, 1 Power, 1 Kablosuz Mikrofon", value=True, disabled=True)
st.checkbox(f"✅ Ses Sistemi 2 ({ses2_cost} TL): 4 Hoparlör, 1 Mikser, 1 Power, 1 Kanun Mikrofon, 1 Keman Mikrofon, 1 Ritm Saz Mikrofon, 1 Ney Mikrofon", value=True, disabled=True)

st.markdown("### 🤡 Palyaço Paketleri")
st.checkbox(f"Palyaço Paketi 1 ({int(PALYAÇO_1*MARKUP)} TL): 1 Palyaço, Ses Sistemi 3, Yüz Boyama, Balon Şekillendirme", key="pal1")
st.checkbox(f"Palyaço Paketi 2 ({int(PALYAÇO_2[region]*MARKUP)} TL): 2 Palyaço, 2 Hoparlör, 1 Mikser, 2 Kablosuz Mikrofon, Yüz Boyama, Balon, Çuval Yarışı, Halat Çekme, Evet–Hayır, Sandalye Kapmaca, Oyunlar", key="pal2")
st.checkbox(f"Palyaço Paketi 3 ({int(3500*MARKUP)} TL): 1 Palyaço, Yüz Boyama, Balon (Ses Ştsmz)", key="pal3")

st.markdown("### 🥁 Mehter Paketleri")
for cnt in [8,12,18,24,30,32]:
    per_cost = int(sem_cost * 1.75 * MARKUP)
    total = per_cost * cnt
    # araç maliyeti
    if location!="Adana":
        if cnt in (8,12,18): vehicle=15000
        elif cnt==24:    vehicle=20000
        else:            vehicle=30000
    else:
        vehicle=0
    st.checkbox(f"{cnt} Kişilik Mehter: {per_cost} TL/kişi (Toplam {total} TL) + Araç {vehicle} TL", key=f"meh{cnt}")

if st.button("💰 Teklifi Hesapla"):
    toplam=0
    toplam += sunucu_cost + sanatci_cost + dj_cost
    toplam += (1 if s1 else 0 + 2 if s2 else 0 + 3 if s3 else 0 + 4 if s4 else 0) * int(sem_cost*MARKUP)
    toplam += ses1_cost + ses2_cost
    toplam += (int(PALYAÇO_1*MARKUP) if st.session_state.pal1 else 0)
    toplam += (int(PALYAÇO_2[region]*MARKUP) if st.session_state.pal2 else 0)
    toplam += (int(3500*MARKUP) if st.session_state.pal3 else 0)
    for cnt in [8,12,18,24,30,32]:
        if st.session_state[f"meh{cnt}"]:
            toplam += cnt * int(sem_cost*1.75*MARKUP)
            if location!="Adana":
                if cnt in (8,12,18): toplam+=15000
                elif cnt==24:       toplam+=20000
                else:               toplam+=30000
    st.subheader(f"✅ Genel Toplam: {toplam:,} TL + KDV")
