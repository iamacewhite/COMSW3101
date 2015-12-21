import string
import pickle
import functools
import collections
import re
import urllib
import urllib.request
# problem 1a
def goodperm(obj):
	alphabet = string.ascii_lowercase
	if(obj.encode(alphabet) != obj.decode(alphabet)):
		return False
	return True

#problem 1b
def saveKey(path, key):
	if(goodperm(key)):
		f = open(path, 'wb')
		pickle.dump(key,f)
		f.close()
		return None
	else:
		raise Exception('Invalid Key')
# problem 2a
def encode(path, s):
	f = open(path, 'rb')
	d = pickle.load(f)
	f.close()
	return(d.encode(s))
	
def decode(path, s):
	f = open(path, 'rb')
	d = pickle.load(f)
	f.close()
	return(d.decode(s))

# problem 2b
class encrot():
	def __init__(self, rot):
		self.a = rot
	
	def encode(self,s):
		output = ""
		if self.a >= 0:
			self.a = self.a % 26
		else:
			self.a = 26 - (-1 * self.a) % 26
		temp = s[len(s)-self.a:]
		for i in range(self.a):
			output += temp[i]
		for i in range(len(s)-self.a):
			output += s[i]
		
		return(output)
	def decode(self, s):
		return(self.encode(s))
# problem 3
def actors2(url):
	line_count = 0
	speech_count = 0
	name = []
	count = []
	with urllib.request.urlopen(url) as ef:
		for bin in ef:
			s = bin.decode('utf-8')
			line_count += 1
			if s.find('NAME=speech') != -1:
				found = False
				speech_count += 1
				pos1 = s.find('<b>')
				pos2 = s.find('</b>', pos1 + 3)
				nam = s[pos1 + 3: pos2]
				i = 0
				for i in range(len(name)):
					if(name[i] == nam):
						found = True
						break
				if found:
					count[i] += 1
				else:
					name.append(nam)
					count.append(1)
	d = collections.defaultdict(int)
	for j in range(len(name)):
		d[name[j]] = count[j]
	return [line_count, speech_count, d]

# problem 4
class Interval:
	def __init__(self, imin, imax):
		self.imin = imin
		self.imax = imax
	def __add__(self, other):
		if isinstance(other, int):
			new_imin = self.imin + other
			new_imax = self.imax + other
		else:
			new_imin = self.imin + other.imin
			new_imax = self.imax + other.imax
		return Interval(new_imin, new_imax)
	def __repr__(self):
		return ('Interval<%d, %d>' % (self.imin, self.imax))
	def __mul__(self, other):
		if isinstance(other, int):
			new_imin = self.imin * other
			new_imax = self.imax * other
		else:
			new_imin = self.imin * other.imax
			new_imax = self.imax * other.imax
		return Interval(new_imin, new_imax)


# problem 5
class polylist:
	def __init__(self, coe):
		self.coe = coe
	def termString(self, c , e):
		cs = str(c)
		if c > 0:
			cs = '+ ' + cs
		if (e == 0):
			return(cs)
		if (e == 1):
			return('%s*X' % cs)
		return('%s*X**%d' % (cs,e))
	def __str__(self):
		terms = [self.termString(c,e)
			for e,c in enumerate(self.coe)
			if c != 0]
		terms.reverse()
		s = (' '.join(terms))
		return(s)
	def __repr__(self):
		return(self.__str__())
	def __len__(self):
		return(len(self.coe) - self.coe.count(0))
	def __add__(self, p2):
		p1len = len(self.coe)
		p2len = len(p2.coe)
		pad = p2len - p1len
		c1 = self.coe
		c2 = p2.coe
		if pad < 0:
			c1, c2 = c2, c1
			pad = -pad
		c1 = c1[:]
		c1.extend([0]*pad)
		return(poly([t1+t2 for t1,t2 in zip(c1,c2)]))
	__hash__ = None
	def evaluate(self, n):
		sum = 0
		for e,c in enumerate(self.coe):
			sum += c*n**e
		return(sum)
	def __mul__(self, p2):
		sums = []
		for e1,c1 in enumerate(self.coe):
			prod = [c1 * c2 for c2 in p2.coe]
			for rpt in range(e1):
				prod.insert(0, 0)
			sums.append(poly(prod))
		return(functools.reduce(poly.__add__, sums))

	def topolydict(self):
		d = {}
		i = 0
		for item in self.coe:
			d[i] = item
			i += 1
		pd = polydict(d)
		return pd






class polydict:
	def __init__(self, d={}):
		self.sparse = d.copy()
	def printTerm(self, c ,e):
		cs = str(c)
		if c > 0:
			cs = '+ ' + cs
		if (e == 0):
			return(cs)
		if (e == 1):
			return('%s*X' % cs)
		return('%s*X**%d' % (cs,e))
	def __str__(self):
		if len(self.sparse) == 0:
			return('0')
		terms = [self.printTerm(self.sparse[e],e)
			 for e in sorted(self.sparse.keys(),
					 reverse=True)
				 if self.sparse[e] != 0]
		s = ' '.join(terms)
		if '+' == s[0:2]:
			s = s[2:]
		return (s)
	def __repr__(self):
		return(self.__str__())
	__hash__ = None
	def __len__(self):
		return(len(self.sparse))
	def __bool__(self):
		return(False if len(self.sparse)==0 else True)
	def __iter__(self):
		return( (i for i in self.sparse.items() ))
	def __eq__(self, other):
		return(self.sparse == other.sparse)
	def __ne__(self, other):
		return(self.sparse != other.sparse)
	def __lt__(self, other):
		return(self.evaluate(1) < other.evaluate(1))
	def __le__(self, other):
		return(self.evaluate(1) <= other.evaluate(1))
	def __contains__(self, e):
		return(e in self.sparse)
	def evaluate(self, n):
		sum = 0
		for e in self.sparse.keys():
			sum += self.sparse[e]*n**e
		return(sum)
	def __add__(self, p2):
		n = self.sparse.copy()
		for k,v in p2.sparse.items():
			if None == n.get(k):
				n[k] = v
			else:
				n[k] += v
		return(polydict(n))
	def __getitem__(self, index):
		keys = sorted(self.sparse.keys(), reverse=True)
		if isinstance(index, int):
			inds = [index]
		if isinstance(index, slice):
			inds = range(*index.indices(len(keys)))
		d = {}
		for i in inds:
			e = keys[i]
			d[e] = self.sparse[e]
		return(polydict(d))
	def __rmul__(self, p2):
		if isinstance(p2, int):
			nd = {}
		for e,c in self.sparse.items():
			nd[e] = c * p2
		return(polydict(nd))
	def differentiate(self):
		d = {}
		for e,c in self.sparse.items():
			if e != 0:
				d[e-1] = c * e
		return(polydict(d))
	def integrate(self):
		d = {}
		for e,c in self.sparse.items():
			d[e+1] = c /(e+1.)
		return(polydict(d))
	def topolylist(self):
		l = []
		for key,value in self:
			l.append(value)
			if value < 0:
				raise ValueError;
		pl = polylist(l)
		return pl
