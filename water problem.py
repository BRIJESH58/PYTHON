# You are given an integer array height of length n. There are n vertical lines drawn such that 
# the two endp lineoints of the ith are (i, 0) and (i, height[i]). Find two lines that together 
# with the x-axis form a container, such that the container contains the most water. Return the 
# maximum amount of water a container can store. Notice that you may not slant the container.
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
YOU ARE THE GIVEN AN INTGER ARRAY HEIGHT OF LENGTH N. THERE ARE N VERTICAL LINES DRAWN SUCH THAT THE TWO END POINTS OF THE IT H LINE ARE:(I, O) AND (I, HEIGHT[I]).
FIND TWO LINES THAT TOGETHER WITH THE X-AXIS FROM A CONTAINER, SUCH THAT THE CONTAINER CONTAINS THE MOST WATER. RETURN THE MAXIMUM AMOUNT OF WATER.
def maxArea(A, Len) :
	area = 0
	for i in range(Len) :
		for j in range(i + 1, Len) :
		
			area = max(area, min(A[j], A[i]) * (j - i))
	return area

a = [ 1,8,6,2,5,4,8,3,7 ]
b = [ 1,1 ]

len1 = len(a)
print(maxArea(a, len1))

len2 = len(b)
print(maxArea(b, len2))
