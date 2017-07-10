import re

def spongebob(s):
	cap = [False]
	def repl(m):
		cap[0] = not cap[0]
		return m.group(0).upper() if cap[0] else m.group(0).lower()

	return re.sub(r'[A-Za-z]', repl, s)

print spongebob(raw_input("Enter message: "))
