import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
file_handler = logging.FileHandler(r"C:\Users\nizan\Desktop\hardware_tester_tool\hardware_tester_tool.log", mode='w')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)