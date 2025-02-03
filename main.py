import os
import logging
import sys

from dotenv import load_dotenv
load_dotenv()

from insight_src.bot.webexBot import runnableBot

logger = logging.getLogger(__name__)
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--openai_key", help="Pass a value to openai_key")
    args = parser.parse_args()

    if args.openai_key:
        print(f"openai_key: {args.openai_key}")
        os.environ["LLM_PROXY_API_KEY"] = args.openai_key
    else:
        print("openai_key is not set.")
        pass

if __name__ == "__main__":
    main()
    bot = runnableBot()
    bot.run()

