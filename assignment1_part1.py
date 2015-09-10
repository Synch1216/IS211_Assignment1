__author__ = 'malcolmbarnes'
class ListDivideException(Exception):
	pass

def ListDivide(numbers, divide=2):
	answer= 0
	try:
		pass

	for num in numbers:
	if num % divide == 0:
		answer + 1



	except:
		raise ListDivideException

		return answer

		def testListDivide():
			try:
				pass
				ListDivide([1,2,3,4,5])
				ListDivide([2,4,6,8,10])
				ListDivide([30,54,63,98,100], divide=10)
				ListDivide([])
				ListDivide([1,2,3,4,5], 1)
			except Exception, e:
				raise ListDivideException

					testListDivide();
