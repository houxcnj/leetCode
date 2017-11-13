def uniquePathsWithObstacles(self, obstacleGrid):
	m = len(obstacleGrid)
	n = len(obstacleGrid[0])

	resGrid = [[0 for x in range(n+1)] for x in range(m+1)]
	resGrid[0][1] = 1
	for i in range(1,m+1):
		for j in range(1, n+1):
			if not obstacleGrid[i-1][j-1]:
				resGrid[i][j] = resGrid[i][j-1] + resGrid[i-1][j]

	return resGrid[m][n]