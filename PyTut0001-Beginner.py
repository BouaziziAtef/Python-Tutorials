print('\t\t *******************************')
print('\t\t **    Python-Tutorial0001    **')
print('\t\t **===========================**')
print('\t\t ** Developer : BOUAZIZI ATEF **')
print('\t\t ** BOUAZIZI-ATEF@OUTLOOK.COM **')
print('\t\t *******************************')
#------------------------------------------------
input('\n Press enter to continue...')
#------------------------------------------------
x=float(input('Enter value 1 : '))
y=float(input('Enter value 2 : '))
print('Value 1 = ',x, '& Value 2 = ',y)
if x == y :
	print('Value 1 : ',x, ' equal to value 2 : ',y)
elif x > y :
	print('Value 1 : ',x, " greater than value 2 : ",y)
else :
	print('Value 1 : ',x, " less than value 2 : ",y)
#------------------------------------------------
print('\n')
print('Value 1 + Value 2 = ', x+y)
print('Value 1 - Value 2 = ', x-y)
print('Value 1 * Value 2 = ', x*y)
print('Value 1 / Value 2 = ', x/y)
print('Value 1 // Value 2 = ', x//y)
#------------------------------------------------
input('\n Press enter to continue...')
#------------------------------------------------
n=str(input('Enter your name : '))
a=int(input('Enter your age : '))

print('\n')
print('Value 1 = ',x, ', Type : ', type(x))
print('Value 2 = ',y, ', Type : ', type(y))
print('Your name = ',n, ', Type : ', type(n))
print('Your age = ',a, ', Type : ', type(a))
#------------------------------------------------
input('\n Press enter to continue...')
#------------------------------------------------
print('\n')
for i in range(10):
	print('2 x ',i,' = ', 2 * i)

print('\n')
for i in range(5,10):
	print('2 x ',i,' = ', 2 * i)

print('\n')
for i in range(10):
	print(i,' x ',i,' = ', i * i)

print('\n')
for i in range(10):
	print(i+1,' x ',i,' = ', i+1 * i)

print('\n')
for i in range(10):
	if i != 0 :
		print('---------------')
	for j in range(10):
		print(j,' x ',i,' = ', j * i)
#------------------------------------------------
input('\n Press enter to continue...')
#------------------------------------------------
r=[10,20,30,40]
f=["BOUAZIZI","BEJAOUI","TEFFEHI"]

print('Value liste 1 = ',r, ', Type : ', type(r))
print('Value liste 2 = ',f, ', Type : ', type(f))

print('\n')
print('lenght liste 1 = ',len(r))
print('lenght liste 2 = ',len(f))

print('\n')
for i in r:
	print(i)

print('\n')
for i in f:
	print(i)

print('\n')
for i in [20,40,60,80,100]:
	print(i)

print('\n')
for i in [20,40,60,80,100]:
	print('---------------')
	for j in r:
		print(j,' x ',i,' = ', j * i)

print('\n')
i=0
while i<len(f):
	print('Value',i +1 , 'de liste 1 ==> ', f[i])
	i=i+1
#------------------------------------------------
print('\n')

input('Press enter to exit!..')
