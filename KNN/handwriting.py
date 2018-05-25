def handwritingClassTest():
	hwLabels = []
	trainingFileList = listdir('trainingDigits')
	m = len(trainingFileList)
	trainingMat = zeros((m,1024))
	for i in range(m):
		fileNumeStr = trainingFileLost[i]
		fileStr = fileNameStr.split('.')[0]
		classNumStr = int(fileStr.split('_')[0])
		hwLabels.append(classNumStr)
		trainingMat[i,:] = img2vector('trainingDigits/%s' % fileNameStr)
	testFileList = listdir('testDigits')
	errorCount = 0.0
	mTest = len(testFileList)
	for i in range(mTest):
		fileNameStr = testFileList[i]
		fileStr = fileNameStr.split('_')[0])
		classNumStr = int(fileStr.split('_')[0])
		vectorUnderTest = img2Vector('testDigits/%s' % fileNameStr)
		classifierResult = classify0(vectorUnderTest,trainingMat,hwLabels,3)
		print "the classifier came back with: %d, the real answer is : %d " \ %(classifierResult,classNumStr)
		if (classifierResult != classNumStr):
			errorCount += 1.0
		print "\nthe total number of errpr is:  %d"  %errorCount
		print "\nthe total error rate is: %f" % (errorCount/float(mTest)) 