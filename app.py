import streamlit as st
from datetime import datetime

# ―――――――――――――――――――――
# 🚩Sabirler
MARKUP   = 1.25
SEMAZEN  = {
    "Adana":1000,
    "Kahramanmaraş":1700,
    "Niğde":1700,
    "Osmaniye":1500,
    "Tarsus":1300,
    "Mersin":1500,
    "Hatay":1700,
    "Aksaray":1900,
    "Nevşehir":1900,
    "Malatya":2500
}
DJ_COSTS    = {"Adana":1500,"Cevre":2000,"Uzak":2500}
PALYAÇO_1   = 3500
PALYAÇO_2   = {"Adana":1500,"Cevre":2000,"Uzak":3000}
SES1_COST   = 2500
SES2_COST   = 3500

# İl → İlçe haritası
PROVINCES = {
    "Adana":    ["Seyhan","Yüreğir","Çukurova","Sarıçam","Ceyhan","Karataş","İmamoğlu","Kozan","Karaisalı","Pozantı","Aladağ","Tufanbeyli","Saimbeyli","Feke"],
    "Kahramanmaraş": ["Merkez","Dulkadiroğlu","Elbistan","Afşin","Türkoğlu","Pazarcık","Andırın","Göksun","Ekinözü","Nurhak"],
    "Niğde":    ["Merkez","Bor","Ulukışla","Çamardı","Altunhisar","Çiftlik"],
    "Osmaniye": ["Merkez","Kadirli","Düziçi","Bahçe","Hasanbeyli","Toprakkale","Sumbas"],
    "Tarsus":   ["Merkez"],
    "Mersin":   ["Merkez"],
    "Hatay":    ["Merkez","Antakya","İskenderun","Reyhanlı","Kırıkhan","Dörtyol","Erzin","Belen","Samandağ","Altınözü","Hassa","Payas","Yayladağı"],
    "Gaziantep":["Şahinbey","Şehitkamil","Nizip","Araban","Karkamış","Yavuzeli","Oğuzeli","Islahiye","Nurdağı"],
    "Kilis":    ["Merkez"],
    "Aksaray":  ["Merkez","Ortaköy","Eskil","Gülağaç","Güzelyurt","Sarıyahşi","Ağaçören"],
    "Nevşehir":["Merkez"],
    "Malatya":  ["Merkez"]
}

# ―――――――――――――――――――――
# 🎨 Arayüz

st.title("🎤 İsra Organizasyon Teklif Hesaplayıcı")

# 1) İl Seçimi
st.markdown("#### 1️⃣ İl Seçiniz")
selected_province = None
for il in PROVINCES:
    if st.checkbox(il, key=f"prov_{il}"):
        selected_province = il
        # kullanıcının birden fazla seçmesinin önüne geçmek için break
        break

# 2) İlçe Seçimi (sadece il seçildiyse)
selected_district = selected_province
if selected_province:
    st.markdown(f"#### 2️⃣ `{selected_province}` İlçeleri")
    for ilce in PROVINCES[selected_province]:
        if st.checkbox(ilce, key=f"dist_{ilce}"):
            selected_district = ilce
            break

location = selected_district or "Adana"

# Bölge türü
if location == "Adana":
    region = "Adana"
elif selected_province:
    region = "Cevre"
else:
    region = "Adana"

# 3) İlahi Grubu Paketleri
st.markdown("#### 3️⃣ İlahi Grubu Paket Seçimi")
paket1 = st.checkbox("Paket 1 – Sunucu+Sanatçı+DJ (semazen sayısı seçenekli)", key="p1")
paket2 = st.checkbox("Paket 2 – Canlı Enstrümanlı", key="p2")
paket3 = st.checkbox("Paket 3 – Defli", key="p3")

