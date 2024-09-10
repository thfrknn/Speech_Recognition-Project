<h1 align="left">Audio Recording and Transcription Project </h1>
This project aims to record audio, split the audio files into specific segments, and transcribe these segments using Google Speech-to-Text API. The project is developed using Python and several popular libraries.

Requirements
To run the project, you need to install the following Python libraries:

pyaudio: Manages audio streaming and recording.
wave: Reads and writes WAV format audio files.
keyboard: Listens to keyboard events.
pydub: Processes audio files.
speech_recognition: Transcribes audio files.
datetime: Retrieves date and time information.
Installation
<h2 align="left">Step 1: </h2>
Install Python and pip
Ensure Python is installed on your computer. You can download the latest version of Python and pip from the official Python website.

<h2 align="left">Step 2:Install Libraries </h2>
Use the following commands to install the required Python libraries:

bash
Copy code
pip install pyaudio wave keyboard pydub SpeechRecognition
<h2 align="left">Step 3: Install FFmpeg </h2>

The pydub library requires FFmpeg or avconv for audio processing. You can download and install FFmpeg from the official FFmpeg website. After installation, make sure FFmpeg is available in your system PATH by running the ffmpeg command in your terminal or command prompt.

Usage
Recording Audio

The recordAudio() function allows you to start recording by pressing the 't' key and stop recording by pressing the 'y' key. To terminate the recording process, press the 'q' key.

Processing and Transcribing the Audio File

The process_audio_file() function splits the audio file into 15-second segments and transcribes each segment using Google Speech-to-Text API. Transcriptions are saved to a text file with a filename that includes the date and time information.

Running the Script
To run the project, execute the following command in your terminal or command prompt:

bash
Copy code
python <script_name>.py
Here, <script_name>.py is the name of your main Python script (e.g., SpeechToText.py).

Troubleshooting
FFmpeg not found: Ensure FFmpeg is added to your system PATH.
Library not installing: Make sure to install missing libraries using pip.
Contributing
This project is open to individual or collective contributions. If you wish to contribute, please create a pull request or report an issue.

License
This project is licensed under the MIT License.

