import librosa
import numpy as np

def extract_features(audio_path):
    y, sr = librosa.load(audio_path)

    pitch, voiced_flag, voiced_probs = librosa.pyin(
        y,
        fmin=librosa.note_to_hz('C2'),
        fmax=librosa.note_to_hz('C7')
    )

    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)

    features = np.hstack([
        np.nanmean(pitch),
        np.nanstd(pitch),
        np.nanmean(mfccs, axis=1),
        np.nanstd(mfccs, axis=1)
    ])

    return features
