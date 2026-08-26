
"""
rows=int(input("rows:"))
if rows>0:
    for rownum in range(1,rows+1):
       print("0" *(rownum-1),f'{rownum}',sep="")
else:
    print("rows value never be -ve")
 
"""  
"""
rows=int(input("rows:"))
if rows>0:
    data=1
    for rownum in range(1,rows+1):
        print(*range(data,data+rownum))
        data=rownum
else:
    print("rows value never be -ve")?"""

"""    
example:5
rows=int(input("rows:"))
if rows>0:
    cpr=rows
    for rownum in range(1,rows+1):
        print(*range (1,cpr+1))
        cpr-=1
else:
    print("rows value never be -ve")"""

"""
example:6
rows=int(input("rows:"))
if rows>0:
    cpr=rows
    for rownum in range(1,rows+1):
        print(*range (cpr,0,-1))
        cpr-=1 
else:
    print("rows value never be -ve")"""
   
""""  
example:7  
rows=int(input("rows:"))
if rows>0:
    for rownum in range(1,rows+1):
        print("*"*rownum)
else:
    print("rows value never be -ve")"""

"""  
example:8  
rows=int(input("rows:"))
if rows>0:
    cpr=rows
    for rownum in range(1,rows+1):
        print("*"*cpr,sep=" ")
        cpr-=1
else:
    print("rows value never be -ve")"""

""""
example:9
rows=int(input("rows:"))
if rows>0:
    for rownum in range(1,rows+1):
        print(" "*(rows-rownum),*range(1,rownum+1))
else:
    print("rows value never be-ve")"""
    
"""  
example:10  
rows=int(input("rows:"))
if rows>0:
    for rownum in range(1,rows+1):
        print(" "*(rows-rownum),"*" * (rownum),"*" *(rownum-1) ,sep="")
else:
    print("rows value never be-ve") """   

"""
example:11
rows=int(input("rows:"))
if rows>0:
    cpr=rows
    for rownum in range(1,rows+1):
        print(" "*(rownum),*range(1,cpr+1))
        cpr-=1
else:
    print("rows value never be -ve")"""

"""
example:12
rows=int(input("rows:"))
if rows>0:
    for rownum in range(1,rows+1):
        print(*range(rows,rows-rownum,-1)) 
else:
    print("rows value never be -ve ")"""
 
"""
rows=int(input("rows:"))        
if rows>0:
    cpr=rows
    for rownum in range(1,rows+1):
        print(f'{cpr}'*cpr+1)
        cpr-=1
else:..
    print("rows never be -ve")"""
    
"""
example:13
rows=int(input("rows:"))  
if rows>0:
    cpr=rows
    for rownum in range(1,rows+1):
        print("*" *cpr,sep="")
        cpr=rows
        
else:
    print("rows never be -ve")"""
    
"""  
example:14  
rows=int(input("rows:"))
if rows>0:
    cpr=rows
    for rownum in range(1,rows+1):
        
        print("*"*cpr,sep=" ")
        cpr-=1
else:
    print("rows never be -ve")"""

"""
1
10
101
1010
10101
 
rows=int(input("rows:"))
if rows>0:
    for rownum in range(1,rows+1):
        if rownum%2==0:
            print("10"*(rownum//2))
        else:
            print("10"*(rownum//2),"1",sep="")
        
else:
    print("rows never be -ve")"""
    
"""   
101010
010101
101010
010101
101010
   
rows = int(input("rows: "))
if rows > 0:
    for rownum in range(1, rows + 1):
      if rownum%2==0: 
        print("01"*3)
      else:
        print("10"*3)         
else:
    print("rows never be -ve")"""

"""    
10000
02000
003000  
00040
000005

rows=int(input("rows:"))
if rows>0:
    for rownum in range(1,rows+1):
       print("0" *(rownum - 1) + f"{rownum}" + "0" * (rows - rownum))   
else:
    print("rows never be -ve")""" 

""""
11111
01111
00111
00011
00001

rows = int(input("rows: "))
if rows > 0:
    for rownum in range(1, rows + 1):
        print("0" * (rownum - 1) + "1" * (rows - rownum + 1))
else:
    print("rows never be -ve")"""
  
"""
  1
    2
      3  
        4  
           5
           
rows=int(input("rows:"))
if rows>0:
    cpr=rows
    for rownum in range(1,rows+1):
        print(" "*rownum,rownum,sep=" ")
else:
    print("rows never be -ve")"""

""""    
rows=int(input("rows:"))
if rows>0:
    cpr=rows
    for rownum in range(1,rows+1):
        print(rownum," "*rownum,sep=" ")
else:
    print("rows never be -ve")"""
    
"""    
for i in range(5, 0, -1):
    print(i)"""
 
"""    
for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(i, j)"""

"""
for i in range(3): 
     print(i, end=" ")"""     
        
"""
count = 0 
while count < 3: 
      print("Hi") 
count += 1 """

"""
for i  in range(2,10,3):
    print(i,end=" ")"""

"""
for ch in "Python": 
     print(ch, end="-") """
     
"""
for i in range(3):
    if i == 1:
        continue
    print(i) """
    
"""    
x = 0 
while x < 5: 
    x += 2 
print(x) """  

"""
a, b, c, count = 1, 1, 1, 0

while a <= 5:
    while b <= 5:
        while c <= 5:
            if a >= 3:
                break
            else:
                count += 60
                c += 1
        else:
            break

        if b >= 3:
            break
    else:
        count += 40
        b += 1
        b, c = 1, 1
        a += 2
        count += 20
else:
    print(count)
"""
"""
1 
2 6 
3 7 10 
4 8 11 13 
5 9 12 14 15 
rows=int(input("rows:"))
if rows>0:
    cpr=rows
    for i in range(1,rows+1):
      data=i
      for j in range(1,i+1):
          print(data,end="")
          data+=cpr
      print()   
else:
     print("rows never be -ve")
     
     
rows = int(input("rows: "))
if rows > 0:
    for i in range(1, rows+1):   
        data = i                  
        print(data, end=" ")
        space = rows - 1          
        for j in range(1, i):    
            data += space
            print(data, end=" ")
            space -= 1             
        print()
else:
    print("rows never be -ve")"""
"""       
1 
3 2 
4 5 6 
10 9 8 7 
11 12 13 14 15

rows=int(input("rows:")) 
data=1
if rows>0:
    for i in range(1,rows+1):
       print(*range(data,i+data))
       data+=i
           
else:
    print("rows never be -ve")"""
 
"""    
1
3 2
6 5 4 
10 9 8 7 
15 14 13 12 11


rows=int(input("rows:"))
data=1
if rows>0:
    for i  in range(1,rows+1):
        print(*range(i+data-1,data-1,-1))
        data +=i """
"""
1 
2 3 
6 5 4 
7 8 9 10 
15 14 13 12 11 

rows=int(input("rows:"))
data=1
if rows>0:
    for i in range(1,rows+1):
        print(*range())
""""
        
        
        
        
        
            
    
     
        
    
    


    






           
        

     
    
    
    
    


      
        
    
    
    
        
     
    

        
        
    
        

        
        
        
        
    
    
    
    
        
    
        
        
       
              
                    
                     
           
