ROW_MIN =0
ROW_MAX=20
import random
class lgs3:
	def __init__(self,x1,x2,x3):
		self.x1=x1
		self.x2 = x2
		self.x3=x3

		self.row1 = [x1,x2,x3,None]
		self.row2 = [x1,x2,x3,None]
		self.row3 = [x1,x2,x3,None]



def add_rows(row1,row2):
	return [row1[i]+row2[i] for i in range(4)]

def scale_row(row,f):
	return [row[i]*f for i in range(4)]

def create_row(filled):
	#filled give information how many 0 are in a row
	# filled =0 means the row is full (no 0)
	#filled = 3 0 0 0
	#filled >3 is ridiculus
	# 0 are always leading e.G 0,0,3 not 3,0,0
	rowT = [random.randint(ROW_MIN,ROW_MAX) for i in range(3)]
	for i in range(filled):
		rowT[i]=0
	rowT.append(0)
	return rowT

	
