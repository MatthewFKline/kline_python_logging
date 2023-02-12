import logging
import logging.handlers
import sys
import colorama

# LOGGING_LEVEL = logging.DEBUG
LOGGING_LEVEL = logging.INFO
# LOGGING_LEVEL = logging.WARNING
# LOGGING_LEVEL = logging.ERROR
# LOGGING_LEVEL = logging.CRITICAL

COLOR_LEVEL_DICT = {
    10: colorama.Fore.BLUE,
    20: colorama.Fore.GREEN,
    30: colorama.Fore.YELLOW,
    40: colorama.Fore.RED,
    50: colorama.Fore.MAGENTA,
}

FIRST_IMPORT = True  # Mutation?  Never heard of it, sounds scary.

PYCHARM_FULL_PATH_LINKS = False
COLOR = True
BLOCK = False
THREAD = False
ROLLING = True
BACKUP_LOG_COUNT = 10

LOG_NAME = 'file.log'


def _generate_format():
    # TODO: Simplify the decision tree as much as possible
    format_string = ""

    if BLOCK:
        format_string += "=" * 100 + "\n"

    if THREAD:
        if PYCHARM_FULL_PATH_LINKS:
            format_string += f"%(levelname)-10s %(funcName)-20s || T:%(thread)-5d-%(threadName)s || %(message)-30s || %(asctime)s\n"
            format_string += f"%(pathname)s:%(lineno)d"
        else:
            format_string += f"%(levelname)-10s %(funcName)-20s || T:%(thread)-5d-%(threadName)s || %(message)-30s || %(asctime)s"

    else:
        if PYCHARM_FULL_PATH_LINKS:
            format_string += f"%(levelname)-10s %(funcName)-20s || %(message)-30s || %(asctime)s\n"
            format_string += f"%(pathname)s:%(lineno)d"
        else:
            format_string += f"%(levelname)-10s %(funcName)-20s || %(message)-30s || %(asctime)s"

    if BLOCK:
        format_string += "\n" + "=" * 100

    return format_string


def init_logging(name):
    global FIRST_IMPORT

    class Custom_Formatter(logging.Formatter):
        def format(self, record):
            self.datefmt = "%H:%M:%S"

            format_string = _generate_format()

            if COLOR:
                self._style._fmt = COLOR_LEVEL_DICT[record.levelno] + format_string + colorama.Style.RESET_ALL
            else:
                self._style._fmt = format_string

            return logging.Formatter.format(self, record)

    logger = logging.getLogger(name)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(Custom_Formatter())
    logger.addHandler(handler)
    logger.setLevel(LOGGING_LEVEL)

    file_out = logging.handlers.RotatingFileHandler(LOG_NAME, backupCount=BACKUP_LOG_COUNT)  # THIS CREATES THE FILE
    if FIRST_IMPORT and ROLLING:
        file_out.doRollover()
    file_out.setFormatter(Custom_Formatter())
    logger.addHandler(file_out)
    FIRST_IMPORT = False
    return logger
