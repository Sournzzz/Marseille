import logging
from pprint import pprint

logger = logging.getLogger(__name__)

formatter = logging.Formatter(
    "{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)  # setFormatter is a method of handlers
console_handler.setLevel("DEBUG")

file_handler = logging.FileHandler("app.log", mode="a", encoding="utf-8")
file_handler.setFormatter(formatter)  # setFormatter has to be done for each handler
file_handler.setLevel("WARNING")


# Ways to set the custom logger level
logger.setLevel(10)
logger.setLevel("INFO")

# Adding the handlers
logger.addHandler(console_handler)
logger.addHandler(file_handler)

if __name__ == "__main__":
    pprint = lambda *args, **kwargs: None

    """
    Printing info about the logger, the default log level is 0, stands for NOTSET
    """
    pprint(f"Logger Level: {logger.level}")
    pprint(f"Logger info by printing the object: {logger}")
    pprint(f"Logger.parent: {logger.parent}")
    pprint(f"Logger, getting the real level: {logger.getEffectiveLevel()}")

    # Getting the handlers
    pprint(f"Logger handlers: {logger.handlers}")

    """
    Testing loggin 
    """
    print(file_handler.level)
    print(console_handler.level)
    logger.debug("debugging")
    logger.warning("warning")
    logger.error("error")
