#Pass or Fail — If marks are 40 or above, print Pass; otherwise Fail.
marks=float(input("enter your grade:-")) 
# float() is used because marks can be entered as decimal values, 
# such as 39.5 or 85.5.

if(marks>=40):
     print("pass")
else:
     print("fail")
