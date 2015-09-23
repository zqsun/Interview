A = [5,2,4,7,1,3,2,6]

def merge(A,p,q,r):
	L = A[p:q+1] 
	R = A[q+1:r+1]
	i =0
	j=0
	k=0
	while i<len(L) and j<len(R):
		if L[i] < R[j]:
			A[p+k] = L[i]
			i += 1
			k += 1
		else:
			A[p+k] = R[j]
			j += 1
			k += 1
	while i < len(L):
		A[p+k] = L[i]
		k += 1
		i += 1
	while j < len(R):
		A[p+k] = R[j]
		j += 1
		k += 1

def merge_sort(A,p,r):
	if p<r:
		q = (p+r-1)/2
		merge_sort(A,p,q)
		merge_sort(A,q+1,r)
		merge(A,p,q,r)


def merge_sort_ex(A):
	if len(A) > 1:
		q = len(A)/2
		L = A[:q]
		R = A[q:]
		merge_sort_ex(L)
		merge_sort_ex(R)
		i = 0
		j = 0
		k = 0
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				A[k] = L[i]
				k += 1
				i += 1
			else:
				A[k] = R[j]
				k += 1
				j += 1
		while i < len(L):
			A[k] = L[i]
			k += 1
			i +=1
		while j < len(R):
			A[k] = R[j]
			k += 1
			j += 1


merge_sort_ex(A)
print A

