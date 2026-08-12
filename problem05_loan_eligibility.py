# Check whether a person is eligible for a loan based on age and income

nam= input("enter the name")
age=int(input("enter your age"))
income=int(input("enter your income"))

if(age<18 or income<5000):
    print("not eigible for loan")


elif(age>=18 and income>=5000):
    print("eligible for loan")
else:
    print("invalid details")
