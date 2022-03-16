import os
import asyncio
import json
from dotenv import load_dotenv

from deepgram import Deepgram


class SpeechToText:
    API_KEY: str = None
    AUDIO_PATH: str = None
    dg_client: Deepgram = None

    def __init__(self, a_audio_path: str) -> None:
        load_dotenv()
        self.API_KEY = os.getenv("API_KEY")
        self.dg_client = Deepgram(self.API_KEY)
        self.AUDIO_PATH = a_audio_path

    async def transcribe(self):
        with open(self.AUDIO_PATH, "rb") as audio:
            source = {"buffer": audio, "mimetype": "audio/mpeg"}

            response = await self.dg_client.transcription.prerecorded(
                source, {"punctuate": True}
            )

        with open("file.json", "w") as f:
            json.dump(response, f, indent=4)

        return response["results"]["channels"][0]
