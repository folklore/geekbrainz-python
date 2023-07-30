import argparse
from t1 import Morpher


parser = argparse.ArgumentParser(description='Перевод даты с бюрократического в календарную')

parser.add_argument('-a', metavar='a', type=str, help='Появление дня недели в месяце', default='')
parser.add_argument('-d', metavar='d', type=str, help='Название дня недели', default='')
parser.add_argument('-m', metavar='m', type=str, help='Название месяца', default='')

args = parser.parse_args()


morpher = Morpher(args.a, args.d, args.m)
print(morpher.date())
