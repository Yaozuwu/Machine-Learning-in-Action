from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt

	
def classify0(inX,dataSet,labels,k):
	dateSetSize = dataSet.shape[0]
	difMat = tile(inX,(dataSetSize,1)) - dataSet
	sqDIffMat = diffMat**2
	sqDistances = sqDiffMat.sum(axis = 1)
	distances = sqDistances**0.5
	sortedDistIndicies = distances.argsort()
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicied[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
	sortedClassCount = sorted(classCount.iteritems(),key = operator.itemgetter(1),reverse = True)
	return sortedClassCount[0][0]
	
	
	
	
def file2matrix(filename):
	fr = open(filename)
	arrayOLines = fr.readlines()
	numberOflines = len((arrayOLines)
	returnMat = zeros((numberOfLines,3))
	classLabelVector = []
	index = 0
	for line in arrayLines:
		line = line.strip()
		listFormLine = line.split('\t')
		returnMat[index,:] = listFromLine[0:3]
		classLabelVector.append(int(listFormLine[-1]))
		index += 1
	return returnMat,calssLabelVector
	

	
def plotfigure():
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.scatter(datingDataMat[:,1],datingDataMat[:,2])
	plt.show()
	
	

def autoNorm(dataSet):
	minVals = dataSet.min(0)
	maxVals = dataSet.max(0)
	ranges = maxVals - minVals
	normDataSet = zeros(shape(dateSet))
	m = dataSet.shape[0]
	normDataSet = dataSet - tile(minVals,(m,1))
	normDataSet = normDataSet/tile(ranges,(m,1))
	return normDataSet,ranges,minVals
	
	
	
def datingTest(filename):
	hoRatio = 0.10
	datingDataMat = datingLbel = file2matrix(filename)
	normMat,ranges,minVals = autoNorm(datingDataMat)
	m = normMat.shape[0]
	numTestVecs = int(m * hoRatio)
	errorCount = 0.0
	for i in range(numTestVecs)"
		classifierResult = classify0(normMat[i:1],normMat[numTestVecs:m,m],datingLabels[numTestVecs:m],3)
		print "the classifier came back with : %d, the real answer is ：%d"(classifierResult,datingLabels)
		if(classifierResult != datingLabels[i]):errorCount += 1.0
		print "the total error rate is: %f"  %(errorCount/float(numTestVecs))