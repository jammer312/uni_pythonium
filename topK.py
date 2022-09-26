#!/usr/bin/env python3

def getTopK(arr, k):
	hashTable = {}
	for elem in arr:
		hashTable[elem] = hashTable.get(elem, 0) + 1
	if k >= len(hashTable):
		return list(hashTable.values())
	return sorted(hashTable.keys(), key=hashTable.get, reverse=True)[:k]

arr = eval(input())
k = eval(input())
print(getTopK(arr, k))
