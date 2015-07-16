#!/usr/bin/python
import tab,login_v2,pickle,commands
global shop_list,shopping_cart 
shop_list = {'coffee':70,'tv':4500,'car':200000,'book':78,'apple':30,'pay':'settlement','exit':'exit shopping'}
shopping_cart = {}
def list():
	print "\nSHOPPING LIST: "
	for s,v in shop_list.items():		
		print "\t\t%s: %s" % (s.ljust(10),v)
	print "\n"
def shopping():
	while True:
		list()
		product = raw_input("please select the product name: ")
		if product in shop_list.keys() and (product != "exit" and product != "pay"):
			amount = int(raw_input("Please enter the number you want to buy: "))
			#print "You buy the %d %s" % (amount,product)
			if product not in shopping_cart.keys():
		 		shopping_cart[product] = amount
		 		print shopping_cart
			else:
		 		shopping_cart[product] += amount
		 		print shopping_cart
		elif product == 'pay':
			total = 0.0
			for p,c in shopping_cart.items():
				money = shop_list[p] * c
				print "You buy the %d %s and you need to spend \033[32;1m%s\033[0m yuan." % (c,p,money)
				total += money	
			print "You need to spend a total of \033[32;1m%d\033[0m yuan." % total
			#print shopping_cart
			card_number = raw_input("please enter your credit card number: ")
			card_password = raw_input("please enter your password: ")
			if login_v2.auth(card_number,card_password) == card_number:
				f = file('bank_info.txt','r')   ## open bank_info file
        			bank_card = pickle.load(f)
        			f.close()
				f = file('query.txt','r')   ## open bank_info file
        			query = pickle.load(f)
        			f.close()
				if bank_card[card_number]['limit'] > total:
					bank_card[card_number]['limit'] -= total
					f = file('bank_info.txt','w')   ## open bank_info file
                                	pickle.dump(bank_card,f)        # record cash info.
                                	f.flush()
                                	f.close()
                                	current_time = commands.getoutput("date +%T_%F")
                                	query[card_number].append("Shopping cost %s yuan in %s." % (total,current_time))  #record cash info to query.txt
                                	q = file('query.txt','w')   ## open bank_info file
                                	pickle.dump(query,q)        # record cash info.
                               		q.flush()
                                	q.close()
                                	print "Shopping cost %s yuan and your credit card quota has %s." % (total,bank_card[card_number]['limit'])
				else:	
					print "Error,over quota,The card quota is %s." % bank_card[card_number]['limit']
			else:print "The credit cart number or password is error."
		elif product == 'exit':
			return "exit"
		else:
			print "The option is not exists,again."
	
	
shopping()
