Numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
Count_Odd = 0
Count_Even = 0
for v in Numbers:
        if not v % 2:
    	     Count_Even+=1
        else:
    	     Count_Odd+=1
print("Number of Even Numbers :",Count_Even)
print("Number of Odd Numbers :",Count_Odd)
