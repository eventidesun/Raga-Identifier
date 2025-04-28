import os
import numpy as np
import joblib
from sklearn.neighbors import KNeighborsClassifier
from extract_features import extract_features

# The folder with the data
data_folder = 'raga_samples'
raga_labels = os.listdir(data_folder)

X = []
y = []

# Extract features from all the files
for raga in raga_labels:
    raga_path = os.path.join(data_folder, raga)
    for file in os.listdir(raga_path):
        file_path = os.path.join(raga_path, file)
        features = extract_features(file_path)
        X.append(features)
        y.append(raga)

X = np.array(X)
y = np.array(y)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

# Save the model
joblib.dump(model, 'raga_model.pkl')
print("Model saved as raga_model.pkl")
