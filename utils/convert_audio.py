from pydub import AudioSegment

from pathlib import Path
#from ..settings import config

from main_project.settings import config

BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = BASE_DIR.parent

#from PROJECT_DIR.settings import config

MEDIA_FOLDER = config["MEDIA_FOLDER"]

def convert_audio(audio_name, original_audio_format, new_audio_format):
    invoice = AudioSegment.from_file(f"{MEDIA_FOLDER}{audio_name}", original_audio_format)
    new_audio_name = audio_name.replace(original_audio_format, new_audio_format)
    invoice.export(f"{MEDIA_FOLDER}{new_audio_name}", new_audio_format)
