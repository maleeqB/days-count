import sys,datetime
def mab(Y,M,D):
	n=datetime.datetime.now()
	b=datetime.datetime(Y,M,D)
	g=n-b
	print(str(g))
Y=int(sys.argv[1])
M=int(sys.argv[2])
D=int(sys.argv[3])
mab(Y,M,D)
