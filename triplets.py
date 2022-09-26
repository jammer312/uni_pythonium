#!/usr/bin/env python3

def countTriplets(arr, a, b, c):
	counter = 0
	for i1, v1 in enumerate(arr):
		for i2, v2 in enumerate(arr[i1+1:]):
			if abs(v1 - v2) > a:
				continue
			for v3 in arr[i1+1+i2+1:]:
				if abs(v1 - v3) > c or abs(v2 - v3) > b:
					continue
				counter += 1
	return counter


arr = eval(input()) or []
a = eval(input()) or 0
b = eval(input()) or 0
c = eval(input()) or 0

print(countTriplets(arr, a, b, c))
