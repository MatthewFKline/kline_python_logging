import logging
import sys
import colorama

LOGGING_LEVEL = logging.DEBUG


# LOGGING_LEVEL = logging.INFO
# LOGGING_LEVEL = logging.WARNING
# LOGGING_LEVEL = logging.ERROR
# LOGGING_LEVEL = logging.CRITICAL


def init_logging(name):
    class Kline_Formatter(logging.Formatter):
        def format(self, record):
            self.datefmt = "%H:%M:%S"
            format_string = "=" * 90 + "\n"
            format_string += f"%(levelname)-10s %(funcName)-20s || TID:%(thread)-5d || %(message)-30s || %(asctime)s\n"
            format_string += f"%(pathname)s:%(lineno)d\n"
            format_string += "=" * 90

            color_level_dict = {
                10: colorama.Fore.BLUE,
                20: colorama.Fore.GREEN,
                30: colorama.Fore.YELLOW,
                40: colorama.Fore.RED,
                50: colorama.Fore.MAGENTA,
            }

            self._style._fmt = color_level_dict[record.levelno] + format_string + colorama.Style.RESET_ALL

            return logging.Formatter.format(self, record)

    def init_logging_complex(name):
        logger = logging.getLogger(name)
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(Kline_Formatter())
        logger.addHandler(handler)
        logger.setLevel(LOGGING_LEVEL)
        return logger

    return init_logging_complex(name)
