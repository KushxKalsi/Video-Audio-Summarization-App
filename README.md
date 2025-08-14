# Video/Audio Summarization Application

A Python-based Streamlit **Video/Audio Summarization Application** that allows users to upload audio or video files, transcribe the content, and generate concise summaries for easy reference.

## Features

- Upload and process video/audio files for transcription
- Automatic transcription of audio content using Wav2Vec 2.0
- Summarize lengthy transcriptions into brief, digestible content
- User-friendly interface with real-time processing and feedback

## Screenshots

<table>
  <tr>
    <td align="center">Home Screen</td>
    <td><img src="https://github.com/LavKalsi/Video-Audio-Summarization-App/blob/main/Screenshots/Home%20Screen.jpg" width="640" height="294"/></td>
  </tr>
  <tr>
    <td align="center">Transcription Output</td>
    <td><img src="https://github.com/LavKalsi/Video-Audio-Summarization-App/blob/main/Screenshots/TranscriptionExample.jpg" width="600" height="200"/></td>
  </tr>
<tr>
  <td align="center">Summary Output</td>
  <td><img src="https://github.com/LavKalsi/Video-Audio-Summarization-App/blob/main/Screenshots/SummaryExample.jpg" width="600" height="200"/></td>
</tr>
</table>

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/VideoAudioSummarizationApp.git
    cd VideoAudioSummarizationApp
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

## Usage

1. Open the application in your browser (typically at `http://localhost:8501`).
   
2. Upload a video or audio file in **.mp4**, **.wav**, or **.mp3** format.

3. The app will extract audio (if a video file is uploaded), transcribe it, and display the transcription.

4. View the summarized content in the Summary section.

## Adding Audio/Video Samples to GitHub

To add sample audio or video files to GitHub:

1. Place sample files in a directory within the project, such as `sample_files/`.
2. In your README, provide links to these files for easy access.
3. Use these sample files for demo purposes or to facilitate testing and contributions.

## Built With

- [Python](https://www.python.org/) - The programming language used.
- [Streamlit](https://streamlit.io/) - For the interactive web application.
- [Hugging Face Transformers](https://huggingface.co/) - For speech-to-text and summarization models.
- [Librosa](https://librosa.org/) - For audio processing.

## Contributing

Contributions are welcome! To contribute, please submit a pull request and follow the standard GitHub workflow.

## Acknowledgments

- Hugging Face community for providing state-of-the-art NLP models.
- Inspiration from various NLP resources for implementing the summarization feature.

## Author

Lav Kalsi
