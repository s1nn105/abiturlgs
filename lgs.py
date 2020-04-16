ROW_MIN =1 # shouldent be 0 otherwise the lgs might be impossible to solve or to easy to solve
ROW_MAX=10
ROW_MAX_SCALE = 4
OB_ITER = 3 # defines the amount of operations that are done to obfusecate the step form (?)
import random
class lgs3:
	def __init__(self,x1,x2,x3):
		self.x1=x1
		self.x2 = x2
		self.x3=x3

		self.row1 = [x1,x2,x3,None]
		self.row2 = [x1,x2,x3,None]
		self.row3 = [x1,x2,x3,None]


def solve_row(row,sa):
	d = sum([row[i]*sa[i] for i in range(3)])

	row[3]=d 
	return row

def add_rows(row1,row2):
	return [row1[i]+row2[i] for i in range(4)]
def substract_rows(row1,row2):
	return [row1[i]-row2[i] for i in range(4)]

def scale_row(row,f):
	return [row[i]*f for i in range(4)]

def change_rows(rows):
	return random.shuffle(rows)
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
def minimize(row):
	#to avoid getting to big numbers here a semi random approach to get the numbers small again
	x,y,z,j =row
	print(x,y,z,j)		
	# division results are always floats in python. If you int a float you will just cut off the anything behind the ,. therefor 
	# int(6/4)==1 and int(6/4)!= 6/4 but if int(6/3) == 6/3 then the result of the division is in N
	for i in range(2,11):
		if int(x/i) == x/i:
			if int(y/i) == y/i:
				if int(z/i) == z/i:
					return [x/i,y/i,z/i,0]
	return row


def add_scaled(row1,row2):
	return add_rows(row1,scale_row(row2,random.randint(2,ROW_MAX_SCALE)))
def obfusecate(rows):
	rows[2] = add_scaled(rows[2],rows[0])
	rows[1] = add_scaled(rows[2],rows[0])
	for i in range(OB_ITER):
		r =randint(0,4)
		if r ==0:
			ro = random.randint(0,3)
			rows[ro] = scale_row(rows[ro],random.randint(ROW_MAX_SCALE))
		elif r==1:
			ro1 = random.randint(0,3)
			ro2 = random.randint(0,3)
			rows[ro1] =add_rows(rows[ro1],rows[ro2])
		elif r==2:
			ro1 = random.randint(0,3)
			ro2 = random.randint(0,3)
			rows[ro1] =substract_rows(rows[ro1],rows[ro2])			
		elif r==3:
			rows = change_rows(rows)

		elif r==4:
			ro = random.randint(0,3)
			rows[ro] = minimize(rows[ro])	

	return rows
