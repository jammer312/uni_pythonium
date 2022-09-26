#!/usr/bin/env python3

from collections import deque

def validateParentheses(inputString, openersForClosers):
	openers = list(openersForClosers.values())
	stack = deque()
	head = None

	for char in inputString:
		wantedOpener = openersForClosers.get(char)
		if wantedOpener:
			if head != wantedOpener:
				return False
			if len(stack):
				head = stack.pop()
			else:
				head = None
		elif char in openers:
			if head:
				stack.append(head)
			head = char

	return not len(stack) and not head




openersForClosers = {
	')': '(',
	']': '[',
	'}': '{',
}
inputString = input()
print(validateParentheses(inputString, openersForClosers))
