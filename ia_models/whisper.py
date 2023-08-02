import openai

from pydub import AudioSegment



invoice = AudioSegment.from_file("media/voice_note.ogg", "ogg")
invoice.export("media/voice_note.mp3", format="mp3")


# audio_file= open("/path/to/file/audio.mp3", "rb")
# transcript = openai.Audio.transcribe("whisper-1", audio_file)