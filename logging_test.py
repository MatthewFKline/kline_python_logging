import logging_setup
import submodules_folder.submodule_one
import submodules_folder.submodule_two
log = logging_setup.init_logging(__name__)


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


# log_tests()

submodules_folder.submodule_one.log_sub_one()
submodules_folder.submodule_two.log_sub_two()
