#Check whether a student is eligible for campus placement based on CGPA.

nam=input("enter your name :-")
cgpa=float(input("enter your cgpa:-"))
if( cgpa<=4.0):
    print(nam,"not eligible for placement")

else:
    print(nam,"eligible for placement")
