import os, urlparse

DEBUG = False
if os.environ.get("DEBUG"):
    DEBUG = True

LOG_LEVEL = os.environ.get("LOG_LEVEL", "DEBUG")
REALM = os.environ.get("REALM", "local")
ROOT_URL = os.environ.get("ROOT_URL", "http://localhost:4000")
PORT_NUMBER = os.environ.get("PORT", 4000)
FLASK_SESSION_SECRET_KEY = os.environ.get("SESSION_SECRET_KEY", "N1BKhJLnBqLpexOZdklsfDKFJDKFadsfs9a3r324YB7B73AglRmrHMDQ9RhXz35")
TEMPLATES_PATH = os.environ.get("TEMPLATES_PATH", "templates")

BIN_TTL = 48*3600
MAX_RAW_SIZE = 1024*10
IGNORE_HEADERS = []
MAX_REQUESTS = 20
CLEANUP_INTERVAL = 3600

# or "requestbin.storage.memory.MemoryStorage"
STORAGE_BACKEND = os.environ.get("STORAGE_BACKEND",  "requestbin.storage.redis.RedisStorage")

if STORAGE_BACKEND == "requestbin.storage.redis.RedisStorage":
    REDIS_URL = os.environ.get("REDIS_URL")

    url_parts = urlparse.urlparse(REDIS_URL)
    REDIS_HOST = url_parts.hostname
    REDIS_PORT = url_parts.port
    REDIS_PASSWORD = url_parts.password
    REDIS_DB = url_parts.fragment
    REDIS_PREFIX = os.environ.get("REDIS_PREFIX", "requestbin")

BUGSNAG_KEY = os.environ.get("BUGSNAG_KEY")

IGNORE_HEADERS = """
X-Varnish
X-Forwarded-For
X-Heroku-Dynos-In-Use
X-Request-Start
X-Heroku-Queue-Wait-Time
X-Heroku-Queue-Depth
X-Real-Ip
X-Forwarded-Proto
X-Via
X-Forwarded-Port
""".split("\n")[1:-1]
