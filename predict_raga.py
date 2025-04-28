import joblib
from extract_features import extract_features

model = joblib.load('raga_model.pkl')

def predict(audio_path):
    features = extract_features(audio_path)
    prediction = model.predict([features])
    return prediction[0]

if __name__ == "__main__":
    path = input("Enter path to the WAV file you want to predict: ")
    raga = predict(path)
    print(f"Predicted Raga: {raga}")
