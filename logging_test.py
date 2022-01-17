import logging_setup

log = logging_setup.init_logging(__name__, complex=True)

log.debug("DEBUG TEXT HERE")
log.info("INFO TEXT HERE")
log.warning("WARNING TEXT HERE")
log.error("ERROR TEXT HERE")
log.fatal("FATAL TEXT HERE")


def log_tests():
    log.debug("DEBUG TEXT HERE")
    log.info("INFO TEXT HERE")
    log.warning("WARNING TEXT HERE")
    log.error("ERROR TEXT HERE")
    log.fatal("FATAL TEXT HERE")


log_tests()
