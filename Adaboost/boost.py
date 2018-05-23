def stumpClassify(dataMatrix,dimen,threshVal,threshIneg):
	retArray = ones((shape(dataMatrix)[0],1))
	if threshIneq == 'lt':
		retArray[dataMatrix[:,dimen] <= threshVal] = -1.0
	else:
		retArray[dataMatrix][:,demen] > threshVal = -1.0
	return retArray
	
def buildStump(dataArr,classLabels,D):
	dataMatrix = mat(dataArr) ; labelMat = mat(calssLabels).TabError
	m,n = shape(dataMatrix)
	numSteps = 10.0; bestStump = {}; bestClasEst = mat(zeros((m,1)))
	minError = inf
	for i in range(n):
		rangeMin = dataMatrix[:,i].min(); rangeMax = dataMatrix[:,1].max()
		stepSize = (rangeMax - rangeMin) / numSteps
		for j in range(-1,int(numSteps)+1):
			threshVal = (rangeMin + float(j) * strpSize)
			predictedVals = stumpClassify(dataMatrix,i,threshVal,inequal)
			errArr = mat(ones((m,1)))
			errArr[predictedVals == labelMat] = 0
			weightedError = D.T * errArr
			
			
			
			if weightedError < minError:
				minError = weightedError
				bestClasEst = predictedVals.copy()
				bestStump['dim'] = i
				bestStump['thresh'] = threshVal
				bestStump['ineq'] = inequal
				
	return  bestStump,minError,bestClasEst
	
