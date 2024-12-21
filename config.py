import re
import os
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("11638149", None))
API_HASH = getenv("7fdb30860c464e73d3d401b01f668c25", None)

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7762993826:AAEZcE5mC9C_zTO3fhh1nMCyRe1SldzHPzQ", None)

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://mongouser:shivammongo@cluster.8dvkd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster", None)
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", None)
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 900))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("-1002274484430", None))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", None))

# Get this value Telegram id
OWNER_ID = int(getenv("OWNER_ID", "7113865066"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("tabahi69")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HRKU-ecc3df77-2524-4520-b2f5-a5efc5065145")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Learningbots79/LB_Music",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/gitchey")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/glitchifys")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# Auto Gcast/Broadcast Handler (True = broadcast on , False = broadcast off During Hosting, Dont Do anything here.)
AUTO_GCAST = os.getenv("AUTO_GCAST")

# Auto Broadcast Message That You Want Use In Auto Broadcast In All Groups.
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", "")

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "bcfe26b0ebc3428882a0b5fb3e872473")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "907c6a054c214005aeae1fd752273cc4")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "2000"))

# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session
STRING1 = getenv("BQG6OwEAKnnAdNkqzkaFx_f6eyast5ArdjoNb2GF4DEDk2rxOCJDbBwisUAQeiKEguKMAONZzTmtMqIy53fPwfIXwNaNO_AJZxwoP3GFJuBEr4UV4fVUiiFx4qLtTd5ZCQF5rdKOCf7Q4VbX4x37F8UP3UJ-K4wtIo1prGtrFsKrCpaLguk7sLUOLvwi-qyGcHYL2lQe5UN0ip3v_XkT5i88pMQoL6M7iNeCkG6gauLMbxUwmqAOumQwz6SnFFFO2p9aLpfbtRmxsCF0nNaUlyj95uvbXt6el7pvtHZDePqKXj5lmUWWdzp5ZqHq9jWTFGbFwC8-Oo1OlrE8YbykPWAq9vrj8gAAAAGoBPdqAA",  None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/cad7038fe82e47f79c609.jpg

"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/cad7038fe82e47f79c609.jpg

"
)
PLAYLIST_IMG_URL = "hhttps://telegra.ph/file/cad7038fe82e47f79c609.jpg

"
STATS_IMG_URL = "https://telegra.ph/file/cad7038fe82e47f79c609.jpg

"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/cad7038fe82e47f79c609.jpg

"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/cad7038fe82e47f79c609.jpg

"
STREAM_IMG_URL = "https://telegra.ph/file/cad7038fe82e47f79c609.jpg

"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/cad7038fe82e47f79c609.jpg

"
YOUTUBE_IMG_URL = "https://telegra.ph/file/cad7038fe82e47f79c609.jpg

"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/cad7038fe82e47f79c609.jpg

"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/cad7038fe82e47f79c609.jpg

"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/cad7038fe82e47f79c609.jpg

"


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
