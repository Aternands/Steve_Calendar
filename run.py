from steveplan import *

try:
   import cPickle as pickle
except:
   import pickle


print "\n"
print "Welcome to the self-adjusting calendar app.\n"
print "\n"

while True:

	entry = raw_input("Please choose an option: [p] = make project; [e] = make event\n"
					"[t] = make task; [r] = make report; [x] = exit\n") 

	if entry == "x":
		break

	elif entry == "p":
		make_project()
	elif entry == "e":
		make_event()
	elif entry == "t":
		make_task()
	elif entry == "r":
		report()
	else:
		print "invalid entry"




