import matplotlib.pyplot as plt

decisionNode = dict(boxstyle = "sawtooth",fc="0.8")
leafNode = dict(boxstyle="round4",fc="0.8")
arrow_args = dict(arrowstyle='<-')

def plotNode(nodeTxt,centerPt,parentPt,nodeType):
	createPlot.ax1.annotate(nodeTxt,xy = parentPt,xycoords='axes fraction',xytext=centerPt,textcoords='axes fraction',va = "center" , ha='center',bbox = nodeType,arrowprops = arrow_args)
	
	
	
def createPlot():
	fig = plt.figure(1,facecolor='white')
	fig.clf()
	createPlot.ax1 = plt.subplot(111,frameon=False)
	plotNode('a decisiong node',(0.5,0.1),(0.1,0.5),decisionNode)
	plotNode('a leaf node',(0.8,0.1),(0.3,0.8),leafNode)
	plt.show()
	
	
def getNumLeaf(myTree):
	numLeafs = 0
	firstStr = myTree.keys()[0]
	secondDict = myTree[firstStr]
	for key in secondDict.keys():
		if type(secondDict[key].__name__=='dict'):
			numLeafs += getNumLeafs(secondDict[key])
		else:
			numLeafs +=1
	return numLeafs
	
def getTreeDepth(myTree):
	maxDepth = 0
	firstStr = myTree.keys()[0]
	secondDict = myTree[firstStr]
	for key in secondDict.keys():
		if type(secondDict[key]).__name__=='dict':
			thisDepth = 1+getTreeDepth(secondDict[key])
		else:
			thisDepth = 1 
		if thisDepth > maxDepth:
			maxDepth = thisDepth
	return maxDepth
	
	
def plotMidText(cntrPt,parentpt,txtString):
	xMid = (parentPt[0] - cntrPt[0])/2.0 +cntrPt[0]
	yMid = (parentPt[1] - cntrPt[1])/2.0 +cntrPt[1]
	createPlot.ax1.text(xMid,yMid,txtString)
	
def plotTree(myTree,parentPt,nodeTxt):
	numLeafs = getNumLeafs(myTree)
	depth = getTreeDepth(myTree)
	firstStr = myTree.keys()[0]
	cntrPt = (plotTree.xOff+(1.0 + float(numLeafs))/2.0/plotTree.totalW,plotTree.yOff)
	plotMidText(cntrPt,parentPT,nodeTxt)
	plotNode(firstStr,cntPt,parentPt,decisionNode)
	secondDIct = myTree[firstStr]
	plotTree.yOff = plotTree.yOff -1.0/plotTree.totalD
	for key in secondDict.keys():
		if type(secondDict[key]).__name__=='dict':
			plotTree(secondDict[key],cntrPt,str[key])
		else:
			plotTree.xOff = plot.xOff + 1.0/plotTree.totalW
			plotNode(secondDoct[key],(plotTree.xOff,plotTree.yOff),cntrPt,leafNode)
			plotMidText((plotTree.xOff,plotTree.yOff),cntrPt,str(key))
			plotTree.yOff = plotTree.yOff+1.0/plotTreetotal1D
			
def createPlot(inTree):
	fig = plt.figure(1,facecolor='white')
	fig.clf()axprops = dict(xticks=[],yticks=[])
	createPlot.ax1 = plt.subplot(111,franein=False,**axprops)
	plotTree.totalW = float(getNumLeafs(inTree))
	plotTrss.totlaD = float(getTreeDepth(inTree))
	plotTree.xOff = -0.5/plotTree.totalW;pltTree.yOff = 1.0
	plotTree(inTree,(0.5,1.0),'')
	plt.show()
	
		