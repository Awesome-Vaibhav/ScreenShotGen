import os


class Config:

    API_ID = "17520136"
    API_HASH = "c1860784db86000a0eaec3f916d6d4ee"
    BOT_TOKEN = "6717780247:AAEwHzIP2xzZdsiFefVTZn5senscOPrnHHc"
    SESSION_NAME = "SS_Gen"
    LOG_CHANNEL = -1002092439112
    DATABASE_URL = "mongodb+srv://v8242428a2749464:Vaibhav8242428@screenshotgen.0h9ce5p.mongodb.net/?retryWrites=true&w=majority"
    AUTH_USERS = "5798143340","5798143340"
    MAX_PROCESSES_PER_USER = int(os.environ.get("MAX_PROCESSES_PER_USER", 15))
    MAX_TRIM_DURATION = int(os.environ.get("MAX_TRIM_DURATION", 600))
    TRACK_CHANNEL = int(os.environ.get("TRACK_CHANNEL", False))
    SLOW_SPEED_DELAY = int(os.environ.get("SLOW_SPEED_DELAY", 2))
    HOST = os.environ.get("HOST", "")
    TIMEOUT = int(os.environ.get("TIMEOUT", 60 * 30))
    DEBUG = bool(os.environ.get("DEBUG"))
    WORKER_COUNT = int(os.environ.get("WORKER_COUNT", 20))
    IAM_HEADER = os.environ.get("IAM_HEADER", "")

    COLORS = [
        "white",
        "black",
        "red",
        "blue",
        "green",
        "yellow",
        "orange",
        "purple",
        "brown",
        "gold",
        "silver",
        "pink",
    ]
    FONT_SIZES_NAME = ["Small", "Medium", "Large"]
    FONT_SIZES = [30, 40, 50]
    POSITIONS = [
        "Top Left",
        "Top Center",
        "Top Right",
        "Center Left",
        "Centered",
        "Center Right",
        "Bottom Left",
        "Bottom Center",
        "Bottom Right",
    ]
