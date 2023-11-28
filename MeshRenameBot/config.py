from typing import Union

try:
    from .tconfig import Config
except ImportError:
    class Config:
        DATABASE_URL = [str, "mongodb+srv://ROKU:ROKU@cluster0.nxjre0s.mongodb.net/?retryWrites=true&w=majority"]
        API_HASH = [str, "792b58c18cfc6b59af09fb41f78a008c"]
        API_ID = [int,"23532430"]
        BOT_TOKEN = [str, "6835749558:AAEBQQ7jZKlHdnEjpkZV3Lwsmt3nkFqZOwA"]
        COMPLETED_STR = [str, "▰"]
        REMAINING_STR = [str, "▱"]
        MAX_QUEUE_SIZE = [int, 500]
        SLEEP_SECS = [int, 10]
        IS_MONGO = [bool, True]

        # Access Restriction
        IS_PRIVATE = [bool, False]
        AUTH_USERS = [list,[]]
        OWNER_ID = [int, "1966867320"]

        # Public username url or invite link of private chat
        FORCEJOIN = [str,""]
        FORCEJOIN_ID = [int,]

        TRACE_CHANNEL = [int,"-1001560632964"]

try:
    from .tconfig import Commands
except ImportError:
    class Commands:
        START = "/start"
        RENAME = "/rename"
        FILTERS = "/filters"
        SET_THUMB = "/setthumb"
        GET_THUMB = "/getthumb"
        CLR_THUMB = "/clrthumb"
        QUEUE = "/queue"
        MODE = "/mode"
        HELP = "/help"
