#/bin/env python3
lss = ['a','b','c',]

def tq(ls):
	book = []
	for i in range(len(ls)):
		book.append(1)
	box = []
	for i in range(len(ls)):
		box.append(0)
	def enum(step):
		if step == len(ls)+1:
			print(box)
			return
		for i in range(len(ls)):
			if book[i] == 1:
				box[step-1] = ls[i]
				book[i] = 0
				enum(step+1)
				book[i] = 1
	enum(1)

tq(lss)
