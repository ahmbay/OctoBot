import time

from config.cst import *
from bot import Crypto_Bot


def test_create_bot():
    # launch a bot
    bot = Crypto_Bot()
    bot.stop_threads()


def test_run_bot():
    # launch a bot
    bot = Crypto_Bot()
    bot.set_time_frames[TimeFrames.ONE_MINUTE]
    bot.create_exchange_traders()
    bot.create_evaluation_threads()
    bot.start_threads()

    # let it run 2 minutes: test will fail if an exception is raised
    time.sleep(2)

    # stop the bot
    bot.stop_threads()
