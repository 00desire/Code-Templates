### Multiprocessing code templates written by Ivan
from multiprocessing import Process, Queue, Manager, Value, Array

## Using Manager Items
## Manager is used to control flags in parallel processes, best used for flags with no time requirements
processManager = Manager()
processManager_dict = processManager.dict()
processManager_dict['run'] = True
processManager_dict['Start'] = False 

## Using Value and Array items are best for flags with time requirements
processValue = Value('i',9) ## first argument is value type ## second argument is the corresponding value of the type
processArray = Array('i',[9,9,9]) ## first argument is value type ## second argument is the corresponding value of the type

## Queues
processQueue = Queue()				## not to confuse with the queue.Queue library in Python which is meant for multithreading
## Add an item to queue
processQueue.put([9,9,9])
## Get an items from queue
item = processQueue.get()

##########################################################################################
## Class style of process declaration
## Perform all inferencing and returns np array
class TemplateProcess(Process):

    def __init__(self,inputs,outputs): 
        super(TemplateProcess, self).__init__()
   		
   		## Connect shared memory to process here
        self.inputs = inputs
        self.outputs = outputs 

    def init(self):
    	self.running = True

    def run(self): 
        ## Initialisions functions here
        self.init()

        ## Main loop
        while self.running:
        	## Perform some actions
        	pass
        	self.functions()

    def functions(self):
    	## Internal functions for the process
        pass

## Create the process
newProcess = TemplateProcess(inputs=processManager_dict, outputs=processQueue)
newProcess.start()

## Kill process by ending the while loop and calling .join/.terminate of the process
newProcess.running = False
newProcess.join()
# newProcess.terminate()

##############################################################################################
## Function Style of process declaration
def TemplateProcess(inputs, outputs):

	## Internal functions for the process
	def functions(inp):
		return inp

	## perform all initialisation here
	running = True

	while running:
		function_output = functions(inputs)

## Create the process
newProcess = Process(target=TemplateProcess, args=(processManager_dict, processQueue))
newProcess.daemon = True
newProcess.start()

## kill process by ending its while loop
## find a way to end it through the shared memory arguments
newProcess.join()
newProcess.terminate()
