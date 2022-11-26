dd1=int(input("Enter Date of Birth"))      #Taking Inputs from the user
mm1=int(input("Enter Month of Birth "))
yyyy1=int(input("Enter Year of Birth "))
dd2=int(input("Enter Todays Date "))
mm2=int(input("Enter Present Month "))
yyyy2=int(input("Enter Present Year "))


#Intializing an array with the number of days in all the 12 months
monthDays = [31, 28, 31, 30, 31, 30,     
             31, 31, 30, 31, 30, 31]


#Defining a function to count the number of leap years 
def countleapyears(x,y):

    if x<=2:
        y-=1
    #A leap year should be a multiple of 4 and 400 but should not be a multiple of 100
    #so the below formula is used to calculate the number of leap years
    return int(y / 4) - int(y / 100) + int(y / 400)


#Defining a function to calculate the number of days till the given date
def getn(a,b,c):
    #Multiplying the Number of years with 365 and adding the number of days in the current month
    n1=c*365+a

    #Using a for loop to add the days of all the previous months in the given year
    for i in range(0,b-1):
        n1 += monthDays[i]
   
   #Adding the Number of Leapdays by calling the countLeapyear function
    n1+=countleapyears(b,c)
    
    #Returns the number of days passed till the given date
    return(n1)
#Finding the number of days passed till the date of birth
a=getn(dd1,mm1,yyyy1)

#Finding the number of days passed till the Peresent date
b=getn(dd2,mm2,yyyy2)

#The total number of days survived is the difference between a and b
ans=("You have survived",b-a,"Days")
print(ans)

    

    
