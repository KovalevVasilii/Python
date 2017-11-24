
def quad(a, n): #квадрат
    if n==2:
        return a*a
    if n==1:
        return a
    if n%2!=0:
        a =a*quad(a,n-1)
    else:
        a = quad(a*a,n//2)
    return a
 
def NOD(a,b): #наибольший общий делитель
    while a!=0 and b!=0:
        if a > b:
         a = a % b
        else:
         b = b % a
    return a+b
 
def ratio(num,den): #приведение дробей
    if num==den:
        return 1
    nod = NOD(num,den)
    num = num/nod
    den = den/nod
    if den==1:
        return num
    else:
         return num,den
   
#def quickSort(arr, l,r): #quickSort
    #if l <r:
        #p = partition(arr,l,r)
        #quickSort(arr,l, p-1)
        #quickSort(arr, p+1,r)

#def partition(arr,l,r):
   # pivot = arr[r]
   # i = l-1
   # for j in range(l,r-1):
     #if arr[j] <= pivot:
       # i= i+1
       # arr[i], arr[j] = arr[j], arr[i]
  #  arr[i+1], arr[r] = arr[r], arr[i+1]
   # return i+1


   # if a=='0':
     # return
   # else:
         #if (int(a)%9==0 or int(a)%3==1):
           # flag =flag+1
       #  else:
          #  flag =0
        # if (int(a)%4==0 or int(a)%8==1):
          #  flag =flag+1
       #  else:
          #   flag =0
     #
       #  for i in num:
          #  if i == a[len(a)-1]:
             #   flag=0
             #   break

def quickSort(array):  #quickSort
    less = []
    equal = []
    more = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                more.append(x)
        return quickSort(less)+equal+quickSort(more)  
    else:  
        return array

def strange_func(): #основан на том, что квадрат целого числа n есть последовательная сумма n нечётных целых чисел
   
    num =['2','3','7','8']
    sqr=0
    flag =0
    a=input("")
    if a=='0':
      return
    else:
       i =1
       while(sqr + 2 <= int(a)):
            sqr += i
            i+=2
    strange_func()
    if sqr==int(a) or sqr==1:
     print(a)
    


class HanoiTower:
     def __init__(self, size):
        self.size = size
        self.tower1 =[]
        self.tower2 =[]
        self.tower3 =[]
        self.top1 =size
        self.top2 =0
        self.top3 =0
        self.moves =0
     def Fill(self):
         i=0
         for i in range(0,self.size):
            self.tower1.append(self.size-i)
         for i in range(0,self.size):
            self.tower2.append(0)
         for i in range(0,self.size):
            self.tower3.append(0)
         #print(self.tower1)
         return 0
     def HT(self,tower1,tower2,tower3,
		 top1, top2, top3, count):
         if (count == 1):
             self.Move(tower1, tower2,top1,top2)
         else:
             self.HT(tower1,tower3,tower2,top1,top3,top2, count-1)
             self.Move(tower1, tower2, top1, top2)
             self.HT(tower3, tower2, tower1, top3, top2, top1, count-1)
     def Move(self, tower1, tower2, top1, top2):
         tower2[top2] = tower1[top1-1]
         top1 = top1-1
         top2 = top2+1
         self.moves= self.moves+1
     def HanoiSearch(self):
        self.HT(self.tower1,self.tower2,self.tower3, self.top1, self.top2, self.top3, self.size)
        print(moves)

     
     def Print(self):
          print("1 - ")
          print(self.tower1)
          print("2 - ")
          print(self.tower2)
          print("3 - ")
          print(self.tower3)



tower = HanoiTower(5)
#print(tower.size)
tower.Fill()
tower.Print()
tower.HanoiSearch()
tower.Print()
#strange_func()



#print(ratio(36,10))
#print(quad(2,5))
#numbers = [4,3,7,33,17,33]
#new=quickSort(numbers)
#numbers=quickSort(numbers,1,len(numbers)-1)
#print(new)