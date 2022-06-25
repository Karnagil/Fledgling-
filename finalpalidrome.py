def prove_palindrome():
       import sys
       start='Beep...boop...beep...Konnichiwa!/Hello! ^_^\n'
       botintro='I am PALIN-CHAN: The Palindrome Checker Bot +_+'
       help1='(For help type: ##. To end the program type: #)\n'
       help2='Takes an input and (if letters only)tells you whether or not it is a palindrome.\nIf the input has characters that are not letters(including space)then those characters will be removed\nand the remaining letters will be analyzed(see first sentence).'
       palinput='Please enter the sequence you want to check:\n'
       stop='The program has stopped. Sayōnara Take care! ^.^'
       alphabet='aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
       lex={}
       space='Space'
       null='',' ',None
       extracted='Extracted character(s) of input:'
       subtracted='Subtracted character(s) of input:'
       ispal='is a palindrome'
       notpal='is not a palindrome'
       print(start)
       count=0
       while count<2000000:
       	count+=1
       	if count==600000:
       		print(botintro)
       	if count==1200000:
       		print(help1)
       while True:
       	palindrome=input(palinput)
       	inp=palindrome
       	if inp!=str():
       		if palindrome=='#':
       			print(stop)
       			sys.exit()
       		if palindrome=='##':
       			print(help2)
       		for ex in inp:
       				pal=''.join(ex for ex in inp if ex in alphabet)
       		for sub in inp:
       			     		if sub in null:
       			     			sub=space
       			     		if inp!='##' and sub not in pal and sub not in lex:
       			     			lex[sub]=1
       			     		else:
       			     		 		if inp!='##' and sub in lex and sub not in pal:
       			     		 			lex[sub]+=1
       		if inp not in ('##',pal):
       			     		 	print(extracted,pal)
       			     		 	print(subtracted,lex)
       		pal2=pal[::-1]
       		if inp!='##' and pal==pal2:
       			     		 	print(pal,ispal)
       			     		 	lex={}
       		if inp!='##' and pal!=pal2:
       		      		 		print(pal,notpal)
       		      		 		lex={}
prove_palindrome()
