import os
import logging
import yt_dlp

log = logging.getLogger(__name__)


class AudioHandler:
    youtube_url: str = None
    video_id: str = None
    audio_path: str = None

    def __init__(self, ayoutube_url: str) -> None:
        self.youtube_url = ayoutube_url
        self.video_id = ayoutube_url.split("=")[-1]

        CUR_DIR = os.getcwd()
        DUMP_DIR = os.path.join(CUR_DIR, "dump")
        self.audio_path = os.path.join(DUMP_DIR, f"{self.video_id}")

    def download(self):
        ydl_opts = {
            "extractaudio": True,
            "audioformat": "mp3",
            "outtmpl": self.audio_path,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ytdl:
            log.info("Downloading audio")
            ytdl.cache.remove()
            ytdl.download([self.youtube_url])

    def delete(self):
        try:
            os.remove(self.audio_path)

        except Exception as e:
            log.error(f"Error deleteing {e}")


if __name__ == "__main__":
    ah = AudioHandler("https://www.youtube.com/watch?v=rrB13utjYV4")
    ah.download()
    ah.delete()
