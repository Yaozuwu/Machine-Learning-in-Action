from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt

	
def classify0(inX,dataSet,labels,k):                 #dataSet(样本x特征值)
	dateSetSize = dataSet.shape[0]
	difMat = tile(inX,(dataSetSize,1)) - dataSet        #tile:复制单元（行数，列数）
	sqDIffMat = diffMat**2
	sqDistances = sqDiffMat.sum(axis = 1)
	distances = sqDistances**0.5
	sortedDistIndicies = distances.argsort()                       #argsort函数返回的是数组值从小到大的索引值  返回array数组
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1    #返回指定键的值，如果值不在字典中返回默认值None    分解为元组列表
	sortedClassCount = sorted(classCount.iteritems(),key = operator.itemgetter(1),reverse = True)
	return sortedClassCount[0][0]
	
	

def img2vector(filename):
	returnVect = zeros((1,1024))
	fr = open(filename)
	for i in range(32):
		lineStr = fr.readline()
		for j in range(32):
			returnVect[0,32*i+j] = int(lineStr[k])
	return returnVect


	
def fileName(filename):
	fr = open(filename)
	arrayOLines = fr.readlines()                 #用于读取所有行(直到结束符 EOF)并返回列表，该列表可以由 Python 的 for... in ... 结构进行处理。
	numberOflines = len((arrayOLines)
	returnMat = zeros((numberOfLines,3))               #修改代码使得自己可以读取特征值
	classLabelVector = []
	index = 0
	for line in arrayLines:
		line = line.strip()             #去掉每行头尾空白，截取掉所有回车字符
		listFormLine = line.split('\t')                        #按照tab键将整行元素，分成元素列表
		returnMat[index,:] = listFromLine[0:3]
		classLabelVector.append(int(listFormLine[-1]))
		index += 1
	fr.close()	
	return returnMat,calssLabelVector
	

	
def plotfigure(inputMat):
	fig = plt.figure()
	ax = fig.add_subplot(111)     #子图总行数，子图总列数，子图位置
	ax.scatter(inputMat[:,1],inputMat[:,2])
	plt.show()
	
	
#newValue = (OldValue - min)/(max - min)将任意范围内的特征值转换到0-1的区间
def autoNorm(dataSet):                            # dataSet为整个数据集              
	minVals = dataSet.min(0)                      #参数0使得是从当前列中选取最小值，而不是行
	maxVals = dataSet.max(0)
	ranges = maxVals - minVals
	normDataSet = zeros(shape(dateSet))
	m = dataSet.shape[0]
	normDataSet = dataSet - tile(minVals,(m,1))
	normDataSet = normDataSet/tile(ranges,(m,1))
	return normDataSet,ranges,minVals
	
	
	
def KNNTest(filename):
	hoRatio = 0.10    #测试向量的比例
	DataMat , Labels = fileName(filename)
	normMat,ranges,minVals = autoNorm(DataMat)
	m = normMat.shape[0]
	numTestVecs = int(m * hoRatio)
	errorCount = 0.0
	for i in range(numTestVecs)：
		classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],Labels[numTestVecs:m],3)
		print "the classifier came back with : %d, the real answer is ：%d"(classifierResult,Labels)
		if(classifierResult != datingLabels[i]):
			errorCount += 1.0
		print "the total error rate is: %f"  %(errorCount/float(numTestVecs))