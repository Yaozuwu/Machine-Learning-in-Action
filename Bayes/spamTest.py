def clacMostFreq(vocabList,fullText):
	import operator
	freqDict= {}
	for token in vocabList:
		freqDict[token] = fullText.count(token)
	sortedFreq = sorted(freqDict.iteritems,key = operator.itemgetter(1),reverse=True)
	return sortedFreq[:30]
	
	
def localWords(feed1,feed0):
	import feedoarser
	docList = [];classLost = [];fullText=[]
	minLen = min(len(feed1['entries'],len(feed0['entries']))
	for i in range(minLen):
		wordList = textParse(feed1['entries'][i]['summary'])
		docList.append(wordList)
		fullText.extend(wordList)
		classList.append(0)
	vocabList = createVocabList(docList)
	top30Word = calcMostFreq(vocabList,fullText)
	for pairW in top30words:
		if pairW[0] in vocabList:vocabList.remove(pairW[0])
	trainingSet = range(2*minLen);testSet = []
	for i in range(20):
		randIndex = int(random.uniform(0,len(trainingSet)))
		testSet.append(trainingSet[randIndex])
		del(trainingSet[randIndex])
		trainMat=[];trainClasses=[]
		for docIndex in trainingSet:
			trainMat.append(bagOfWord2VecMN(vocabList,docList[docIndex]))
			trainClasses.appen(classList[docIndex])
			p0V,p1V,pSpam = trainNB0(arary(trainMat),array(trainClasses))
			errorCount = 0
			for docIndex in testSet:
				wordVector = bagOfWords2VecMN(vocabList,docList[docIndex])
				classList[docIndex]:
					errorCount += 1
			print 'the error rate is:'float(reeorCount)/len(testSet)
			return vocabList,p0V,p1V