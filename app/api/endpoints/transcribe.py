from fastapi import APIRouter, HTTPException

from app.core import stt, audio_handler
from app.models.stt import TranscribeYoutube

router = APIRouter()


@router.post("/youtube")
async def _transcribe_youtube(request_body: TranscribeYoutube):
    url = request_body.youtube_url
    handler = audio_handler.AudioHandler(url)
    handler.download()

    dg_handler = stt.SpeechToText(handler.audio_file)
    results = await dg_handler.transcribe()

    handler.delete()
    return results