# 4) Ortak Değişkenler
sem_cost = SEMAZEN.get(selected_province, SEMAZEN["Adana"])
sunucu_cost  = int(sem_cost * 1.5 * MARKUP)
sanatci_cost = int(sem_cost * 1.5 * MARKUP)
dj_cost      = int(DJ_COSTS[region] * MARKUP)
ses1_cost    = int(SES1_COST * MARKUP)
ses2_cost    = int(SES2_COST * MARKUP)

# ―――――――――――――――――――――
# 📋 Paket 1
if paket1:
    st.markdown("**Paket 1 İçeriği**")
    st.checkbox(f"✅ 1 Sunucu ({sunucu_cost} TL)",   value=True, disabled=True)
    st.checkbox(f"✅ 1 Sanatçı ({sanatci_cost} TL)", value=True, disabled=True)
    st.checkbox(f"✅ 1 DJ ({dj_cost} TL)",           value=True, disabled=True)

    st.markdown("**Semazen Sayısı**")
    s1 = st.checkbox(f"1 Semazen ({int(sem_cost*MARKUP)} TL)", key="s1")
    s2 = st.checkbox(f"2 Semazen ({int(sem_cost*2*MARKUP)} TL)", key="s2")
    s3 = st.checkbox(f"3 Semazen ({int(sem_cost*3*MARKUP)} TL)", key="s3")
    s4 = st.checkbox(f"4 Semazen ({int(sem_cost*4*MARKUP)} TL)", key="s4")

    st.markdown("**Ses Sistemi 1**")
    st.checkbox(f"✅ 4 Hoparlör, 1 Mikser, 1 Power, 1 Kablosuz Mikrofon ({ses1_cost} TL)", 
                value=True, disabled=True)

# ―――――――――――――――――――――
# 📋 Paket 2
if paket2:
    st.markdown("**Paket 2 İçeriği (Canlı Enstrümanlar)**")
    st.checkbox(f"✅ 1 Sunucu ({sunucu_cost} TL)",   value=True, disabled=True)
    st.checkbox(f"✅ 1 Sanatçı ({sanatci_cost} TL)", value=True, disabled=True)
    st.checkbox(f"✅ 1 DJ ({dj_cost} TL)",           value=True, disabled=True)

    st.markdown("**Ses Sistemi 2**")
    st.checkbox(f"✅ 4 Hoparlör, 1 Mikser, 1 Power, 1 Kanun Mik., 1 Keman Mik., 1 Ritm Saz Mik., 1 Ney Mik. ({ses2_cost} TL)", 
                value=True, disabled=True)

# ―――――――――――――――――――――
# 📋 Paket 3
if paket3:
    st.markdown("**Paket 3 İçeriği (Defli)**")
    st.checkbox("✅ 1 Ney", value=True, disabled=True)
    st.checkbox("✅ 3 Defli Solist", value=True, disabled=True)

    st.markdown("**Ses Sistemi 2**")
    st.checkbox(f"✅ 4 Hoparlör, 1 Mikser, 1 Power, 1 Kablosuz Mik., 1 Ney Mik., 3 Def Mik. ({ses2_cost} TL)", 
                value=True, disabled=True)

# ―――――――――――――――――――――
# Hesapla Butonu
if st.button("💰 Teklifi Hesapla"):
    toplam = 0
    # Paket 1
    if paket1:
        toplam += sunucu_cost + sanatci_cost + dj_cost
        toplam += (1 if s1 else 0 + 2 if s2 else 0 + 3 if s3 else 0 + 4 if s4 else 0) * int(sem_cost*MARKUP)
        toplam += ses1_cost
    # Paket 2
    if paket2:
        toplam += sunucu_cost + sanatci_cost + dj_cost + ses2_cost
    # Paket 3
    if paket3:
        toplam += sem_cost*1.75*MARKUP*4  # basit örnek: defli toplam maliyet
        toplam += ses2_cost
    st.subheader(f"✅ Genel Toplam: {int(toplam):,} TL + KDV")
