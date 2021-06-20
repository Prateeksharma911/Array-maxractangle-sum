def kadane(arr):
	sumi=-999999999
	maxsum=0
	start=0
	end=0
	for i in range(len(arr)):
		maxsum+=arr[i]
		if sumi<maxsum:
			end=i
		sumi=max(maxsum,sumi)

		if maxsum<0:
			start=i+1
			maxsum=0
	return sumi,start,end


def ractanglesum(array):
	row=len(array)
	column=len(array[0])
	maxsum=-9999999999
	maxup=0
	maxdown=0
	maxleft=0
	maxright=0
	for i in range(row):
		temp=[0]*row
		for j in range(i,column):
			for k in range(row):
				temp[k]+=array[k][j]
			sumi,left,right=kadane(temp)
			if sumi>maxsum:
				maxsum=sumi
				maxleft=i
				maxright=j
				maxup=left
				maxdown=right
	print(maxsum)
	print(maxleft,maxup)
	print(maxdown,maxright)




M = [[1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]]
ractanglesum(M)