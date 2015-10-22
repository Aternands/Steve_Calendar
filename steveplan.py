import datetime
import time




#<------------------------------Global Variables---------------------------------------------->


# event_list = []

# task_list = []

# project_dict = {"Unassigned":[None]}



#<------------------------------Class Definitions----------------------------------------------->


class Event:
	'''An individual event'''

	def __init__(self,description,year,month,day,duration):
		self.description = description
		self.date = datetime.date(year,month,day)
		self.duration = duration

	def change_date(self,year,month,day):
		self.date = datetime.date(year,month,day)

	def change_duration(self,duration):
		self.duration = duration


class Task:
	'''An individual task'''

	def __init__(self,description,duration):
		self.description = description
		self.duration = duration

	def change_duration(self,duration):
		self.duration = duration


#<------------------------------Functions----------------------------------------------->


def make_project(project_dict):

	project = raw_input("Please enter the project's name:\n")
	project_dict[project] = [None]
	print "Project has been saved.\n"
	return project_dict



def make_event(event_list, project_dict):

	#creates event object
	description = raw_input("Enter event description:\n") 
	year = int(raw_input("Enter year in YYYY format:\n"))
	month = int(raw_input("Enter month in MM format:\n"))
	day = int(raw_input("Enter day in DD format:\n")) 
	duration = float(raw_input("Enter event duration in hours:\n"))

	a = Event(description,year,month,day,duration)

	#adds event object to event list, re-sorts event list by date
	
	event_list.append(a)
	event_list.sort(key=lambda x: x.date)

	has_project(a, project_dict)

	print "Event has been saved.\n"
	return event_list

	



def make_task(task_list, project_dict):

	#creates task object
	description = raw_input("Enter task description:\n") 
	duration = float(raw_input("Enter task duration in hours:\n"))

	a = Task(description,duration)

	#adds task object to task list in order of priority
	
	if len(task_list) == 0:
		task_list.append(a)
	elif len(task_list) != 0:
		print "Here are the current incomplete tasks in order of priority:\n"
		n = 1
		for i in task_list:
			print str(n) + ":   " + i.description
			n += 1
		priority = int(raw_input("What priority would you like to assign to this new task? Please enter a positive integer:\n"))
		task_list.insert(priority-1,a)

	has_project(a, project_dict)

	print "Task has been saved.\n"
	return task_list




	
def has_project(item, project_dict):


	should_assign = (raw_input("Would you like to assign this entry to a project? Enter y/n:\n"))

	if should_assign == "n":
		if project_dict["Unassigned"] == [None]:
			project_dict["Unassigned"] = [item]
		else:
			project_dict["Unassigned"].append(item)
		print "Your entry is not assigned to a project."

	elif should_assign == "y":
		if len(project_dict) == 1:
			print "There are no current projects.\n"
		elif len(project_dict) > 1:
			print "Here are the current projects:\n"
			for i in project_dict:
				if i != "Unassigned":
					print i + "\n"
		chosen_project = raw_input("Please enter the project you'd like to assign this entry to:\n")
		if chosen_project not in project_dict:
			should_add = raw_input("This isn't one of the current projects. Would you like to add it as a new project? Enter y/n:\n")
			if should_add == "y":
				project_dict[chosen_project] = [item]
				print "Project and entry added."
			if should_add == "n":
				has_project(item, project_dict)
		elif chosen_project in project_dict:
			if project_dict[chosen_project] == [None]:
				project_dict[chosen_project] = [item]
			else:
				project_dict[chosen_project].append(item)
			print "Entry added to project."
	return project_dict


def add_project(project_entered, item, project_dict):


	should_add = raw_input("This isn't one of the current projects. Would you like to add it as a new project? Enter y/n:\n")
	if should_add == "y":
		project_dict[project_entered] = [item]
		print "Project and entry added."
		return project_dict
	if should_add == "n":
		return project_dict

#<------------------------------Reports----------------------------------------------->

def report(task_list,event_list,project_dict):

	print "Generating report....\n"
	time.sleep(2)

	fin = open("Schedule_Report.txt", "w")

	fin.write("Tasks and Events (by Project):\n")

	fin.write("\n")

	for key in project_dict.keys():
		fin.write("%s" % key.upper())
		fin.write("\n")
		for i in project_dict[key]:
			if i == None:
				pass
			else:
				fin.write("%s   " % i.description)
				fin.write("%s hrs  " % i.duration)
			fin.write("\n")
		fin.write("\n") 

	print "Report has been generated. Open 'Schedule_Report.txt' to review.\n"

	fin.close()


	

