import logging

'''    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(name)s %(message)s"
    )

    log = logging.getLogger(__name__)

    logging.debug("debug")
    logging.critical("azazin creet")'''

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)

file = logging.FileHandler("app.log", "w", encoding="utf-8")
file.setLevel(logging.WARNING)

formatter = logging.Formatter(
    "%(asctime)s %(levelname)s %(name)s %(message)s, (%(filename)s : %(lineno)s)"
)

console.setFormatter(formatter)
file.setFormatter(formatter)

logger.addHandler(console)
logger.addHandler(file)

logger.debug("debug")
logger.error("3RR0R")

try:
    1 / 0
except ZeroDivisionError as e:
    #logger.exception(e)
    logger.warning("warning", exc_info=True)
