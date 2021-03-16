#IMatrixChain.py

import numpy as np
import time

def i_matrix_chain(p:list)->list:
	n = len(p) - 1
	M = np.zeros([n, n], dtype = int)
	K = np.zeros([n, n], dtype = int)
	for l in range(1, n): # From 0 to 2
		for i in range(0, n - l):
			j = i + l
			m1 = float('inf')
			for k in range(i, j):			
				x = M[i][k] + M[k+1][j] + p[i] * p[k+1] * p[j+1]
				if(m1 >= x):
					m1 = x
					kk = k + 1
			M[i][j] = m1
			K[i][j] = kk
	return [M, K]

def main():
	#d = [30, 1, 40, 10, 25]
	d = [80, 96, 66, 4, 85, 94, 68]
	tic = time.perf_counter()	
	x = i_matrix_chain(d)
	toc = time.perf_counter()
	print("M: ")
	print(x[0])
	print("K: ")
	print(x[1])
	print(f"Time: {toc - tic:0.8f}")

if __name__ == "__main__":
	main()
