from random import randint

def quickMath():
	m1 = randint(0, 16)
	m2 = randint(0, 16)
	symbol = randint(0,2)
	if symbol == 0:
		answer = int(input(str(m1) + " - " + str(m2) + "\n"))
		c_answer = m1-m2
		if answer == c_answer:
			print("Correct\n")
			quickMath()
		else:
			print("Wrong")
			for a in range(5):
				answer = int(input())
				if answer == c_answer:
					print("Correct\n")
					quickMath()
				else:
					print("Wrong\n")
			quickMath()
	elif symbol == 1:
		answer = int(input(str(m1) + " * " + str(m2) + "\n"))
		c_answer = m1*m2
		if answer == c_answer:
			print("Correct\n")
			quickMath()
		else:
			print("Wrong")
			for a in range(5):
				answer = int(input())
				if answer == c_answer:
					print("Correct\n")
					quickMath()
				else:
					print("Wrong\n")
			quickMath()
	elif symbol == 2:
		answer = int(input(str(m1) + " + " + str(m2) + "\n"))
		c_answer = m1+m2
		if answer == c_answer:
			print("Correct\n")
			quickMath()
		else:
			print("Wrong")
			for a in range(5):
				answer = int(input())
				if answer == c_answer:
					print("Correct\n")
					quickMath()
				else:
					print("Wrong\n")
			quickMath()


quickMath()