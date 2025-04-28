from pydub import AudioSegment
import os

# Example folder - I updated the names for every new folder i wanted to create
input_folder = "raga_samples/Hamsadhwani"
output_folder = "raga_samples/Hamsadhwani_wav"

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    if file.endswith(".mp3"):
        mp3_path = os.path.join(input_folder, file)
        wav_filename = os.path.splitext(file)[0] + ".wav"
        wav_path = os.path.join(output_folder, wav_filename)

        sound = AudioSegment.from_mp3(mp3_path)
        sound.export(wav_path, format="wav")
        print(f"Converted {file} to {wav_filename}")
