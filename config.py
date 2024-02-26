import os

API_ID = API_ID = 20778821

API_HASH = os.environ.get("API_HASH", "70ddbf0162bafe8b7e0007c3b22d01c0")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6628279167:AAFnEvwm9siVGx8G6IscwSoodCRxIx5HSf8")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6236239489))

LOG = -1002091621555

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6236239489").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


