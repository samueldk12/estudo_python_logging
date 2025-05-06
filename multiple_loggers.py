import logging


## create a logger for module1
logger1 = logging.getLogger("module1")
logger1.setLevel(logging.DEBUG)

logger2 = logging.getLogger("module2")
logger2.setLevel(logging.WARNING)


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S'
)



## log essage with different loggers

logger1.debug("This is a debug for module 1")
logger2.warning("This is a warning message for module 2")
logger2.error("This is an error message")