def insert_sort():
	A = [5,2,4,7,1,3,2,6]
	for i in range(1,len(A)):
		key = A[i]
		j = i - 1
		while j>=0 and key<A[j]:
			A[j+1] = A[j]
			j -= 1
		A[j+1] =  key
	print A

insert_sort()