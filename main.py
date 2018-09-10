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
	if (len(arr) <= 1):
		return arr
	pointer = int(len(arr) / 2)
	left = mergeSort(arr[0:pointer])
	right = mergeSort(arr[pointer:len(arr)])
	joined = merge(left,right)
	return joined

print(mergeSort([52,26,93,17,77,31,44,55,20]));