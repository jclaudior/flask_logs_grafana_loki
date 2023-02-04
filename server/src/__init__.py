
from flask import Flask
import logging
import logging_loki
logging_loki.emitter.LokiEmitter.level_tag = "level"
handler = logging_loki.LokiHandler(
   url="http://loki:3100/loki/api/v1/push",
   version="1",
)
logger = logging.getLogger("my-logger")
logger.setLevel(logging.DEBUG)

app = Flask(__name__)


from src.resources import *


