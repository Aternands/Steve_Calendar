from steveplan import *
import os.path
try:
   import cPickle as pickle
except:
   import pickle



if os.path.isfile("stored_calendar.p") == True:
	with open('stored_calendar.p') as f:
		event_list, task_list, project_dict = pickle.load(f)
		
else:
    event_list = []
    task_list = []
    project_dict = {"Unassigned":[None]}





print "\n"
print "Welcome to the self-adjusting calendar app.\n"
print "\n"

while True:

	entry = raw_input("Please choose an option: [p] = make project; [e] = make event\n"
					"[t] = make task; [r] = make report; [x] = exit\n") 

	if entry == "x":
		with open("stored_calendar.p", "wb") as f:
			pickle.dump([event_list, task_list, project_dict], f)
		break

	elif entry == "p":
		make_project(project_dict)
	elif entry == "e":
		make_event(event_list, project_dict)
	elif entry == "t":
		make_task(task_list, project_dict)
	elif entry == "r":
		report(task_list,event_list,project_dict)
	else:
		print "invalid entry"


	