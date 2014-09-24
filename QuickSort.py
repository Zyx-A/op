#!/usr/bin/python
def qsort(arr):
	if len(arr) <= 1:
		return arr
	else:
		piovt = arr[0]
		return qsort([x for x in arr[1:] if x <= piovt]) + \
		[piovt] + \
		qsort([x for x in arr[1:] if x > piovt])




a = [0,3,34,-5,23,2,3]
print qsort(a)
