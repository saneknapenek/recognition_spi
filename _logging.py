import logging
import os
from datetime import datetime

import coloredlogs



if not os.path.exists("logs/"):
    os.makedirs("logs/")
logging.basicConfig(level=logging.INFO, filename=f"logs/{datetime.now().date()}.log", filemode="w",
                    format="%(asctime)s %(message)s")
logger = logging.getLogger(__name__)
coloredlogs.install(level='INFO', fmt='%(asctime)s %(message)s', logger=logger)