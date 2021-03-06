function merge(arrA,arrB) {
	let singleSorted = [];
	while (arrA.length && arrB.length) {
		if (arrA[0] < arrB[0]) {
			singleSorted.push(arrA[0]);
			arrA.shift();
		} else {
			singleSorted.push(arrB[0]);
			arrB.shift();
		}
	}
	return singleSorted.concat(arrA,arrB);
}

function mergeSort(arr) {
	if (arr.length < 2) {
		return arr;
	}
	let midPoint = Math.floor(arr.length / 2);
	let left = mergeSort(arr.slice(0,midPoint));
	let right = mergeSort(arr.slice(midPoint));
	return merge(left,right);
}


console.log(mergeSort([1,6,5,3,10,9,3,4,5,6,2,1,7,5,9,10]));