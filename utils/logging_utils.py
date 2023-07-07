import logging


def setup_logging():
    logging.basicConfig(
        filename='app.log',
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
