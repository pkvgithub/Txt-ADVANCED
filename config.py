import os

API_ID = API_ID = 26349510

API_HASH = os.environ.get("API_HASH", "a4f6c5bdb4ce4b9c5f2eb88b3dda8d55")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7160465659:AAHRxaAgvcuaOWe4a6fj4EeOQk7tv91CKf8")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6880857886))

LOG = -1002085617089

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "745084259").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


