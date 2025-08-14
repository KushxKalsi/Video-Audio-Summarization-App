import streamlit as st
import librosa
import soundfile as sf
import os

# Function to handle video/audio processing
def extract_audio(video_file):
    from moviepy.editor import VideoFileClip
    video = VideoFileClip(video_file)
    audio = video.audio
    audio.write_audiofile("output_audio.wav")
    os.system('ffmpeg -y -i output_audio.wav -acodec pcm_s16le -ar 16000 outputAudio.wav')
    return "outputAudio.wav"

# Function to transcribe audio
def transcribe_audio(audio_file):
    import torch
    from huggingsound import SpeechRecognitionModel
    model = SpeechRecognitionModel('jonatasgrosman/wav2vec2-large-xlsr-53-english', device="cuda" if torch.cuda.is_available() else "cpu")
    stream = librosa.stream(
        audio_file,
        block_length=60,
        frame_length=16000,
        hop_length=16000
    )
    
    for i, speech in enumerate(stream):
        sf.write(f'{i}.wav', speech, 16000)
    
    audio_paths = [f'{i}.wav' for i in range(i + 1)]
    transcriptions = model.transcribe(audio_paths)
    
    full_transcription = ''.join([item['transcription'] for item in transcriptions])
    full_transcription = full_transcription.lower()
    return full_transcription

# Function to summarize text in chunks of 1000 words
def summarize_text(full_transcription):
    from textblob import TextBlob
    from transformers import pipeline
    summarizer = pipeline('summarization')

    # Split transcription into chunks of 1000 words each
    # words = full_transcription.split()
    # chunk_size = 1000
    sentences = []

    # for i in range(0, len(words), chunk_size):
    #     chunk = ' '.join(words[i:i + chunk_size])
    #     text = summarizer(chunk)
    
    text = summarizer(full_transcription)
    sentences.extend([item['summary_text'] for item in text])

    joined_text = ' '.join(sentences)
    b = TextBlob(joined_text)
    return str(b.correct())

# Streamlit app layout
def main():
    st.title("Video/Audio Summarization App")
    uploaded_file = st.file_uploader("Upload a video or audio file", type=["mp4", "wav", "mp3"])
    if uploaded_file is not None:
        # Save the file temporarily
        with open("uploaded_file", "wb") as f:
            f.write(uploaded_file.read())
        
        # Extract audio if it's a video
        if uploaded_file.name.endswith('.mp4'):
            st.write("Extracting audio from video...")
            audio_path = extract_audio("uploaded_file")
        else:
            audio_path = "uploaded_file"

        # Transcribe audio
        st.write("Transcribing audio...")
        transcription = transcribe_audio(audio_path)
        st.text_area("Transcription", transcription, height=200)

        # Summarize the transcription
        st.write("Summarizing transcription...")
        summary = summarize_text(transcription)
        st.text_area("Summary", summary, height=200)

# Call the main function
main()