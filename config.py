import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("24658337"))
API_HASH = getenv("bf99242dbb7f3501f28d39f0a0383cbf")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("6444935129:AAGmLtUrxj03_xbijnVBE_Ef-f9JjrG1-kQ")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://itachi:itachi@itachi.hyhnjlq.mongodb.net/?retryWrites=true&w=majority", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("-1002037503706", None))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("5490773419")

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("YAE X MUSIC")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("11de3676-284d-4d86-acfd-a754d6ad5271")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/GojoDevloper/JiraiyaXMusic.git",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/yaemikologs")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/yae_support")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/cfc2971662ab9f0e6854d.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/f8abaa00e1a953eb0e036.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/9a81db9701f6c5a6a5191.jpg"
STATS_IMG_URL = "https://telegra.ph/file/9a81db9701f6c5a6a5191.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/9a81db9701f6c5a6a5191.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/9a81db9701f6c5a6a5191.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/9a81db9701f6c5a6a5191.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/9a81db9701f6c5a6a5191.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/9a81db9701f6c5a6a5191.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/9a81db9701f6c5a6a5191.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/9a81db9701f6c5a6a5191.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/9a81db9701f6c5a6a5191.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
