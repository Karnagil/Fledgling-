def prove_palindrome(palindrome=input('enter word or phrase: ' ' ')):
       '''takes an input and (if letters only)tells you whether or not it is a palindrome.
	   If the input has characters that are not letters(as well as spaces) alongside letters,
	   those characters will be removed and the remaining letters will be analyzed as in first sentence.'''
       alphabet='aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
       lex={}
       space='Space'
       inp=palindrome
       for ex in inp:
       	pal=''.join(ex for ex in inp if ex in alphabet)
       for sub in inp:
               if sub==' ':
               	sub=space
               if sub not in pal and sub!=lex:
               	lex[sub]=1
               if sub in lex and sub not in pal:
               		lex[sub]=lex[sub]+1
       if inp!=pal:
       	print('Extracted character(s) of input:',pal)
       	print('Subtracted character(s) of input:',lex)             		
       pal2=pal[::-1]
       '''Tells whether or not the analyzed input is a palindrome.'''
       if pal==pal2:
	   		             print(pal,'is a palindrome')
       if pal!=pal2:
	   		            print(pal,'is not a palindrome')
	   		                            

prove_palindrome()
