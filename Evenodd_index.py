
import operator
def CharAt_Even_Odd_Index(S,N):
       Evenchar=[ ]
       Oddchar=[ ]
  if N>=2 and N<=10000:      
         for char in S:
          index=S.find(char)
          if  operator.eq(index  %  2,  0):
               Evenchar.append(char)       
          elif operator.ne(index % 2,  0):
                
 print(Evenchar)   
 print(Oddchar)       

             
                          
                                                    
 
 
 def displayEven(Evenchar):
       print(Evenchar)
       for char in Evenchar:
             print(char, end='  ')
             print('  ', end='  ')

def  displayOdd(Oddchar):
       print(Oddchar)
       for char in Oddchar:
             print(char, end='  ')
           

                     
                                                                                                   
S=[ '2' ,'Hacker','Rank']
for s in S:
      N=len(s)
      CharAt_Even_Odd_Index(s,N)