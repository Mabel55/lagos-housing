import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import joblib

# 1. Load Data
try:
    data = pd.read_csv('lagos_housing_data.csv')
    print("✅ Data Loaded Successfully!")

    # 2. Map Locations (MUST MATCH APP.PY)
    location_map = {
        'Ikorodu_Selewu': 0,
        'Lekki_Phase1': 1,
        'Surulere': 2,
        'Ikeja_GRA': 3,
        'Yaba': 4,
        'Victoria_Island': 5,
        'Ajah': 6,
        'Festac': 7
    }
    
    # Translate text to numbers
    data['Location'] = data['Location'].map(location_map)

    # 3. Features (Inputs) & Target (Output)
    X = data[['Location', 'Bedrooms', 'POP_Ceiling', 'Close_to_Road']]
    y = data['Price_Naira']

    # 4. Train the Model
    model = DecisionTreeRegressor()
    model.fit(X, y)
    print("🧠 Training Complete (Decision Tree)!")

    # 5. Save the Brain
    joblib.dump(model, 'house_price_model.pkl')
    print("💾 Model saved as 'house_price_model.pkl'")

except Exception as e:
    print(f"❌ Error during training: {e}")