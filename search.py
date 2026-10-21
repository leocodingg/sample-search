import torch
import librosa
from transformers import ClapModel, ClapProcessor

model = ClapModel.from_pretrained("laion/clap-htsat-unfused")
processor = ClapProcessor.from_pretrained("laion/clap-htsat-unfused")

print("loaded")

audio, sr = librosa.load("samples/jazzy loop.mp3", sr=48000)

print(audio.shape, sr)

inputs = processor(audio, sampling_rate=sr, return_tensors="pt")

with torch.no_grad():
    audio_embed = model.get_audio_features(**inputs)

print(audio_embed.shape)