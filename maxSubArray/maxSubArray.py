from sys import maxint

def maxSubArray(nums):

	"""
	:type nums: List[int]
	:rtype: int
	"""
	max_here = 0
	max_so_far = -maxint - 1

	for i in nums:
		max_here = max(i, max_here + i)
		max_so_far = max(max_so_far, max_here)

	return max_so_far

	# call divide and conquer
	l = 0
	h = len(nums) - 1
	maxNum = maxSubArrayhelper(nums, l, h)
	return maxNum

# divide and conquer
def maxCrossingSum(nums, l, m, h):
	s = 0
	left = -maxint - 1
	for i in range(m,l,-1):
		s = s + nums[i]
		if s > left:
			left = s

	s = 0
	right = -maxint - 1
	for i in range(m, h):
		s = s + nums[i]
		if s > right:
			right = s

	return left + right

def maxSubArrayhelper(nums, l, h):
	if l == h:
		return nums[l]

	m = (l + h) / 2

	return max(max(maxSubArrayhelper(nums, l, m), maxSubArrayhelper(nums, m+1, h)), maxCrossingSum(nums,l,m,h))

