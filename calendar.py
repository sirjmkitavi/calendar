import time
import calendar

def calendar():
    import time
    import calendar
    localtime1 = time.localtime(time.time())
    localtime = time.asctime(time.localtime(time.time()))
    cal = calendar.month(localtime1.tm_year,localtime1.tm_mon)
    print localtime
    print cal

def get_time():
    isValid = False
    while not isValid:
        event_time = raw_input("Enter date as yyyy-mm-dd :")
        try:
            dt = time.strptime(event_time, '%Y-%m-%d')
            isValid = True
        except:
            print "Invalid date format /n"
    return '{0}-{1}-{2}'.format(dt.tm_year,dt.tm_mon,dt.tm_mday)

def enter_eventname():
    event_name = raw_input("Enter name of event :")
    return event_name


def event():
    n = input("Enter 0 to view all events or 1 to create new input and 2 to view last event:")
    if n == 1:
        event_details2 = [get_time(),enter_eventname()]
        print "You entered"
        print event_details2
        f = open("event.txt",'a')
        f.write("Event date :"+format(event_details2[0])+"\t"+"Event name :"+format(event_details2[1]) + "\n")
        f.close()
    elif n ==2:
        f = open("event.txt",'r')
        last = open('event.txt', 'r').read().count("\n")
        i = 1
        for line in f:
            if i == last:
                break
            i += 1
        # line now holds the line
        # (or is empty if the file is smaller than that number)
        print line
    elif n ==0:
        f = open("event.txt",'r')
        for line in f:
            print line
    else:
        print "Wrong choice"

calendar()

def run():
    while True:
        choice = raw_input("Enter c to continue or q to quit :")
        if choice == "c":
            event()
        elif choice == "q":
            return

if __name__ == "__main__":
    run()