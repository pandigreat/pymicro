import numpy as np
from  Request import request
#import rpy2.robjects as robjects
from Pearson import pearsonr


service_dict = {
	"saw" : 9,
	"serviceA" : 5,
	"serviceB" : 4,
	"serviceC" : 3,
	"serviceA1" : 1,
	"serviceA2" : 6,
	"serviceA3" : 14,
	"serviceB1" : 2,
	"serviceB2" : 7,
	"serviceB3" : 11,
	"serviceC1" : 10,
	"serviceC2" : 13,
	"serviceC3" : 8,
	"serviceDB1" : 16,
	"serviceDB2" : 15,
	"serviceDB3" : 12
}
##########
def normal_x(mat):
	n = len(mat[0])
	res = [[0 for j in range(n)] for i in range(n)]
	for i in range(n):
		k = 0.0
		for j in range(n):
			k += mat[i][j]
		for j in range(n):
			res[i][j] = mat[i][j] / k
	return res
def normal_y(mat):
	n = len(mat[0])
	res = [[0 for j in range(n)] for i in range(n)]
	for j in range(n):
		k = 0
		for i in range(n):
			k += mat[i][j]
		for i in range(n):
			res[i][j] = mat[i][j] / k
#############			
def findleaf(i, callgraph, xsimilar):
	al = []
	res = -1
	for j in range(len(callgraph[0])):
		if (callgraph[i][j]) != 0:
			al.append(j)
	if len(al) == 0:
		return res
	for k in al:
		if float(xsimilar[k][0]) > res:
			res = float(xsimilar[k])
	return res

def RandomWalk(callgraph, similar, num, rho, itertimes, alpha):
	#callgraph = np.matrix(callgraph)
	similar = np.matrix(similar)
	ysimilar = np.sum(similar, axis = 0) 
	xsimilar = np.sum(similar, axis = 1) 
	xsimilar = np.array(xsimilar)
	ysimilar = np.array(ysimilar)
	#print ysimilar
	m = [[0 for i in range(num)] for j in range(num)]
	
	start_mark = service_dict['saw']
	
	for i in range(num):
		for j in range(num):
			if i == j and i == start_mark:
				m[i][j] = 0
			elif i == j and i != start_mark:
				r = findleaf(i, callgraph, xsimilar)
				if r == -1:
					m[i][j] = 0
				else:
					m[i][j] = max(0, float(xsimilar[i][0]) - r)#???
			elif callgraph[i][j] != 0:
				m[i][j] = float(xsimilar[i][0])
			elif callgraph[i][j] != 0 and callgraph[j][i] == 0:
				m[i][j] = float(ysimilar[0][j]) * rho
	
	m = np.matrix(m)
	xm = np.sum(m, axis = 1)
	#print xm
	m = np.array(m)
	xm = np.array(xm)
	
	#####xiuzheng ########
	k = 0
	for i in range(num):
		k += xm[i]
	k /= num
	for i in range(num):
		if xm[i] < 0.00001:
			xm[i] = k
	#######################
	
	p = [[0 for i in range(num)] for j in range(num)]
	for i in range(num):
		for j in range(num):
			p[i][j] = float(m[i][j]) / float(xm[i][0])
			
	p = np.matrix(p)
	#u = xsimilar
	pi = np.matrix([1 for i in range(num)])
	
	#Iteration formulation
	for i in range(itertimes):
		pi *= alpha 
		pi = pi * p
		pi += 1
		
	return pi

def MyRandomWalk(callgraph, similar, num, rho, itertimes, alpha):
	#callgraph = np.matrix(callgraph)
	similar = np.matrix(similar)
	ysimilar = np.sum(similar, axis = 0) 
	xsimilar = np.sum(similar, axis = 1) 
	xsimilar = np.array(xsimilar)
	ysimilar = np.array(ysimilar)
	#print ysimilar
	m = [[0 for i in range(num)] for j in range(num)]
	
	start_mark = service_dict['saw']
	
	for i in range(num):
		for j in range(num):
			if i == j and i == start_mark:
				m[i][j] = 0
			elif i == j and i != start_mark:
				r = findleaf(i, callgraph, xsimilar)
				if r == -1:
					m[i][j] = 0
				else:
					m[i][j] = max(0, float(xsimilar[i][0]) - r)#???
			elif callgraph[i][j] != 0:
				m[i][j] = float(xsimilar[i][0])
			elif callgraph[i][j] != 0 and callgraph[j][i] == 0:
				m[i][j] = float(ysimilar[0][j]) * rho
	
	m = np.matrix(m)
	xm = np.sum(m, axis = 1)
	#print xm
	m = np.array(m)
	xm = np.array(xm)
	
	#####xiuzheng ########
	k = 0
	for i in range(num):
		k += xm[i]
	k /= num
	for i in range(num):
		if xm[i] < 0.00001:
			xm[i] = k
	#######################
	
	p = [[0 for i in range(num)] for j in range(num)]
	for i in range(num):
		for j in range(num):
			p[i][j] = float(m[i][j]) / float(xm[i][0])
			
	p = np.matrix(p)
	#u = xsimilar
	pi = np.matrix([1 for i in range(num)])
	
	#Iteration formulation
	for i in range(itertimes):
		pi *= alpha 
		pi = pi * p
		pi += 1
		
	return pi
	
	
