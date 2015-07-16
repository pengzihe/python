#!/usr/bin/python
import pickle,commands,tab


###bank_card = {'119':{'password':'119','limit':10000,'borrow':0,'cash':0},'400123456':{'password':'123456','limit':35000,'borrow':0,'cash':0},'120':{'password':'120','limit':8000,'borrow':0,'cash':0},'110':{'password':'110','limit':7000,'borrow':0,'cash':0}}
def auth():  ##login_auth function
#def auth(number,password):  ##login_auth function
	with open('lock.txt','r') as f:  ##open lock.txt file
		lock = f.readlines()
	f = file('bank_info.txt','r')   ## open bank_info file
	bank_card = pickle.load(f)
	f.close()
	times = 0
	k=0
	while True:
		card_number = raw_input("Please input your card number: ").strip()
		#card_number = number
		if len(card_number) ==0:continue  # if card_number is null,please again.
		elif "%s\n" % card_number in lock:return "None"		#if card_number in lock.txt,break.
		while True:
			card_password = raw_input("Please input your password: ").strip()
			#card_password = password
			for n,p in bank_card.items():
				if n == card_number and p['password'] == card_password :  #Be sure card_number and password is right.
					#print "right"					
					k = 1
					return card_number
			if times == 2:   ##if input password is error in the third,card_number is lock.
				with open('lock.txt','a') as f:
					f.write("%s\n" % card_number)
				return "None"
			elif k==0:   ##if input password is error,please again.
				times += 1
				print "Your password is error,you have %s chances." %(3 - times)



def option(login):   ##Function of credit card 

	## query = {'400123456': [], '119': [], '120': [], '110': []}
	f = file('bank_info.txt','r')   ## open bank_info file
	BANK_CARD = pickle.load(f)
	f.close()
	q = file('query.txt','r')   ##open inquiries file
	query = pickle.load(q)
	q.close()
	limit = BANK_CARD[login]['limit']
	while True:
		print """Option info: 
			1. Cash
			2. Inquiries
			3. Repayment
			4. Transfer
			5. Exit
		"""
		sn = raw_input("please select the serial number: ")
		if sn == '1':    ##Cash
			cash = int(raw_input("Please enter the cash you want to go and bank charge is 5%. "))
			if limit < cash:
				print "Over quota,your quota is %d " % limit
			else:
				limit = limit - (cash + cash * 0.05)
				BANK_CARD[login]['limit'] = limit   ## credit limit
				BANK_CARD[login]['borrow'] += (-cash + -cash * 0.05)  ##credit card payments
				BANK_CARD[login]['cash'] += cash     # personal cash 
				f = file('bank_info.txt','w')   ## open bank_info file
				pickle.dump(BANK_CARD,f)        # record cash info.
				f.flush()
				#f.close()
				current_time = commands.getoutput("date +%T_%F")
				query[login].append("Cash %s and bank charge is %s in %s" % (cash,cash * 0.05,current_time))  #record cash info to query.txt
				q = file('query.txt','w')   ## open bank_info file
				pickle.dump(query,q)        # record cash info.
				q.flush()
				q.close()
				print "Cash %s is successful and bank charge is %s." % (cash,cash * 0.05)

				
		elif sn == '2': #Inquiries
			f = file('bank_info.txt','r')   ## open bank_info file
        		BANK_CARD = pickle.load(f)
        		f.close()
			for i,j in query.items():
				 if i == login:
					values = 1
					for k in j:
						print k
					print "Your credit limit have",BANK_CARD[login]['limit']
					print "Your credit card payments is",BANK_CARD[login]['borrow']
					print "Your cash is",BANK_CARD[login]['cash']


		elif sn == '3':  #Repayment
			repayment = int(raw_input("Pleases input your repayment amount: "))
			BANK_CARD[login]['borrow'] += repayment
			BANK_CARD[login]['limit'] += repayment
			f = file('bank_info.txt','w')   ## open bank_info file
                        pickle.dump(BANK_CARD,f)        # record cash info.
                        f.flush()
			f.close()
			current_time = commands.getoutput("date +%T_%F")
                        query[login].append("Repayment of %s yuan in %s" % (repayment,current_time))  #record cash info to query.txt
                        q = file('query.txt','w')   ## open bank_info file
                        pickle.dump(query,q)        # record cash info.
                        q.flush()
                        q.close()		
			print "Repayment of %s yuan is successful." % repayment	


		elif sn == '4':   #Transfer
			transfer_account = raw_input("Please input your transfer account: ")
			if transfer_account in BANK_CARD.keys():
				transfer_amount = int(raw_input("Please input your transfer amount: "))
				if BANK_CARD[login]['cash']  > transfer_amount:
				   	BANK_CARD[login]['cash'] -= transfer_amount
				   	BANK_CARD[transfer_account]['cash'] += transfer_amount
					f = file('bank_info.txt','w')   ## open bank_info file
                               		pickle.dump(BANK_CARD,f)        # record cash info.
                                	f.flush()
                                	f.close()
					current_time = commands.getoutput("date +%T_%F")
					query[login].append("Transfer %s yuan  in %s" % (transfer_amount,current_time))  #record cash info to query.txt
					query[transfer_account].append("Receive %s transfer %s yuan in %s" % (login,transfer_amount,current_time))  #record cash info to query.txt
                               		q = file('query.txt','w')   ## open bank_info file
                                	pickle.dump(query,q)        # record cash info.
                                	q.flush()
                                	q.close()
					print "you transfer %s yuan is successful." % transfer_amount
				   	
				else:
					print "The cash is over quota, you have cash is %s." % BANK_CARD[login]['cash'] 
			else:
				
				print "The account of %s is not exist." % transfer_account
				
				
			


		elif sn == '5':   #Exit
			return "exit"
		else:  ##Inpur error
			print "The option is not exists,again."
				

		
		

if __name__ == "__main__":
	#card_number = raw_input("Please input your card number: ").strip()
	#card_password = raw_input("Please input your password: ").strip()
	login_auth = auth()
	#login_auth = auth(card_number,card_password)
	if login_auth != "None":
		print "Welcome to ATM,", login_auth
		option(login_auth)
	else:
		print "The card is lock,please unlock."
	
