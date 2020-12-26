import datetime
import sys


def mab(y, m, d):
    n = datetime.datetime.now()
    b = datetime.datetime(y, m, d)
    g = n - b
    return str(g)


Y = int(sys.argv[1])
M = int(sys.argv[2])
D = int(sys.argv[3])

if __name__ == "__main__":
    print(mab(Y, M, D))
