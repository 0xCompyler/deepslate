from pydantic import BaseModel


class TranscribeYoutube(BaseModel):
    youtube_url: str
