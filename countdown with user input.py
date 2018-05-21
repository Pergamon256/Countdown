import time

x = int(input("Enter countdown minutes: "))
y = int(input("Enter countdown seconds: "))

print('Countdown started') #You can edit this to display whatever text you want, even include strings using {} and .format()
def countdown(m,s):
	i=m
	j=s
	k=0
	try:
		while True:
			if(j == -1):
				j = 59
				i -= 1
			if((i > 9) and (j > 9)):
				print(str(i)+":"+str(j), end='\r') #Carriage return only works with python 3; end='\r' will not work with python 2.
			elif(i > 9):
				print(str(i)+":"+str(k)+str(j), end='\r')
			elif(j > 9):
				print(str(k)+str(i)+":"+str(j), end='\r')
			else:
				print(str(k)+str(i)+":"+str(k)+str(j), end='\r')								
			time.sleep(1)
			j -= 1
			if(i == 0 and j == -1):
				break
	except KeyboardInterrupt:
		pass
		print("", end='\r')
	if(i == 0 and j == -1):
		print('Countdown ended') #You can edit this to display whatever text you want, even include strings using {} and .format()
		time.sleep(1)

result = countdown(x,y)
countdown(result)