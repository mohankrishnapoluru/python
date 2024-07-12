month =  input("Enter the name of the month:")
day   =  int(input ("Enter the day number:"))

if(month=="Mar"and day>19)or(month=="Apr")or(month=="May")or(month=="Jun" and day<21):
    season = 'summer'
elif(month=="Jun"and day>20)or(month=="Jul")or(month=="Aug")or(month=="sep" and day<22):
    season = 'Spring'
elif(month=="Sep"and day>21)or(month=="Oct")or(month=="Nov")or(month=="Dec" and day<21):
    season = 'Fall'
else:
    season = 'Winter'
print("The Season is currently",season)
                                                               
