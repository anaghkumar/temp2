# x = [i for i in range(5)]
# x = [{i: i+2} for i in range(5)]
# print(x)


# a = lambda *args, **kwargs: [[arg*2 for arg in args], [kwargs.get("hello")]]

# print(a(4, 1, 2, 3, 4, hello="Anagh"))

# x, y = 25, 26

# big = x if x < y else y
# print(big)


# def binarySearch(arr,key):
#     low = 0
#     high = len(arr)-1
#     mid = 0

#     while low<=high:
#         mid = (low+high)//2
#         if arr[mid] > key:
#             high = mid-1
#         elif arr[mid]<key:
#             low = mid +1
#         else :
#             print("Found At", mid,"Index")
#             return mid
#     return -1


# def binarySearch(arr,key):
#     low = 0
#     high = len(arr)-1
#     mid = 0

#     while low<=high:
#         mid = (low+high)//2
#         if arr[mid]>key:
#             high = mid-1
#         elif arr[mid]<key:
#             low = mid+1
#         else:
#             print("Found at", mid ,"Post")
#             return mid
#     return -1


# binarySearch([1, 3, 4, 5, 6, 7, 10], 10)


# x = [1,2,2,3,4,5,6]
# x.remove(2)
# x.remove(2)
# try:
#     x.remove(2)
# except ValueError:
#     print("Value Error")
# print(x)


def hello(fun):
    def run():
        a = fun()
        return a.upper()
    return run


@hello
def sayHello():
    return "abc"


# print(sayHello())


def twoSum(arr, target):
    map = {}
    for idx, value in enumerate(arr):
        if target-value in map:
            return [map[target-value], idx]
        else:
            map[value] = idx

# [2,3,4,5]
# 9


def twoSum(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j] == target:
                return [i, j]
    return -1


# print(twoSum([2, 3, 4, 5], 9))

def spiralMatrix(mat):
	r = len(mat)
	c = len(mat[0])

	top = 0
	left = 0
	bottom = r
	right = c

	while top <= bottom and left <= right:
		for i in range(left, right):
			print(mat[top][i], end=" ")
		top += 1

		for i in range(top, bottom):
			print(mat[i][right], end=" ")
		right -= 1

		if top <= bottom:
			for i in range(right, left+1, -1):
				print(mat[bottom][i], end=" ")

			bottom -= 1

		if left <= right:
			for i in range(bottom, top+1, -1):
				print(mat[i][left], end=" ")
			left += 1

spiralMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]])


def spiralMatrix()