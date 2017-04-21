import urllib
import urllib2
import time
import json
import time
import datetime
import random
import simplejson as json

service_dict = {
	"saw" : "view_services",
	"serviceA" : "serviceA",
	"serviceB" : "serviceB",
	"serviceC" : "serviceC",
	"serviceD" : "serviceD",
	"serviceA1" : "serviceA1",
	"serviceA2" : "serviceA2",
	"serviceA3" : "serviceA3",
	"serviceB1" : "serviceB1",
	"serviceB2" : "serviceB2",
	"serviceB3" : "serviceB3",
	"serviceC1" : "serviceC1",
	"serviceC2" : "serviceC2",
	"serviceC3" : "serviceC3",
	"serviceD1" : "serviceD1",
	"serviceD2" : "serviceD2",
	"serviceD3" : "serviceD3",
	"serviceDB1" : "serviceDB1",
	"serviceDB2" : "serviceDB2",
	"serviceDB3" : "serviceDB3"
}

dict_res = {} #response 
dict_th = {} #Throughoutput
list_res = [] #time slice of response
list_th = [] #time slice of throughoutput
for key in service_dict.keys():
	dict_res[key] = 0.0
	dict_th[key] = 0.0

'''
	Solve message of json format
'''
def extractMsg(l, res):
	if isinstance(l, list):
		for ls in l:
			extractMsg(ls, res)
	elif isinstance(l, dict):
		msg =l['message']
		t = l['t']
		name = l['name']
		if name == 'view': 
			res['saw'] += float(t)
		else :
			res[name] += float(t) 
		extractMsg(msg, res)
	else:
		pass

'''
	Just a request to a url
'''
def req_test(url):
	T = time.time() #For vies data
	try:
		msg = urllib2.urlopen(url, timeout = 15).read()
		f = open('s', 'w')
		f.write(msg)
		f.close()
	except Exception as e:
		print e
		return 'error'
	T = time.time() - T
	res = {}
	for key in service_dict.keys():
		res[key] = 0.0
	#res['view'] = 0.0
	msg = json.loads(msg)
	extractMsg(msg, res) 
	#print res
	return res
	
'''
	Request for requestnum-time and loopnum-time loop
'''
def request(url, requestnum, loopnum):
	#print dict_res
	dict_res = {} #response 
	dict_th = {} #Throughoutput
	dict_err = {} #Error
	for key in service_dict.keys():
		dict_res[key] = 0.0
		dict_th[key] = 0.0
		dict_err[key] = 0
	for i in range(loopnum):
		t = time.time()
		for j in range(requestnum):
			ts = time.time()
			tmpres = req_test(url)
			ts = time.time() - ts + random.uniform(0.003,0.00001)
			ts *= 100
			dict_res['saw'] += ts #response time of saw
			for key in tmpres.keys():
				if tmpres[key] < 0:
					#tmpres[key] = random.uniform(0.003,0.00001)
					tmpres[key] = 0
					dict_err[key] += 1
				tmpres[key] *= 100
				dict_res[key] += tmpres[key]
		t = time.time() - t
		
		for key in dict_res.keys():
			#dict_res[key] *= 100
			
			if dict_res[key] != 0:
				dict_th[key] = requestnum / dict_res[key] * 1000
			dict_res[key] /= t 
		res = []
		th = []
		for key in dict_res.keys():
			res.append((key, dict_res[key]))
			th.append((key, dict_th[key]))
		#res = sorted(dict_res.items(), key = lambda d:d[0], reverse = True)
		#th = sorted(dict_th.items(), key = lambda d:d[0], reverse = True)
		#print 'heoo\n'th
		
		list_res.append(res)
		list_th.append(th)
		
		time.sleep(1)
		for key in dict_res.keys():
			dict_res[key] = 0.0
			
	return (list_res, list_th, dict_err)		

'''
if __name__ == "__main__":
	url = "http://192.168.99.100:9180/bottle/all/view"
	timeout = 2
	requestnum = 100;
	loopnum = 2
	list_res, list_th = request(url, requestnum, loopnum)
	for key in list_res:
		for val in key:
			print val
'''	
	