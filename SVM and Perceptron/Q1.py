# 获取数据
import glob
fcf = glob.glob('*.txt')
print(fcf[0])
f = open(fcf[0],'r')
tex1 = f.read()
print(tex1)
