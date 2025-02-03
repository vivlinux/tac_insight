import os
import logging
from dotenv import load_dotenv
load_dotenv()

from insight_src.bot.webexBot import runnableBot

logger = logging.getLogger(__name__)
if __name__ == "__main__":
    bot = runnableBot()
    bot.run()

