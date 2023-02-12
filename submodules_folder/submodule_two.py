import logging_setup

log = logging_setup.init_logging(__name__)

def log_sub_two():
    log.debug('SUBMODULE DEBUG TEXT 2')