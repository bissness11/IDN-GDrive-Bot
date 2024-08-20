import os
import sys
import logging
from gdrive import config
logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    format="[IDN-GDrive-Bot] - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


ENV = bool(os.environ.get('ENV', False))
try:
  if ENV:
    BOT_TOKEN = os.environ.get('BOT_TOKEN','5502855202:AAGW3MYUov5Gb2wWgpcaNTgxDjZ98IFh4P8')
    APP_ID = os.environ.get('APP_ID','6534707')
    API_HASH = os.environ.get('API_HASH','4bcc61d959a9f403b2f20149cbbe627a')
    DATABASE_URL = os.environ.get('DATABASE_URL','postgres://dgdxlptb:uP0wjJhot4kqWrwXg8ENLEFAuEd2yk4d@mouse.db.elephantsql.com/dgdxlptb')
    SUDO_USERS = os.environ.get('SUDO_USERS','1430593323')
    SUPPORT_CHAT_LINK = os.environ.get('SUPPORT_CHAT_LINK','-1001714109958')
    DOWNLOAD_DIRECTORY = os.environ.get("DOWNLOAD_DIRECTORY", "./downloads/")
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID",'161719911468-5jtb7bsug2reg42nts4vmpah5r2l95e1.apps.googleusercontent.com ')
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET",'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')
except KeyError:
  LOGGER.error('One or more configuration values are missing exiting now.')
  sys.exit(1)
