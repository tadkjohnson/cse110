
with open("hr_system.txt") as hr_information:    #opens txt file and gives it a new name  does this look up 1 level for the file?
    next(hr_information)    #skips the first line whicch is the header line

    for line in hr_information:  #start to loop 
        hr_list = line.split(" ")   #seperates the line of information at the space 
        name = hr_list[0] #assigns first item in list is the name
        idnum = int(hr_list[1])
        title = hr_list[2]
        salary = float(hr_list[3])

        paycheck = (salary / 24)
        if title.lower() == "engineer":
                paycheck += 1000


        print (f"{name.capitalize()} (ID: {idnum}), {title.capitalize()} ${salary:.2f} ${paycheck:.2f}")




 







