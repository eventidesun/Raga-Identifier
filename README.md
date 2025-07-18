# Raga Identifier

## Project Overview
This project is a Raga Identifier system that predicts the raga of an input audio clip based on its musical features.
It focuses on Carnatic and Hindustani music styles and applies machine learning techniques to solve a real-world audio classification problem.

The project automates:
- Downloading YouTube audio samples
- Converting audio to usable formats
- Extracting meaningful audio features
- Training a classification model (KNN)
- Predicting the raga from unseen audio clips

## Technologies Used
- Python 3.10
- librosa (audio feature extraction)
- pytube and yt-dlp (YouTube audio downloading)
- pydub (audio format conversion)
- scikit-learn (machine learning)
- numpy (numerical operations)
- joblib (model saving and loading)

## How it Works
1. Using yt-dlp, audio clips are downloaded from YouTube links based on selected ragas.
2. Downloaded mp3 files are converted to wav format using pydub and ffmpeg to ensure compatibility with feature extraction.
3. Each raga has its own folder under raga_samples/, containing all the corresponding wav files.
4. For each audio file: 
   - Pitch contours are extracted using librosa.pyin.
   - mfccs (Mel Frequency Cepstral Coefficients) are computed.
   - Features are aggregated into a numerical vector.
5. To train the model. a K-Nearest Neighbors (KNN) classifier is trained on the extracted features and then the model is saved using joblib for reuse without retraining.
6. Finally, a separate script loads the trained model and given a new audio clip, it predicts the corresponding raga.





