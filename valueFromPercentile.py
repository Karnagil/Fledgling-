#get the value of an array/list via it's percentile:

class dresun999():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.y.sort()
    def perval(self):
        a=self.y
        b=int((len(a)/100)*self.x)
        print(a[b-1])
               
x=[5,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31] 

dresun999(75,x).perval()

        
   
