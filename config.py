import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 23900880
API_HASH = "137f9ff5e213f143a532ff8d12431004"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7136727874:AAG8Bjs30e4PL8gHQy4UhSYkF95qQ9C53_c"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://pkis7739036068:Hearted@2023@cluster0.sepld.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1001649081118

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 6309624343

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/study_with_dreamers"
SUPPORT_GROUP = "https://t.me/study_with_dreamers"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQFsstAAHPYDmwytu2wBScZ_YmGrzhAhygob0uE5lJP9fU3G_45fzYvVkY-frxfijQ4_bGWZe3ehWu9lJ1HRx2Q0OUVqLDdYkqwHipLNGZQ3uIWd5AKS4DftmLOn_sF1rpXsseWDzuBKds4utvsF-ncv2jQpEPt-wqJt0M9_jPVbpTKSvRX-leiePyIqRkQ88vyvMYLmYyEZ5hF7_FnIsha5xuwro_nnA9tBKdjZJeuIZpiRERaAiGR1jGWzTLxXGMz8SI9E3RxQo3ulfcPC-alpszio60Zfoa2oRym5YmatULxJ4UVstXrv0HpYwwzCwrhoxuynJaOlTF-j2AG4aZfnLPETfQAAAAF4FToXAA"
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


START_IMG_URL = "https://graph.org/file/a20bea0b2db07ee9f33d1-c6e1a77221fdbf6435.jpg"

PING_IMG_URL = "https://graph.org/file/a20bea0b2db07ee9f33d1-c6e1a77221fdbf6435.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/c0fc70e21d4eb7110050c-0c9f6a734f5328c63b.jpg"
STATS_IMG_URL = "https://graph.org/file/c0fc70e21d4eb7110050c-0c9f6a734f5328c63b.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
TELEGRAM_VIDEO_URL = "https://graph.org/file/c0fc70e21d4eb7110050c-0c9f6a734f5328c63b.jpg"
STREAM_IMG_URL = "https://graph.org/file/c0fc70e21d4eb7110050c-0c9f6a734f5328c63b.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/c0fc70e21d4eb7110050c-0c9f6a734f5328c63b.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/c0fc70e21d4eb7110050c-0c9f6a734f5328c63b.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/c0fc70e21d4eb7110050c-0c9f6a734f5328c63b.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/c0fc70e21d4eb7110050c-0c9f6a734f5328c63b.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
