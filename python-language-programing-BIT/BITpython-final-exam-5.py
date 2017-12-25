'''
"3位水仙花数"是指一个三位整数，
其各位数字的3次方和等于该数本身。
例如：ABC是一个"3位水仙花数"，则：A的3次方＋B的3次方＋C的3次方 = ABC。

请按照从小到大的顺序输出所有的3位水仙花数，请用"逗号"分隔输出结果。
'''

a=b=c=0
rel=""
for v in range(100,1000):
	a=v//100
	b=v//10%10
	c=v%10
	if v==a**3+b**3+c**3:
		rel+=str(v)
		rel+=','
print(rel[:-1])

