# 1a finished
def decimals(n):
	temp = list(divmod(10,n))
	yield temp[0]
	while temp[1]:
		temp = list(divmod(temp[1]*10,n))
		yield temp[0]
	return
# 1b finished
def genlimit(g, limit):
    for i in range(limit):
        yield next(g)
# 2 finished
def decimals2(n):
	remainder = 1
	record1 = [0]
	record2 = [1]
	while remainder != 0:
		remainder *= 10
		num = remainder//n
		yield num
		record1.append(num)
		remainder = remainder - num * n
		record2.append(remainder)
		for i in range(len(record2)):
			for j in range(i+1, len(record2)):
				if record2[i] == record2[j]:
					if remainder == 0:
						break
					else:
						num2 = (10 * remainder) // n
						remainder *= 10
						yield record1[(i+1):len(record2)]
						return
		
		
				
	
    
# 3a finished
def select(l, selectors):
	result = []
	for i in l:
		if selectors[i]:
			result.append(l[i])
	return result

# 3b finished
def nbitIntToDigits(i, n):
    result=[]
    count = 0
    while i > 0:
        result.append(i&1)
        i = i // 2
        count += 1
    if count < n:
        for i in range(n - count):
            result.append(0)
    return result[::-1]
        
# 3c finished
def powerSet(l):
	result = []
	def powerset(l):
		if len(l) > 0:
			head = l[0]
			for tail in powerSet(l[1:]):
				yield [head] + tail
				yield tail
		else:
			yield []
	for item in powerset(l):
		result.append(item)
	return result
# 4 finished
# when testing this function, change the path to your own file path
def oil(path):
	f = open(path)
	count = 1
	data = []
	leftside = True
	for i in range(7):
		next(f)
	while True:
			data = []
			x = next(f)
			years = x.split()
			for n in f:
				temp = n.split()
				data.append(temp)
				if not (count % 13):
					break
				count += 1
			count += 1
			if len(years)==0:
				return
			yield report(years, data, leftside)
			yield report(years, data, not leftside)

		
	

def report(years, data, leftside):
	price = []
    if leftside:
		year = years[0]
		total = data[0][1]
		for i in range(1,len(data)):
			price.append(float(data[i][5]))
		mean = sum(price)/float(len(data)-1)
		maxPrice = float(max(price))
		minPrice = float(min(price))
	else:
		year = years[1]
		total = data[0][8]
		for i in range(1,len(data)):
			price.append(float(data[i][12]))
		mean = sum(price)/float(len(data)-1)
		maxPrice = max(price)
		minPrice = min(price)
	return year + ": quan: total=" + total + " prices: max = " + str(maxPrice) + " min = " + str(minPrice) + " avg = " + str(mean)


# 5a finished
def countBases(dna):
    result = []
    counta = 0
    countc = 0
    countg = 0
    countt = 0
    for i in range(len(dna)):
        if dna[i] == 'A':
            counta += 1
        elif dna[i] == 'C':
            countc += 1
        elif dna[i] == 'G':
            countg += 1
        elif dna[i] == 'T':
            countt += 1
    result = [counta, countc, countg, countt]
    return result
# 5b finished
def reverseComplement(dna):
    result = ''
    for i in range(len(dna)):
        if dna[i] == 'A':
            result += 'T'
        elif dna[i] == 'C':
            result += 'G'
        elif dna[i] == 'G':
            result += 'C'
        elif dna[i] == 'T':
            result += 'A'
    return result[::-1]

