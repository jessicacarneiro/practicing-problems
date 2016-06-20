'''
Find the difference between the sum of the squares of the first one hundred natural
numbers and the square of the sum.
'''

squareSum = 0
for i in range(1,101):
	squareSum = squareSum + i

squareSum = squareSum**2

sumOfSquares = 0
for i in range(1,101):
	sumOfSquares = sumOfSquares + i**2

print squareSum - sumOfSquares