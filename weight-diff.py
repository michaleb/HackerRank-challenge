# Python program to print all subsets with given diff

# The vector v stores current subset.
def printAllSubsetsRec(arr, n, v, diff) :

	# If remaining diff is 0, then print all
	# elements of current subset.
	if (diff == 0) :
		for value in v :
			print(value, end=" ")
		print()
		return
	

	# If no remaining elements,
	if (n == 0):
		return

	# We consider two cases for every element.
	# a) We do not include last element.
	# b) We include last element in current subset.
	printAllSubsetsRec(arr, n - 1, v, diff)
	v1 = [] + v
	v1.append(arr[n - 1])
	printAllSubsetsRec(arr, n - 1, v1, diff - arr[n - 1])


# Wrapper over printAllSubsetsRec()
def printAllSubsets(arr, n, diff):

	v = []
	printAllSubsetsRec(arr, n, v, diff)


# Driver code

arr = [ 2, 5, 8, 4, 6, 11 ]
diff = 3
n = len(arr)
printAllSubsets(arr, n, diff)

# This code is contributed by ihritik
