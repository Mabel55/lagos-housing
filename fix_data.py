import csv

# COMPLETE DATASET: Includes Ikorodu, Lekki, Surulere, Ikeja, Yaba, VI, Ajah, Festac
data = [
    ["Location", "Bedrooms", "POP_Ceiling", "Close_to_Road", "Price_Naira"],
    
    # --- IKORODU (Affordable) ---
    ["Ikorodu_Selewu", 1, 0, 0, 350000],   # Basic 1 Bed
    ["Ikorodu_Selewu", 1, 1, 1, 600000],   # Luxury 1 Bed
    ["Ikorodu_Selewu", 2, 0, 0, 800000],   # Basic 2 Bed
    ["Ikorodu_Selewu", 2, 1, 1, 1500000],  # Luxury 2 Bed
    ["Ikorodu_Selewu", 3, 1, 1, 3000000],  # Luxury 3 Bed

    # --- SURULERE (Mainland Bridge) ---
    ["Surulere", 1, 1, 1, 1200000],       # 1 Bedroom
    ["Surulere", 2, 1, 1, 2500000],       # 2 Bedrooms
    ["Surulere", 3, 1, 1, 5000000],       # 3 Bedrooms

    # --- IKEJA GRA (Luxury Mainland) ---
    ["Ikeja_GRA", 1, 1, 1, 3500000],      # Studio/Mini-flat
    ["Ikeja_GRA", 2, 1, 1, 8000000],      # 2 Bedrooms
    ["Ikeja_GRA", 3, 1, 1, 20000000],     # 3 Bedrooms

    # --- LEKKI PHASE 1 (Premium Island) ---
    ["Lekki_Phase1", 1, 1, 1, 3000000],   # 1 Bedroom
    ["Lekki_Phase1", 2, 1, 1, 6500000],   # 2 Bedrooms
    ["Lekki_Phase1", 3, 1, 1, 12000000],  # 3 Bedrooms

    # --- YABA (Tech Hub) ---
    ["Yaba", 1, 0, 0, 800000],            # Student Room
    ["Yaba", 1, 1, 1, 1500000],           # Luxury Mini-flat
    ["Yaba", 2, 1, 1, 3000000],           # 2 Bedroom
    ["Yaba", 3, 1, 1, 5000000],           # 3 Bedroom

    # --- VICTORIA ISLAND (Business Hub) ---
    ["Victoria_Island", 1, 1, 1, 4000000], 
    ["Victoria_Island", 2, 1, 1, 9000000], 
    ["Victoria_Island", 3, 1, 1, 15000000],

    # --- AJAH (New Lagos) ---
    ["Ajah", 1, 0, 0, 600000],            # Basic
    ["Ajah", 1, 1, 1, 1000000],           # Luxury
    ["Ajah", 2, 1, 1, 2000000],
    ["Ajah", 3, 1, 1, 3500000],

    # --- FESTAC (Mainland Heritage) ---
    ["Festac", 1, 0, 0, 500000],
    ["Festac", 1, 1, 1, 900000],
    ["Festac", 2, 1, 1, 1800000],
    ["Festac", 3, 1, 1, 3000000]
]

filename = "lagos_housing_data.csv"
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"✅ SUCCESS: {filename} has been updated with {len(data)} property examples!")