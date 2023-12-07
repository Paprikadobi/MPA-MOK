#!/usr/bin/python3

#python3 -m pip install statsmodels
import numpy as np
import statsmodels.api as sm


VERBOSITY = 0

##### TEST UTILITY #####
# input:
#	data = original dataset
#	adata = anonymized dataset
# output:
#	ut = 0 same data set
# We want that ut is close to 0

def utility(data,adata):
	row_data = len(data)
	colm_data = len(data[0])
	udata = []
	udata.extend(data)
	udata.extend(adata)
	T = list(1 for i in range(row_data))
	T.extend(list(0 for i in range(row_data)))
	T = np.array(T)
	logit = sm.Logit(T,udata)
	result = logit.fit(method = 'bfgs', maxiter=1000)
	ut = 0
	print(row_data)
	for i in range(row_data):
		p = result.predict(adata[i])
		print(p)
		ut = ut + (p-0.5)**2
	ut = ut/row_data

	return ut


# ##### TEST DISCLOSURE RISK = RECORD LINKAGE #####
# input:
#	data = original dataset
#	adata = anonymized dataset
# output:
#	distance = 0 same data set
# we want that distance is far from 0

def record_linkage(data, adata):

	tdata = []
	sort_tdata = []
	t_adata = []
	sort_tadata = []



	# data
	tdata = transpose_data(data)
	for x in tdata: #sort data
		sort_x = sorted(x)
		sort_tdata.extend([sort_x])
	#matrix of the rank of data
	rank_data = rankData(tdata,sort_tdata)


	t_adata = transpose_data(adata)
	for x in t_adata: #sort data
		sort_x = sorted(x)
		sort_tadata.extend([sort_x])
	rank_adata = rankAdata(t_adata, sort_tadata)
	distance = sum_rank_distance(rank_data, rank_adata)



	return distance



# ##### Functions #####

def transpose_data(data):      #column to row and viceversa
	a = np.matrix(data)
	a = a.transpose()
	a = a.tolist()
	return a

def rankAdata(tadata,sdata):    # the ranks of all anonymazed elements
	dictionary = []
	for i in range(len(tadata)):
		dicti = []
		for j in range(len(tadata[i])):
			dicti.append(sdata[i].index(tadata[i][j]))
			if VERBOSITY==1:
				print('tadata ',tadata[i][j],'rank ',dicti[j])
		dictionary.append(dicti)
	rank = transpose_data(dictionary)
	return rank




def rankData(tdata,sort_tdata):
	nrecord = len(tdata[0])
	nattr = len(tdata)
	rank  = list(list(0 for i in range(len(tdata))) for i in range(len(tdata[0])))
	if VERBOSITY ==1:
		print("start rank", rank)
	for j in range(nattr):
		for i in range(nrecord):
			if i == 0 or sort_tdata[j][i] != sort_tdata[j][i-1]:
				if VERBOSITY ==1:
					print("different from the previous")
				pos = tdata[j].index(sort_tdata[j][i])
				rank[pos][j] = i
				if VERBOSITY ==1:
					print("i = ", i, "[", j, "][", i, "] = ", sort_tdata[j][i], " != [", j, "][", i-1, "] = ", sort_tdata[j][i-1])
					print("pos = ", pos, 'rank= ', rank[pos][j])
			else:
				if VERBOSITY ==1:
					print("equal to the previous")

				pos = tdata[j][pos+1:].index(sort_tdata[j][i]) + pos + 1
				rank[pos][j] = i
				if VERBOSITY == 1:
					print("i = ", i, "[", j, "][", i, "] = ", sort_tdata[j][i], " = [", j, "][", i-1, "] = ", sort_tdata[j][i-1])
					print("pos = ", pos, 'rank= ', rank[pos][j])


	if VERBOSITY ==1:
		print("matrix of the rank", rank)
	return rank


# sum on all the records and attributes of the rank distance (record, linked_record)

def sum_rank_distance(rank_data,rank_adata):
	sample = []
	distribution = list(0 for i in range(len(rank_data)))
	dist = 0
	for i in range(len(rank_data)):
		distance = []
		for k in range(len(rank_adata)):
			d = 0
			for j in range(len(rank_adata[0])):
				d = d + (rank_adata[k][j] - rank_data[i][j])**2
			if d==0:
				d = 0
			else:
				d = np.log(np.sqrt(d))

			if VERBOSITY ==1:
				print('d = ', d)
			distance.append(d)

		if VERBOSITY==1:
			print("MIN distance", min(distance), "\ndistance", distance)
		dist = dist + min(distance)
	if VERBOSITY==1:
		print("distance ", dist)
	dist = dist/(len(rank_data)*len(rank_data[0]))
	if VERBOSITY==1:
		print("distance = ",dist)

	return dist







