import streamlit as st

# -----------------------------------
# 🔧 Sabitler ve Parametreler
MARKUP_RATE       = 0.25
MARKUP            = 1 + MARKUP_RATE
DIESEL_PER_L      = 44      # TL/litre
FUEL_CONS_L_100KM = 6.5     # litre/100 km
MEAL_PER_PERSON   = 350     # TL (Adana dışı)
CAR_SMALL_COST    = 2000    # TL (5 kişilik)
CAR_LARGE_COST    = 10000   # TL (turizm araç)

# Semazen birim maliyetleri
SEMAZEN_COSTS = {
    "Adana":1000, "Seyhan":1000, "Yüreğir":1000, "Çukurova":1000, "Sarıçam":1000,
    "Ceyhan":1300, "Karataş":1350, "İmamoğlu":1300, "Kozan":1500, "Karaisalı":1300,
    # … diğer ilçeler merkezleri
    "Merkez":1700,  # Kahramanmaraş/Niğde/Osmaniye/Mersin/Hatay/Gaziantep/Kilis/Aksaray/Nevşehir/Malatya
}

# DJ, palyaço, ses sistemi, palyaço paketleri
DJ_COSTS    = {"Adana":1500, "Cevre":2000, "Uzak":2500}
SES1_COST   = 2500
SES2_COST   = 3500
PALYAÇO1    = 3500
PALYAÇO2    = {"Adana":1500, "Cevre":2000, "Uzak":3000}

# İl → İlçe haritası (sadece kalanları)
PROVINCES = {
    "Adana":        ["Merkez","Seyhan","Yüreğir","Çukurova","Sarıçam"],
    "Kahramanmaraş":["Merkez"],
    "Niğde":        ["Merkez"],
    "Osmaniye":     ["Merkez","Kadirli","Düziçi","Bahçe","Hasanbeyli","Toprakkale","Sumbas"],
    "Mersin":       ["Merkez"],
    "Hatay":        ["Merkez"],
    "Gaziantep":    ["Merkez"],
    "Kilis":        ["Merkez"],
    "Aksaray":      ["Merkez"],
}

# Tahmini karayolu mesafeleri (tek yön km)
ROAD_KM = {
    # Adana ilçeleri
    "Merkez":0, "Seyhan":5, "Yüreğir":10, "Çukurova":10, "Sarıçam":15,
    "Ceyhan":45,"Karataş":55,"İmamoğlu":70,"Kozan":75,"Karaisalı":45,
    # Kahramanmaraş/Niğde/...
    "Merkez":200,  # Kahramanmaraş Merkez için, Niğde Merkez de bu kategori
    "Elbistan":270,
    # … diğer ilçeler için ROAD_KM dict’e ekleyin
}

# -----------------------------------
# 🌐 Başlık
st.title("🎤 İsra Organizasyon Teklif Hesaplayıcı")

# 1️⃣ İl Seçimi
st.markdown("## 1️⃣ İl Seçiniz")
selected_province = None
for il in PROVINCES:
    if st.checkbox(il, key=f"prov_{il}"):
        selected_province = il
        break

# 2️⃣ İlçe Seçimi
selected_district = None
if selected_province:
    st.markdown(f"## 2️⃣ {selected_province} İlçeleri")
    for ilce in PROVINCES[selected_province]:
        if st.checkbox(ilce, key=f"dist_{ilce}"):
            selected_district = ilce
            break

location = selected_district or selected_province or "Adana"

# Bölge türü (DJ/Palyaço2 tarifesi)
if location == "Adana":
    region = "Adana"
elif selected_province:
    region = "Cevre"
else:
    region = "Uzak"

# Karayolu km (gidiş-dönüş)
oneway_km = ROAD_KM.get(location, 0)
roundtrip_km = oneway_km * 2

