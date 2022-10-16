import logging_setup

log = logging_setup.init_logging(__name__)

def log_sub_one():
    log.debug('SUBMODULE DEBUG TEXT')