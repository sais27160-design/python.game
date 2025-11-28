import logging
from logging.handlers import RotatingFileHandler
import json
import os
from functools import wraps

#logging
logger = logging.getLogger("tictactoe_logger")
logger.setLevel(logging.INFO)
os.makedirs("logs", exist_ok=True)
handler = RotatingFileHandler("logs/app.log", mode = 'a')
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

#log move 
def log_move(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"{func.__name__} called with args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

#state
os.makedirs("data", exist_ok=True)
STATS_FILE = "data/stats.json"

def save_stats(stats):
    os.makedirs("data", exist_ok=True)
    with open(STATS_FILE, "w") as f:
        json.dump(stats, f)
    logger.info(f"Saved stats: {stats}")