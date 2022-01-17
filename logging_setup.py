import logging
import sys

LOGGING_LEVEL = logging.DEBUG
# LOGGING_LEVEL = logging.INFO
# LOGGING_LEVEL = logging.WARNING
# LOGGING_LEVEL = logging.ERROR
# LOGGING_LEVEL = logging.CRITICAL


def header():
    logging.getLogger().critical("=" * 95)
    logging.getLogger().critical(" " * 39 + "STARTING LOGGING")
    logging.getLogger().critical("=" * 95)
    logging.getLogger().critical("| SEVERITY:    MODULE    LINE:           FUNCTION ||             MESSAGE            ||  TIME  |")
    logging.getLogger().critical("-" * 95)


def init_logging_simple(name):
    logging.basicConfig(level=LOGGING_LEVEL,
                        format="%(levelname)10s: %(module)12s %(lineno)3d:%(funcName)20s || %(message)30s || %(asctime)s",
                        datefmt = "%H:%M:%S")
    log = logging.getLogger(name)
    log.setLevel(LOGGING_LEVEL)
    return logging.getLogger(name)


def init_logging(name, complex=False):
    if not complex:
        header()
        return init_logging_simple(name)
    else:
        try:
            import colorama
        except ModuleNotFoundError as e:
            logging.getLogger().critical("=" * 80)
            logging.error(str(e))
            logging.warning("COULD NOT IMPORT COLORAMA, LOGGING FORMATTING WILL BREAK")
            logging.warning("Please set 'complex' to 'False' to restore proper formatting")
            logging.getLogger().critical("=" * 80)
            return init_logging_simple(name)

        class Kline_Formatter(logging.Formatter):
            def format(self, record):
                self.datefmt = "%H:%M:%S"
                format_string = "%(levelname)10s: %(module)12s %(lineno)3d:%(funcName)20s || %(message)30s || %(asctime)s"
                if record.levelno == logging.DEBUG:
                    self._style._fmt = colorama.Fore.BLUE + format_string + colorama.Style.RESET_ALL
                elif record.levelno == logging.INFO:
                    self._style._fmt = colorama.Fore.GREEN + format_string + colorama.Style.RESET_ALL
                elif record.levelno == logging.WARNING:
                    self._style._fmt = colorama.Fore.YELLOW + format_string + colorama.Style.RESET_ALL
                elif record.levelno == logging.ERROR:
                    self._style._fmt = colorama.Fore.RED + format_string + colorama.Style.RESET_ALL
                elif record.levelno == logging.CRITICAL:
                    self._style._fmt = colorama.Fore.MAGENTA + format_string + colorama.Style.RESET_ALL
                return logging.Formatter.format(self, record)

        def init_logging_complex(name):
            logger = logging.getLogger(name)
            handler = logging.StreamHandler(sys.stdout)
            handler.setFormatter(Kline_Formatter())
            logger.addHandler(handler)
            logger.setLevel(LOGGING_LEVEL)
            return logger

        header()
        return init_logging_complex(name)
