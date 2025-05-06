import logging


## configuring logging 
logging.basicConfig(
    filename='app.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

## log messages
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is an logging warning")
logging.error("This is an error message")
logging.critical("This is a critical message")