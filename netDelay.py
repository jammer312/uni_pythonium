#!/usr/bin/env python3

from collections import deque

class node:
	def __init__(self, index):
		self.index = index
		self.paths = {}

def calculateDelay(*, times, N, X):
	nodeMap = dict()
	for src, dst, delay in times:
		srcNode = nodeMap.get(src, node(src))
		srcNode.paths[dst] = min(delay, srcNode.paths.get(dst, delay))
		nodeMap[src] = srcNode
	reachedNodes = dict()
	reachedNodes[X] = 0
	processQueue = deque()

	processNodesSet = {X}
	processQueue.append(X)

	while len(processQueue):
		src = processQueue.popleft()
		processNodesSet -= {src}
		for dst, delay in nodeMap.get(src, node(src)).paths.items():
			pathDelay = reachedNodes[src] + delay
			if dst in reachedNodes and reachedNodes[dst] <= pathDelay:
				continue
			reachedNodes[dst] = pathDelay
			if dst not in processNodesSet:
				processNodesSet |= {dst}
				processQueue.append(dst)

	if len(reachedNodes) != N:
		return - 1
	return max(reachedNodes.values())

print(calculateDelay(times=[(2,1,1),(2,3,1),(3,4,1)], N=4, X=2))
print(calculateDelay(times=[(1,2,1)], N=2, X=2))
