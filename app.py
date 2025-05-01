import streamlit as st

MARKUP = 1.25
DIESEL_PER_L = 44
FUEL_CONS_L_100 = 6.5

# … sabit sözlükler tanımlı …

# 1) İl + İlçe seçimi (checkbox hiyerarşi)
il = st.selectbox("İl", ["Adana","Kahramanmaraş",…])
ilce = st.selectbox("İlçe", PROVINCES[il])

# 2) Paket seçimi
p1 = st.checkbox("Paket 1")
p2 = st.checkbox("Paket 2")
p3 = st.checkbox("Paket 3")
solo = st.checkbox("Sadece Semazen Gösterisi")
pal1 = st.checkbox("Palyaço Paketi 1")
pal2 = st.checkbox("Palyaço Paketi 2")

# 3) Ortak veriler
sem = SEMAZENLER[ilce]
sunucu = sem*1.5
sanatci = sem*1.5
dj = DJ_COSTS[region]
ses1 = 2500
ses2 = 3500

# 4) Km ve yakıt
km = get_route_km("Adana", ilce)            # sürüş mesafesi fonksiyonu
fuel_cost = km*2*(FUEL_CONS_L_100/100)*DIESEL_PER_L

# 5) Yemek
kisiler = …  # semazen sayısı, mehter sayısı, palyaço
yemek_cost = 350 * kisiler if il!="Adana" else 0

# 6) Araç
arac_cost = 2000 if kisiler<=5 else 10000

# 7) Hesapla
toplam = 0
if p1:
    toplam += sunucu+sanatci+dj+ses1
    toplam += sem*semazen_sayisi
if p2:
    toplam += sunucu+sanatci+dj+ses2
    toplam += sem*semazen_sayisi
if p3:
    toplam += sem*1.75*semazen_sayisi + ses2
if solo:
    toplam += sem*semazen_sayisi + fuel_cost + yemek_cost + arac_cost
if pal1:
    toplam += PALYAÇO_1 + fuel_cost + yemek_cost + arac_cost
if pal2:
    toplam += PALYAÇO_2[region] + fuel_cost + yemek_cost + arac_cost

# Kar
final_price = toplam * MARKUP
st.write(f"🏷️ Teklif: {final_price:.0f} TL + KDV")
