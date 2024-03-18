import logger
import arg_parser

# GLOBAL VARIABLES
unit = "GB"
exponents_map = ['BYTES', 'KB', 'MB', 'GB', 'TB']


def check_argv():
    global unit, exponents_map
    arg_unit = arg_parser.args.size.upper()
    arg_debug = arg_parser.args.debug

    if arg_unit not in exponents_map:
        logger.logger.error("unit input is wrong! Must select from ['BYTES', 'KB', 'MB', 'GB', 'TB']")
    else:
        unit = arg_unit
    logger.logger.info("unit for displaying data in table: " + unit + ".")

    if arg_debug == 'd':
        logger.logger.setLevel(logger.logging.DEBUG)
    elif arg_debug:
        print("Argument typed for 'DEBUG' is wrong.")
