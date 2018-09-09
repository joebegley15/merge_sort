def merge(arrA,arrB):
	sorted = []
	while (len(arrA) and len(arrB)):
		if (arrA[0] < arrB[0]):
			sorted.append(arrA[0])
			del arrA[0]
		else:
			sorted.append(arrB[0])
			del arrB[0]			
	return sorted + arrA + arrB


def mergeSort(arr):
	if (arr.length <= 1):
		return arr
	pointer = math.floor(len(arr) / 2)

print(mergeSort([1,6,5,3,10,9,3,4,5,6,2,1,7,5,9,10]));