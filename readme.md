# Telegram whisper bot

This bot recieves audio and downloads it, then changes the format from ogg to mp3 in order to be digested by Whisper.

The Whisper endpoint will be other repo linked here.

If you wish, you can use the whisper script inside ia_models if you have OpenAI tokens available instead of the local implementation.

The core here is to download and convert the audio file.

## Installation

- First of all you should have a bot token from Telegram. You can get one from the BotFather.

- Another thing is ffmpeg, which is a dependency of pydub. You can install it with:

```bash
apt-get install ffmpeg libavcodec-extra
```

- Now create a virtual environment and install the requirements:

```python
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```

To run the project just run the main.py file:

```python
python main.py
```

And the bot will be listening to audios and text.

## Requirements

- Python 3.8+
- ffmpeg