# 3️⃣ Paket Seçimi
st.markdown("## 3️⃣ Paket Seçimi")
p1 = st.checkbox("📦 Paket 1 – Sunucu+Sanatçı+DJ+Semazen(1–4)+Ses Sistemi 1")
p2 = st.checkbox("📦 Paket 2 – Sunucu+Sanatçı+DJ+Semazen(2–4)+Ses Sistemi 2")
p3 = st.checkbox("📦 Paket 3 – Defli+Semazen(2–4)+Ses Sistemi 2")
solo = st.checkbox("🕋 Sadece Semazen Gösterisi (2–4 Semazen)")
pal1 = st.checkbox("🎈 Palyaço Paketi 1")
pal2 = st.checkbox("🎈 Palyaço Paketi 2")

# 4️⃣ Semazen Sayısı
sem_count_p1 = sem_count_p2 = sem_count_p3 = solo_count = 0
if p1:
    st.markdown("### Paket 1 için Semazen Sayısı")
    for n in (1,2,3,4):
        if st.checkbox(f"{n} Semazen", key=f"p1_sem_{n}"):
            sem_count_p1 = n
            break
if p2:
    st.markdown("### Paket 2 için Semazen Sayısı")
    for n in (2,3,4):
        if st.checkbox(f"{n} Semazen", key=f"p2_sem_{n}"):
            sem_count_p2 = n
            break
if p3:
    st.markdown("### Paket 3 için Semazen Sayısı")
    for n in (2,3,4):
        if st.checkbox(f"{n} Semazen", key=f"p3_sem_{n}"):
            sem_count_p3 = n
            break
if solo:
    st.markdown("### Sadece Semazen için Sayı")
    for n in (2,3,4):
        if st.checkbox(f"{n} Semazen", key=f"solo_sem_{n}"):
            solo_count = n
            break

# 5️⃣ Maliyet Hesaplamaları
# Semazen birim
base_sem = SEMAZEN_COSTS.get(location, 1000)
sem_cost_markup = base_sem * MARKUP

# Personel
sunucu_cost  = base_sem * 1.5 * MARKUP
sanatci_cost = base_sem * 1.5 * MARKUP
dj_cost      = DJ_COSTS[region] * MARKUP

# Ses sistemleri
ses1_cost = SES1_COST * MARKUP
ses2_cost = SES2_COST * MARKUP

# Yakıt & Araç
fuel_cost = round((roundtrip_km * (FUEL_CONS_L_100KM/100) * DIESEL_PER_L))
car_cost  = CAR_SMALL_COST if (p1 and sem_count_p1+3<=5) or (p2 and sem_count_p2+3<=5) else CAR_LARGE_COST

# Yemek
people_count = 0
if p1: people_count += 3 + sem_count_p1
if p2: people_count += 3 + sem_count_p2
if p3: people_count += 1 + 3 + sem_count_p3  # ney+3def+sem
if solo: people_count += solo_count
if pal1: people_count += 1
if pal2: people_count += 2

meal_cost = MEAL_PER_PERSON * people_count if region!="Adana" else 0

# Palyaço
pal1_cost = PALYAÇO1 * MARKUP
pal2_cost = PALYAÇO2[region] * MARKUP

# Mehter (entegre içinde değil, örnek)
mehter_count = 0

# ――― Hesapla butonu ―――
if st.button("💰 Teklifi Hesapla"):
    toplam = 0
    # Paket1
    if p1:
        toplam += sunucu_cost + sanatci_cost + dj_cost + ses1_cost
        toplam += sem_count_p1 * sem_cost_markup
    # Paket2
    if p2:
        toplam += sunucu_cost + sanatci_cost + dj_cost + ses2_cost
        toplam += sem_count_p2 * sem_cost_markup
    # Paket3
    if p3:
        toplam += sunucu_cost + sanatci_cost + ses2_cost
        toplam += sem_count_p3 * sem_cost_markup
    # Sadece semazen
    if solo:
        toplam += solo_count * sem_cost_markup + fuel_cost + car_cost + meal_cost
    # Palyaço
    if pal1:
        toplam += pal1_cost + fuel_cost + car_cost + meal_cost
    if pal2:
        toplam += pal2_cost + fuel_cost + car_cost + meal_cost

    st.subheader(f"🏷️ Genel Toplam: {int(toplam):,} TL + KDV")
