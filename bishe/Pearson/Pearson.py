import math
import numpy as np
np.seterr(divide='ignore', invalid='ignore')

def pearsonr(matrix):#x-axis is time series of a nodes
    nrows = len(matrix)
    ncols = len(matrix[0])
    for i in  range(nrows):
        for j in range(ncols):
            tmp = matrix[i][j] * 10000
            matrix[i][j] = int(tmp)
    n = ncols * 1.0
    res = [[0 for i in range(nrows)] for j in range(nrows)]
    for i in range(nrows):
            idx = i + 1
            for j in range(idx, nrows):
                    a = b = c = f = e = 0;
                    for k in range(0, ncols):
                            a += matrix[i][k] * matrix[j][k]; #sigma xy
                            b += matrix[i][k]; #sigma x
                            c += matrix[j][k]; #sigma y
                            e += matrix[i][k] * matrix[i][k]; #sigma xx
                            f += matrix[j][k] * matrix[j][k]; #sigma yy
                    
                    para1 = a
                    para2 = b * c / n
                    para3 = e
                    para4 = b * b / n
                    para5 = f;
                    para6 = c * c / n
                    
                    #print a, b ,c , e, f					
                    r1 = para1 - para2
                    #print para3 - para4
                    #print para5 - para6
                    r2 = (para3 - para4) * (para5 - para6)
                    #print "r2", r2
                    r2 = math.sqrt(r2)
                    r = 1.0 * r1 / r2 
                    res[i][j] = res[j][i] = r * 1.00000
    return res
'''    
def pearsonr(matrix):#x-axis is time series of a nodes
	nrows = len(matrix)
	ncols = len(matrix[0])
	mat = np.matrix(matrix)
	pear_mat = np.corrcoef(mat)
	#pear_mat = np.corrcoef(mat)*0.5+0.5  
	res = [[0 for i in range(nrows)] for j in range(nrows)]
	for i in range(nrows):
		for j in range(nrows):
			res[i][j] = pear_mat[i][j]

def spearman(matrix):
	print 'spearman'
'''			