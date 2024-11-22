from arbitrage_bot.config import load_config
from arbitrage_bot.utils import setup_logging
from arbitrage_bot.arbitrage_bot import EnhancedArbitrageBot
import asyncio

if __name__ == "__main__":

    config = load_config()
    
    logger = setup_logging(config)
    
    bot = EnhancedArbitrageBot(config, logger)
    asyncio.run(bot.monitor_opportunities())
