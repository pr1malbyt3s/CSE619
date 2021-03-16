#IMatrixChain.py

import numpy as np
import time

def recursive_cost(p:list, i:int, j:int)->dict:
	if (i == j):
		return {'m1': 0, 'kk':0}
	else:
		m1 = float('inf')
		kk = 0
		for k in range(i, j):			
			x = recursive_cost(p, i, k)
			x1 = x['m1']
			y = recursive_cost(p, k+1, j)
			x2 = y['m1']
			x3 = p[i-1] * p[k] * p[j]
			x = x1 + x2 + x3
			if (m1 > x):
				m1 = x
				kk = k + 1
	return {'m1':m1, 'kk':kk}


def r_matrix_chain(p:list)->list:
	n = len(p) - 1
	M = np.zeros([n, n], dtype = int)
	K = np.zeros([n, n], dtype = int)
	for l in range(1, n): # From 0 to 2
		for i in range(0, n - l):
			j = i + l
			x = recursive_cost(p, i, j)
			M[i][j] = x['m1'] 
			K[i][j] = x['kk']
	return [M, K]

def main():
	#d = [30, 1, 40, 10, 25]
	d = [80, 96, 66, 4, 85, 94, 68]	
	tic = time.perf_counter()	
	x = r_matrix_chain(d)
	toc = time.perf_counter()
	print("M: ")
	print(x[0])
	print("K: ")
	print(x[1])
	print(f"Time: {toc - tic:0.8f}")

if __name__ == "__main__":
	main()
