import re
import random
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("23716755"))
API_HASH = getenv("5503b68991d161b6863dba06ff28fcb0")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7039575496:AAEvIXHELmQLTo7Bbm4CDGsbKoYebm8oS7E")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://admin22:admin22@cluster0.9lqp0ci.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = int(getenv("-1002204218687", None))

# Get this value from @MissRose_Bot on Telegram by /id
OWNER_ID = int(getenv("6209871909", None))

# Fill Queue Limit . Example - 15
QUEUE_LIMIT = int(getenv("-15", "10"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/TeamInflex/InflexMusicBot",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/YorXSupport")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/YorXSupport")

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


# Get your pyrogram v2 session from Replit
STRING1 = getenv("BQFp45MALFdC7_vb5dWVJB72Rwkwh_h3d7e78BVtVRNk2GK90fLcTMtNw97BwoNeCU39Z9C-KjY6jwUkrisgzhXrk5iORwnDv-qEUjHepGDYA5zmRJ-1qgKJNjdNkp1NoVAD9Pw2ctRYPZ8GRCaVP97yernOz-vOVdUhFHbdZcDXG6QnOMRmZPZzJPjbflGC-zmKvQjbHQXtx2g00nUSNhWsuBQACj5atNO1qk71rEmQcVpjGg0MNRcbTXszIatRMl9AmtJhikFk6-gmQ63fxry3KNvTXIDclQX1luVDWj3UVPoRdQL3y2z7m7sRDyzwQAJXozcOd3J2Bhnkq_k3znPX45tvtgAAAAGvHwl_AA", None)
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


START_IMG_URL = ["https://graph.org/file/8fe8c4eb2886376e48423.jpg", "https://graph.org/file/89e0800248a16eb93515b.jpg", "https://graph.org/file/df74d3cb75436c6f1e345.jpg", "https://graph.org/file/d57d12a1d0cd409d8eec4.jpg", "https://graph.org/file/6ce1ae50a475b058b79f9.jpg", "https://graph.org/file/a5af4a1a970b39a936c1d.jpg", "https://graph.org/file/e8a56835015bf849637cf.jpg", "https://graph.org/file/829b7bcb6eb706765b3d2.jpg", "https://graph.org/file/3c61dd910606440ee8f66.jpg"]
PING_IMG_URL = ["https://graph.org/file/3c5ba5eaddad3b9aa2790.jpg", "https://graph.org/file/556669af8776281c962ca.jpg", "https://graph.org/file/e24ddcc48bf5c191978b7.jpg", "https://graph.org/file/165eef1799e0edd83b56d.jpg", "https://graph.org/file/1135f6756396a2d130921.jpg", "https://graph.org/file/e24ddcc48bf5c191978b7.jpg"]
STATS_IMG_URL = ["https://graph.org/file/2186735b6999d0c0f53e3.jpg"]
PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL", "https://graph.org/file/9d75bfb77e17b80b3da5b.png"
)
TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL", "https://graph.org/file/9d75bfb77e17b80b3da5b.png"
)
TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL", "https://graph.org/file/9d75bfb77e17b80b3da5b.png"
)
STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL", "https://te.legra.ph/file/693694b0d94afa372ca5a.jpg"
)
SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL", "https://te.legra.ph/file/f72ea4bd955c418c724e1.jpg"
)
YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL", "https://telegra.ph/file/5547c6a0bcfc016089088.png"
)
SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL", "https://te.legra.ph/file/c3682dc6fd740b2dac969.jpg"
)
SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL", "https://te.legra.ph/file/c3682dc6fd740b2dac969.jpg"
)
SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL", "https://te.legra.ph/file/c3682dc6fd740b2dac969.jpg"
)


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
