#!/usr/bin/env python3

import heapq

class MedianFinder:
	def __init__(self):
		self.top = []
		self.bottom = []

	def addNum(self, num):
		if len(self.top) > len(self.bottom):
			num = heapq.heappushpop(self.top, num)
			heapq.heappush(self.bottom, -num)
		else:
			num = -heapq.heappushpop(self.bottom, -num)
			heapq.heappush(self.top, num)

	def findMedian(self):
		if len(self.top) == 0:
			return 0
		elif len(self.top) > len(self.bottom):
			return self.top[0]
		else:
			return (self.top[0] - self.bottom[0]) / 2

median_finder = MedianFinder()
assert median_finder.findMedian() == .0
median_finder.addNum(1)
median_finder.addNum(2)
assert median_finder.findMedian() == 1.5
median_finder.addNum(3)
assert median_finder.findMedian() == 2
