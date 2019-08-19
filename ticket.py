def tickets(people):

    vas_mon = []

    for item in people:
        if item == 25:
            vas_mon.append(item)
        if item == 50:
            if 25 in vas_mon:
                vas_mon.append(item)
                vas_mon.remove(25)
            else:
                return 'NO'
        if item == 100:
            if vas_mon.count(25) >= 3 and 50 not in vas_mon:
                vas_mon.append(item)
                vas_mon.remove(25)
                vas_mon.remove(25)
                vas_mon.remove(25)
            elif (25 in vas_mon) and (50 in vas_mon):
                vas_mon.append(item)
                vas_mon.remove(25)
                vas_mon.remove(50)
            else:
                return 'NO'
        print("Insert: {}".format(item))
        print(vas_mon)
    return 'YES'


print(tickets([25,50,25,100,25,50,25,100,25,25,25,100,25,25,50,100,25,25,25,100]))