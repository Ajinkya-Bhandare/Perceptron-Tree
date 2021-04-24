def msb(x):
	r = 0
	while (x>>1):
		r+=1
		x = x>>1
	return r

def log(y):
	if y>1:
			#	Refernce :
		#	https:#stackoverflow.com/questions/9799041/efficient-implementation-of-natural-logarithm-ln-and-exponentiation

	    log2 = msb(int(y))
	    divisor = (float)(1 << log2)
	    x = y / divisor

	    result = -1.7417939 + (2.8212026 + (-1.4699568 + (0.44717955 - 0.056570851 * x) * x) * x) * x
	    #cout<<result<<","<<log2<<endl;
	    result += (float(log2)) * 0.69314718; # ln(2) = 0.69314718
	    # print(divisor,log2,result,y,x)
	    return result
	else:
		return -log(1/y)