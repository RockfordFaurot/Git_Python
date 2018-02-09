#create 100 widgites as fast as possible:
#get several workers to make a widget include a delay for each worker:
#start by writing to difrent documents, 
#then write to the same document onec you get that figured out. 
import time 
import threading 

#set up a file to read and write to:
#file needs to already exist in order to use "r+" read and write function
work_file = open("/Users/rockfordfaurot/Documents/Programing/Python/Git_Python/Threading_file.txt", "r+")

#create worker class:
class Worker(object):		#object is necisary to call __init__ during inharitince
	def __init__(self, pace):
		self.pace = pace	#this is how long it take to work
		self.task = 0
	def run(self):
		while self.task < 10:
			self.task+=1
			time.sleep(self.pace)
			work_file.write("Task "+str(self.task)+" has been accomplished.\n")
			#print("Task "+str(self.task)+" has been accomplished.")

class Worker2(object):
	def __init__(self, pace):
		self.pace = pace
		self.jobs = 0
	def run(self):
		while self.jobs < 8:
			self.jobs+=1
			time.sleep(self.pace)
			work_file.write("Job "+str(self.jobs)+" has been completed.\n")
			#print("Job "+str(self.jobs)+" has been compleated.")

class SuperViser(Worker):
	def __init__(self, pace):
		self.pace=pace
		self.count=0
	def check(self):
		while self.count < 5:
			self.count+=1
			time.sleep(self.pace)
			work_file.write("Work Harder!!\n")
			#print("Work Harder!!!!")



Jim = Worker(1)
Steve = Worker2(1.5)
Jhon = SuperViser(2)
Jim.run()
Steve.run()
Jhon.check()
work_file.close()

#you need this statment to preforme multithreading:

# if __name__ == '__main__':
# 	NumOfThreads = 4
# 	threadList = []
# 	t = threading.Thread(target=function, args=(tup,))
# 	t.start()
