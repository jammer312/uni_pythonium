#!/usr/bin/env python3

import time

class MyTimer:
	def __init__(self, *, units):
		self.units = units

	def __enter__(self):
		self.enterTime = time.perf_counter()
		return self

	def __exit__(self, exc_type, exc_value, exc_tb):
		self.exitTime = time.perf_counter()

	def elapsed_time(self):
		ret = self.exitTime - self.enterTime
		if self.units == "h":
			return ret / 60 / 60
		if self.units == "m":
			return ret / 60
		if self.units == "s":
			return ret
		return 42

with MyTimer(units="m") as t:
	print("Hello world")

print(t.elapsed_time())
