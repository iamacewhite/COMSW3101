import itertools
import functools
import operator

# problem 1 finished
def los(s):
    strings = []
    for i in range(len(s)-1):
        strings.append([s[i]])
        for j in range(i,len(s)-1):
            if s[j] < s[j+1]:
                strings[i].append(s[j+1])
            else:
                break
    msize = 0
    for k in range(len(strings)-1):
        if len(strings[msize]) < len(strings[k+1]):
            msize = k+1
    return "".join(strings[msize])
            
# problem 2 finished
def c2f(tem):
    return (9*tem + 160) / 5

def f2c(tem):
    return (5*tem - 160) / 9

            
            
class Constraint:
    def __init__(self, name, coef, total):
        self.name = name
        name = name.split()
        self.names = []
        for i in range(len(name)):
            self.names.append([name[i]])
        self.coef = coef
        self.total = total
    def setvar(self, index, value):
        if isinstance(index, int):
            if len(self.names[index]) == 1:
                self.names[index].append(value)
            else:
                self.names[index][1] = value
        else:
            for j in range(len(self.names)):
                if self.names[j][0] == index:
                    index = j
                    if len(self.names[index]) == 1:
                        self.names[index].append(value)
                    else:
                        self.names[index][1] = value
        count = 0
        find = 0
        output = []
        for i in range(len(self.names)):
            if len(self.names[i]) == 1:
                count += 1
                find = i
        if count == 1:
            s = 0
            for i in range(len(self.coef)):
                if i == find:
                    continue
                else:
                    s += self.coef[i] * self.names[i][1]
            self.names[find].append((self.total-s)/self.coef[find])
            for i in range(len(self.names)):
                print(self.names[i][0], ' = ', float(self.names[i][1]))
                output.append(float(self.names[i][1]))
            if isinstance(self.name, str):
                self.name = self.name.split()
            self.names = []
            for i in range(len(self.name)):
                self.names.append([self.name[i]])
            return output
        else:
            return

# problem 3 finished
def mindot(v1, v2):
    result = []
    temp = itertools.permutations(v2)
    for item in temp:
        cal = 0
        for i in range(len(v1)):
            cal += v1[i] * item[i]
        result.append(cal)
    return min(result)

# problem 4 finished
def pickitems(price, cash):
    for n in range(len(price)):
        temp = itertools.permutations(price, n+1)
        for item in temp:
            cal = 0
            for i in range(len(item)):
                cal += item[i]
                if cal == cash:
                    return item[:i+1]

# problem 5 finished
class secure(object):
    def __init__(self, f):
        self.f = f
    def __call__(self, user, password, *pos, **kw):
        if not user in up:
            raise Exception('User %s not registered' % user)
        if password != up[user]:
            raise Exception("Bad password")
        val = self.f(*pos, **kw)
        return val
        
