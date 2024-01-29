import argparse

parser = argparse.ArgumentParser(prog="computer_hardware", description=f"A system which prints the user's computer hardware details")
parser.add_argument('-s', dest='size', type=str, default="GB", help='type of size to show on the table. Options are: BYTES, KB, MB, GB, TB')
parser.add_argument('-f', dest='find_device', type=str, default="Y", help='show device location: Y/N')
parser.add_argument('-d', dest='debug', type=str, help='For debugging')
args = parser.parse_args()