if __name__ == '__main__':

	rho = 0.3
	alpha = 0.6
	itertimes = 100
	#For the function request
	requestnum = 2
	loopnum = 9
	
	num = 16
	
	url = "http://192.168.99.100:9180/bottle/all/view"
	rscript = "C:\\Users\\EdisonPan\\Desktop\\bishe\\PC.r"
	rscript2 = "C:\\Users\\EdisonPan\\Desktop\\bishe\\PC2.r"
	keys = []
	splitlist = ['serviceD', 'serviceD1', 'serviceD2', 'serviceD3']
	call_by_saw = ['serviceA', 'serviceB', 'serviceC'] #pre set the callgraph
	
	#Solve data
	raw_res = [[0 for j in range (loopnum)] for i in range(num)]
	raw_th = [[0 for j in range(loopnum)] for i in range(num)]
	
	dict_res, dict_th, dict_err = request(url, requestnum, loopnum)
	#for k in dict_res[0]:
	#	print dict_res
	for i in range(loopnum):
		k = 0
		for j in (dict_res[i]):
			#print j[0], j[1]
			if j[0] not in splitlist:
				raw_res[k][i] = j[1]
				raw_th[k][i] = dict_th[i][k][1]
				k += 1
				if i == 0:
					keys.append(j[0])
	#print raw_res
	#Save keys name
	fp = open('C:\\Users\\EdisonPan\\Desktop\\bishe\\key', 'w')
	j = 1
	for i in keys:
		#print j, i
		j += 1
		fp.write(i + " ")
	fp.write('\n')
	fp.close()
	#Save data to files
	fp = open('C:\\Users\\EdisonPan\\Desktop\\bishe\\raw_res', 'w')
	for i in range(num):
		for j in range(loopnum):
			fp.write(str(raw_res[i][j]) + " ")
		fp.write('\n')
	fp.close()
	fp = open('C:\\Users\\EdisonPan\\Desktop\\bishe\\raw_th', 'w')
	for i in range(num):
		for j in range(loopnum):
			fp.write(str(raw_th[i][j]) + " ")
		fp.write('\n')
	fp.close()
	#Run PC-Algorithm and get the callgraphs 
	
	#robjects.source(rscript)
	#robjects.source(rscript2)
	#callgraph_res = []
	#callgraph_th = []
	
	##########Pre set the call edge and Get the callgraph##############
	callgraph_res = [[0 for j in range(num)] for j in range(num)]
	callgraph_th = [[0 for j in range(num)] for j in range(num)]
	c_ = []

	fp = open("C:\\Users\\EdisonPan\\Desktop\\bishe\\a.txt", 'r')
	for l in fp:
		c = l.split(' ')
		c_.append(c)
	fp.close()
	for i in range(1, num + 1):
		for j in range(1, num + 1):
			callgraph_res[i-1][j-1] = int(c_[i][j])
	c_ = []
	fp = open("C:\\Users\\EdisonPan\\Desktop\\bishe\\b.txt", 'r')
	for l in fp:
		c = l.split(' ')
		c_.append(c)
	fp.close()
	for i in range(1, num + 1):
		for j in range(1, num + 1):
			callgraph_th[i-1][j-1] = int(c_[i][j])
	
	k = service_dict['saw']
	for i in call_by_saw:
		tmp = service_dict[i]
		callgraph_res[k][tmp] = 1
		callgraph_th[k][tmp] = 1
    
	############################################
	#Calculation the pearson
	
	pear_res = pearsonr(raw_res)
	pear_th = pearsonr(raw_res)
	#print pear_res
	#print '\n'
	#print pear_th

	
	#Run RandomWalk and get the answers
	pi_res = RandomWalk(callgraph_res, pear_res, num, rho, itertimes, alpha)
	pi_th = RandomWalk(callgraph_th, pear_th, num, rho, itertimes, alpha)
	arr_res = np.array(pi_res)
	arr_th = np.array(pi_th)
	
	dict_res = dict(zip(keys, arr_res[0]))
	dict_th = dict(zip(keys, arr_th[0]))
	#normal_x(pear_res)
	#normal_x(pear_th)
	
	#print rs_th
	rs_res = sorted(dict_res.items(), key = lambda d:d[1], reverse = True)
	rs_th = sorted(dict_th.items(), key = lambda d:d[1], reverse = True)
	rs_err = sorted(dict_err.items(), key = lambda d:d[1], reverse = True)
	print "Result of RandomWalk"
	for k in rs_res:
		print k
	print "##########################"
	print "Result of MyRandomWalk"
	for k in rs_th:
		print k
	print "##########################"
	print "Result of Error times"
	for i in rs_err:
		print i
