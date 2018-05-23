def loadDataSet():
	postingList = [['my','dog','has','flea',\
					'problems','help','please'].
					['maybe','not','take','him'.\
					'to','dog','park','stupid'],
					['my','dalmation','is','so','cute',\
					'I','love','him'],
					['stop','posting','stupid','worthless','garbage'],
					['mr','licks','ate','my','steak','how',\
					'to','stop','him'],
					['quit','buying','worthless','dog','food','stupid']]
	classVec = [0,1,0,1,0,1]
	return postingList,classVec
	
def createVocabList(dataSet):
	vocaSet = set([])
	for document in dataSet:
		vocabSet = vocabSet | set(document)
	return list(vocabSet)
	
	
def setOfWord2Vec(vocabList,inputSet):
	returnVec = [0] * len(vocabList)
	for word inputSet:
		if word in vocabList:
			returnVec[vocabList,index(word)] = 1
		else:
			print ("the word %s is not in my Vocabulary!" %word)
	return returnVec
	
	
	
	
def bagOfWoeds2VecMN(vocabList,inputSet):
	returnVec = [0]*len(vocabList)
	for word in inputSet:
		returnVec[vocablist.index(word)] += 1
	return returnVec
	
	
def trainNB0(trainMatrix,trainCategory):
		numTrainDocs = len(TrainMatrix)
		numWord = len(trainMatrix[0])
		pAbusive = sum(trainCategory) / float(numTrainDocs)
		p0Num = zeros(numWords)
		p1Num = zeros(numWords)
		p0Denmo = 0.0
		p1Denmo = 0.0
		for i in range(numTrainDocs):
			if trainCategory[i] == 1
				p1Num += trainMatrix[i]
				p1Demo += sum(trainMatrix[i])
			else:
				p0Num += trainMatrix[i]
				p0Demo += sum(trainMatrix[i])
		
		p1Vect = p1Num / p1Denmo
		p0Vect = p0Num / p0Denmo
	
	return p0Vect,plVect,pAbusive
	
	
	
def classifyNb(vec2Classify,p0Vec,p1Vec,pClass):
	p1 = sum(vec2Classify * p1Vec) + log(pClass1)
	p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass)
	if p1 > p0:
		return 1
	else:
		return 0


def testingNB():
	listOPosts,listClasses = loadDataSet()
	myVocabList = createVocabList(listOPosts)
	trainMat=[]
	for postinDoc in listOPosts:
		trainMat.append(setOfWords2Vec(MyVocabList,postinDoc))
	p0V,p1V,PAb = trainNB0(array(trainMat),array(ListClasses))
	testEntry = ['love','my','dalmation']
	thisDoc = array(setOfWords2Vec(MyVocabList,testEntry))
	print(testEntry,'classified as:',calssifyNB(thisDoc,p0V,p1V,pAb))
	testEntry = ['stupid','garbage']
	thisDoc = array(setOfWords2Vec(myVocabList,testEntry))
	print(testEntry,'classified as:',classifyNB(thisDoc,p0V,p1V,pAb))
	
	
	
	
