import logging

logging.basicConfig(level=logging.INFO,
                    filename="logs.log",
                    filemode="w",
                    format="We have next logging message:%(asctime)s:%(levelname)s - %(message)s")

logging.info("info")

