#!/usr/bin/python

class DefaultService:
	name = None
	interval = 300
	monitor_dic = {}
	graph_dic = {}
	data_from = 'agent'
	warning_retry = 3
	critical_retry = 1

#if this sets to rmpty, all the status will be caculated in > mode, gt =>
	lt_operator = []
