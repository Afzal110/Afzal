eng=int(input("Enter English Marks:"))
isl=int(input("Enter Islamiat Marks:"))
math=int(input("Enter Math Marks:"))
urdu=int(input("Enter Urdu Marks:"))
pst=int(input("Enter Pakistan Studies Marks:"))

print("\nEnglish Marks:",eng)
print("Islamiat Marks:",isl)
print("Math Marks:",math)
print("Urdu Marks:",urdu)
print("Pakistan Studies Marks:",pst)

total=eng+isl+math+pst+urdu
print ("\nTotal:",total)


perc=total/5
print("Percentage:",perc)

if perc >=80 and perc<=100:
	grd='A'
if perc >=60 and perc<80:
	grd='B'
if perc >=50 and perc<60:
	grd='C'
if perc >=40 and perc<50:
	grd='D'
print("Grade:",grd)






