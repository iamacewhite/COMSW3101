#Homework I
# 1a
def dp(x,y):
	total = 0
	x_new = x[0: min(len(x), len(y))]
	y_new = y[0: min(len(x), len(y))]
	for i,j in zip(x_new, y_new):
		total += i*j
	return total


# 1b
def shortlong(x, y):
	if len(x) > len(y):
		result = [y, len(y), x, len(x)]
	else:
		result = [x, len(x), y, len(y)]
	return result 

# 1c
def odp(x, y, n):
	total = 0
	input_list = shortlong(x,y)
	short = input_list[0]
	long = input_list[2]
	long_new = long[n:len(short)+n]
	for i, j in zip(short, long_new): 
		total += i*j
	return total 

# 1d
def pdp(x, y, n):
	total = 0
	list = shortlong(x, y)
	short = list[0]
	long = list[2]
	diff = len(long) - len(short)
	for i in range(diff):
		short.append(int(n))
		i += 1
	for i,j in zip(long, short):
		total += i*j
	return total

# 2
def rle(x):
	element = []
	number = []
	total = 0
	result = []
	for i in range(len(x)):
		if len(x) ==1:
			element.append(x[0])
			number.append(1)
		else:
			if i==0:
				element.append(x[0])
				total +=1
			else:
				if x[i] == x[i-1] and i != len(x) - 1:
					total += 1
				elif x[i] == x[i-1] and i == len(x) - 1:
					total += 1
					number.append(total)
				elif x[i] != x[i-1] and i == len(x) - 1:
					element.append(x[i])
					number.append(total)
					total = 1
					number.append(total)
				else:
					element.append(x[i])
					number.append(total)
					total = 1
	for j in range(len(element)):
		temp = [element[j], number[j]]
		result.append(temp)
	return result        

                                

# 3
def partition(l, n, overlap=0):
	result = []
	element_num = len(l) // (n - overlap)
	for i in range(element_num):
		if len(l[i*(n - overlap) : i*(n- overlap) + n]) == n:
			result.append(l[i*(n - overlap) : i*(n- overlap) + n])
			i += 1
		else:
			break
	return result 

# 4a
def expandlazy(x):
	if isinstance(x, zip) or isinstance(x, range) or isinstance(x,enumerate):
                                return list(x)
	else:
		return x


# 4b
def expandlazylist (new_list):
	final = list(map(expandlazy, new_list))
	return final 

# 5
def flatten(vector):
    result = []
    for item in vector:
        if not isinstance(item, list):
            result.append(item)
        else:
            for x in flatten(item):
                result.append(x)
    return result













                
