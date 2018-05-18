print('Countdown started') #You can edit this to display whatever text you want, even include strings using {} and .format()

import time
def countdown(m,s):
	i=m
	j=s
	k=0
	while True:
		if(j ==- 1):
			j = 59
			i -= 1
		if(j > 9):
			print(str(k)+str(i)+":"+str(j), end='\r') #Carriage return only works with python 3; end='\r' will not work with python 2.
		else:
			print(str(k)+str(i)+":"+str(k)+str(j), end='\r')
		time.sleep(1)
		j -= 1
		if(i == 0 and j == -1):
			break
	if(i == 0 and j == -1):
		print('Countdown ended') #You can edit this to display whatever text you want, even include strings using {} and .format()
		time.sleep(1)
countdown(1,0) #This is in (minutes, seconds) format, so change the values to increase or decrease the timer. (1,0) would be a 1 minute countdown, (0,5) would be a 5 second countdown, (5,10) would be a 5 minute 10 second countdown, etc.
