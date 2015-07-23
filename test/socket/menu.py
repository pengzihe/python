#!/usr/bin/python

import tab

def title(title_name):
	#title_name = ['Choose the host', 'Choose the group','View all hosts','Exit']
	n = 1
	print "Menu info:\n"
	for v in title_name:
		print "\t%s.\t%s" % (n,v)
		n += 1

	choose = raw_input("\nPlease input your choose: ").strip()
	return choose






