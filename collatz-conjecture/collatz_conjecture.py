def steps(number):
	
	n=0    	

	if number < 1:
		raise ValueError('Value is less than 1')
	
	while number !=1:
		if number%2==0:
			number /= 2
			n +=1
		else:
			number = 3*number +1
			n +=1
	
	return n