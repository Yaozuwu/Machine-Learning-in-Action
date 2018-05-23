from numpy import *
from Tkinter import *
import regTrees
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkSAgg
from matplotlib.figure import Figure
def reDraw(tolS,tolN):
	pass

	
def drawNewTree():
	pass
	
root  = Tk()

Label(root,text ="plot Place Holder").grid(row=0,columnspan = 3)
Label(root text = "tolN").grid(row = 1,column = 0)
tolNentry = Entry(root)
tolNentry.grid(row = 1,column = 0)
tolNentry.insert(0,'10')
Label(root,text="tolS").grid(row=2,column = 0)
tolSentry = Entry(root)
tolSentry.grid(row = 2,column = 1)
tolSentry.insert(0,'1.0')
Button(root,text="ReDraw",command=drawNewTree).grid(row=1,column=2,rowspan=3)
chkBtnVar = IntVar()
chkBtn = cheackbutton(root,text="Model Tree",varible = chkBtnVar)
chkBtn.grid(row=3,column=0,columnspan=2)

reDraw.rawDat = mat(regTrees.loadDataSet('sine.txt'))
reDraw.testDat = arange(min(reDraw.rawDat[:,0]),max(reDraw.rawDat[:,0]),0.01)

reDraw(1.0,10)
root.mainloop()


def reDraw(tolS,tolN):
	reDraw.f.clf()
	reDraw.a = reDraw.f.add_subplit(111)
	if chkBtnVar.get():
		if tolN < 2:
			tolN = 2
		myTree = regTrees.createTree(reDraw.reDat,regTrees.modelLeaf,regTrees.modelErr(tolS,tolN))
		yHat = regTrees.createForeCast(myTree,reDraw.testDat,regTrees.modelTreeEval)
	else:
		myTree = regTrees.createTree(reDraw.rawDat[:,0],reDraw.rawDat[:,1],s=5)
		reDraw.canvas.show()
	
def getInputs():
	try:
		tolN = int(tolNentry.get())
	except:
		tolN = 10
		print "enter Integer for tolN"
		tolNentry.delete(0,END)
		tolNentry.insert(0,'10')
	try:
		tolS = float(tloSentry.get())
	except:
		tolS = 1.0
		print"enter Float for tols"
		tolSentry.delete(0,END)
		tolSentry.insert(0,'1.0')
	return tolN,tolS
	
deg drawNewTree():
	tolN,tolS = getInputs()
	reDraw(tolS,tolN)
