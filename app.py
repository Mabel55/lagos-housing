from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# 1. Load the AI Brain
try:
    model = joblib.load('house_price_model.pkl')
    print("✅ Model loaded successfully!")
except:
    print("⚠️ WARNING: Run 'python train_model.py' first!")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 2. Get User Input
        location_input = request.form['location']
        bedrooms = int(request.form['bedrooms'])
        pop_ceiling = int(request.form['pop'])
        close_to_road = int(request.form['road'])

        # DEBUG: Print to terminal so we can see what's happening
        print(f"\n👀 USER INPUT: {location_input}, Beds={bedrooms}, POP={pop_ceiling}, Road={close_to_road}")

        # 3. Translate Location (MUST MATCH TRAIN_MODEL.PY)
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
        
        location_number = location_map[location_input]

        # 4. Make Prediction
        input_data = pd.DataFrame([[location_number, bedrooms, pop_ceiling, close_to_road]], 
                                  columns=['Location', 'Bedrooms', 'POP_Ceiling', 'Close_to_Road'])
        
        estimated_price = model.predict(input_data)[0]

        print(f"🤖 AI PREDICTION: ₦{estimated_price:,.2f}")

        # 5. Show Result
        return render_template('index.html', prediction_text=f"Estimated Rent: ₦{int(estimated_price):,}")

    except Exception as e:
        print(f"❌ ERROR: {e}")
        return f"An error occurred: {e}"

if __name__ == "__main__":
    app.run(debug=True)