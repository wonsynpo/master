varA=input()
varB=int(input())
# print(type(varA)==str)
# type(varA)==str 这样比较
if type(varA)==type('a') or type(varB)==type('a'):
    print("string involved")
elif varA>varB:
    print("bigger")
elif varA==varB:
		print('equal')
else:
		print('smaller')