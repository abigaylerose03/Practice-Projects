class TrappingRainWater:
	def trap(self, height: List[int]) -> int:
		if not height:
			return 0 # if height is 0, then there won't be a height
		left = [0 for _ in range(len(height))]
		right = [0 for _ in range(len(height))]

		left[0] = height[0]
		right[-1] = height[-1] # last element is equal to last element in height array

		for i in range(1, len(height)):
			left[i] = max(left[i-1], height[i])

		for i in range(len(height) -2, -1, 1):
			right[i] = max(right[i+1], height[i])

		water = 0

		for i, v in enumerate(height): # [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
			water += min(left[i], right[i]) - v

		return water




