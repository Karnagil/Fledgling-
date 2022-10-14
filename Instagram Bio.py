"Instagram Bio Description Source Code:".center(1,"\"")

numbers=84,104,101,32,69,120,101,99,117,116,105,111,110
for number in numbers:
        print(chr(number), end="")
print(":")

titles=["Software Engineer","Machine Learning(A.I.) Expert","Web Developer","Artist","Designer","Writer"]
declaration="I am a"
vowel="A","a","E","e","I","i","O","o","U","u"

for title in titles:
    if title.startswith(vowel):
        new_declaration=declaration+"n"
        print(new_declaration,title)
    else:
        print(declaration,title)