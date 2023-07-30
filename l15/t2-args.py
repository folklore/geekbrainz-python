import argparse
from t2 import NewYearThree


parser = argparse.ArgumentParser(description='Елочка гори!')

parser.add_argument('-l', metavar='l', type=int, help='Высота елки', default=NewYearThree.DEFAULT_HEIGHT)
parser.add_argument('-s', metavar='s', type=str, help='Символ вывода', default=NewYearThree.DEFAULT_SYMBOL)

args = parser.parse_args()


morpher = NewYearThree(args.l, args.s)
print(morpher.draw())
