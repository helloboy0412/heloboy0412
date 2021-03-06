#Ex1
import random
def ex1a(n):
	count = 0 
	for i in range (n):
		if random.randint(1,6) == random.randint(1,6):
			count += 1
	return(count/n)	
			
def ex1b(n):
	count = 0  
	for i in range (n):
		if random.randint(1,6) != random.randint(1,6):
			count += 1
	return(count/n)

def ex1c(n):
	count = 0 
	for i in range (n):
		if random.randint(1,6) % 2 == 0 and random.randint(1,6) % 2 == 0:
			count += 1
	return(count/n)

def ex1d(n):
	count = 0
	for i in range (n):
		if random.randint(1,6) % 2 != 0 and random.randint(1,6) % 2 != 0:
			count += 1
	return(count/n)

def ex1e(n):
	count = 0
	for i in range (n):
		if (random.randint(1,6) + random.randint(1,6)) % 2 != 0:
			count += 1
	return(count/n)

def ex1f(n):
	count = 0
	for i in range (n):
		if random.randint(1,6) == random.randint(1,6) == 6:
			count += 1
	return(count/n)

def ex1g(n):
	count = 0 
	for i in range (n):
		if (random.randint(1,6) + random.randint(1,6)) > 10:
			count += 1
	return count/n

#Ex2
def cross(A,B):
	return {a+b for a in A for b in B }
urn = cross('R','123') | cross('B','12') | cross('W','12345')

def ex2a(n):
	count = 0
	for i in range (n):
		res = {i[0] for i in random.sample(urn,3)}
		if len(res) == 1:
			count += 1
	return count/n

def ex2b(n):
	count = 0
	for i in range (n):
		res = {i[0] for i in random.sample(urn,3)}
		if len(res) == 3:
			count += 1
	return count/n

def ex2c(n):
	count = 0
	for i in range (n):
		res = {i[0] for i in random.sample(urn,3)}
		if len(res) == 2:
			count += 1
	return count/n

def ex2d(n):
	count = 0
	for i in range (n):
		res = [i[0] for i in random.sample(urn,3)]
		if res.count('R') == 2 and res.count('W') == 1:
			count += 1
	return count/n

def ex2e(n):
	count = 0
	for i in range (n):
		res = random.sample(urn,3)
		res1 = [i[0] for i in res]

		if res1.count('W') == 3:
			count += 1
			print (res)
	return count/n

#Ex3
def cross(A,B):
	return {a + b for a in A for b in B}
deck = cross('1234567890JQK','????????????')

def ex3a(n):
	count = 0
	for i in range (n):
		res = {i[1] for i in random.sample(deck,4)}
		if len(res) == 1:
			count += 1
	return count/n

def ex3b(n):
	count = 0
	for i in range (n):
		res = {i[1] for i in random.sample(deck,4)}
		if len(res) == 4:
			count += 4
	return count/n

def ex3c(n):
	count = 0 
	for i in range (n):
		res = [i[1] for i in random.sample(deck,4)]
		if (res.count('???') + res.count('???') == 4) or (res.count('???')+res.count('???') == 4):
			count += 4
	return count/n

def ex3d(n):
	count = 0
	for i in range (n):
		res = {i[0] for i in random.sample(deck,4)}
		if len(res) == 1:
			count += 1
			print (res)
	return count/n

def ex3e(n):
	count = n
	for i in range (n):
		res = [i[0] for i in random.sample(deck,4)]
		if (res.count('K') + res.count('Q') + res.count('J') > 0):
			count -= 1
	return count/n

def ex3f(n):
	count = 0
	for i in range (n):
		res = [i[0] for i in random.sample(deck,4)]
		if (res.count('K') + res.count('Q') + res.count('J') == 4):
			count += 1
	return count/n

#Ex4
import itertools
def cross(A,B):
	return {a + b for a in A for b in B}
urn = cross('W','12') | cross('B','123') | cross('R','1234')

U3 = list(itertools.combinations(urn,3))

W = cross('W','12')
B =  cross('B','123')
R = cross('R','1234')
WB = cross(W,B)
WBR = cross(WB,R)

P = len(WBR)/len(U3)

#Ex5a
Rank = {2,3,4,5,6,7,8,9,10,11,12,13,14}
Suits = {'???','???','???','???'}
Deck = list(itertools.product(Rank, Suits))

U5 = list(itertools.combinations(Deck,5))
straight = []
Count = 0
for H5 in U5:
	Values = []
	for Card in H5:
		Values.append(Card[0])
	if (max(Values) - min(Values) == 4 and len(set(Values)) == 5):
	 	Count +=1
	if sum(Values)==28 and len(set(Values))==5 and max(Values)==14:
		Count +=1

#Ex5b
Rank = {2,3,4,5,6,7,8,9,10,11,12,13,14}
Suits = {'???','???','???','???'}
Deck = list(itertools.product(Rank,Suits))

def Ex5b(n):
	count = 0
	for i in range (n):
		a = random.sample(Deck,5)
		Values = [i[0] for i in a]
		if (max(Values) - min(Values) == 4 and len(set(Values)) == 5):
			count += 1
		 
			count += 1
	return count/n

#Ex6a
E={0,1,2,3,4,5}
A={1,2,3,4,5}
def cross(A,B,C):
	return [a+b+c for a in A for b in B for c in C]
Ex6a = cross('12345','012345','012345')

#Ex6b
B = list(itertools.permutations(E,4))
H =[]
for i in B:
	if i[0] != 0:
		H.append(str(i[0])+str(i[1])+str(i[2])+str(3))


				






