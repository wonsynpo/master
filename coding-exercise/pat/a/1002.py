'''
1002. A+B for Polynomials (25)

时间限制
400 ms
内存限制
65536 kB
代码长度限制
16000 B
判题程序
Standard
作者
CHEN, Yue
This time, you are supposed to find A+B where A and B are two polynomials.

Input

Each input file contains one test case. Each case occupies 2 lines, and each line contains the information of a polynomial: K N1 aN1 N2 aN2 ... NK aNK, where K is the number of nonzero terms in the polynomial, Ni and aNi (i=1, 2, ..., K) are the exponents and coefficients, respectively. It is given that 1 <= K <= 10，0 <= NK < ... < N2 < N1 <=1000.

Output

For each test case you should output the sum of A and B in one line, with the same format as the input. Notice that there must be NO extra space at the end of each line. Please be accurate to 1 decimal place.

Sample Input
2 1 2.4 0 3.2
2 2 1.5 1 0.5
Sample Output
3 2 1.5 1 2.9 0 3.2
'''
line1_lst=input().split()
line2_lst=input().split()
# print(line1_lst)
rel=[]
for i in range(1,len(line1_lst),2):
	rel.append({line1_lst[i]:line1_lst[i+1]})
# print(rel)


for j in range(1,len(line2_lst),2):
	exitorNot=False
	for i in range(len(rel)):
		if line2_lst[j] in rel[i]:
			# print("line2_lst[j],rel[i]",line2_lst[j],rel[i])
			# print(rel[i][line2_lst[j]],type(rel[i][line2_lst[j]]))
			# print(line2_lst[j+1],type(line2_lst[j+1]))

			rel[i][line2_lst[j]]=str(eval(rel[i][line2_lst[j]])+eval(line2_lst[j+1]))
			# rel[i][line2_lst[j]]=eval(rel[i][line1_lst[j]])+eval('3')
			# print(rel)
			exitorNot=True
			break
	if not exitorNot:
		rel.append({line2_lst[j]:line2_lst[j+1]})
# print(rel)
# 字典之间是无序的
keys=[]
for v in rel:
	for k in v.keys():
		keys.append(k)
keys=sorted(keys,reverse=True)
# print(keys)

print(len(keys),'',end='')

for k in keys[:-1]:
	for v in rel:
		# print(v)
		if k in v:
			print(k,v[k],'',end='')
			break
print(keys[-1],'',end='')
for v in rel:
	if keys[-1] in v:
		print(v[keys[-1]])



