import datetime


def get_time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    return Time

def get_date():
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)

    date = day+":"+month+":"+year
    return date
def wishing():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<12:
        wish = "Good Morning"
    elif hour>=12 and hour<15:
        wish = "Good Afternoon"
    elif hour>=15 and hour<19:
        wish = "Good Evening"
    else :
        wish = "Good Night"
    return wish


#while True:
print("The Time is:",get_time())
    #time.sleep(1)
print("date is:",get_date())
print(wishing())

    