# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20230484
# Date: 10.12.2023

from graphics import *

# Function to display histogram
def histogram(progress_count,trailer_count,retriver_count,exclude_count):
    total_outcomes = progress_count + trailer_count + retriver_count + exclude_count
    progess_precentage = (progress_count / total_outcomes) * 100
    trailer_precentage = (trailer_count / total_outcomes) * 100
    retriver_precentage = (retriver_count / total_outcomes) * 100
    exclude_precentage = (exclude_count / total_outcomes) * 100
    
    progress_height = 453
    if(progess_precentage != 0.0):
        progress_height = 453-(230+progess_precentage)

    trailer_height = 453
    if(trailer_precentage != 0.0):
        trailer_height = 453-(230+trailer_precentage)

    retriver_height = 453
    if(retriver_precentage != 0.0):
        retriver_height = 453-(230+retriver_precentage)

    exclude_height = 453
    if(exclude_precentage != 0.0):
        exclude_height = 453-(230+exclude_precentage)


    win = GraphWin("Histogram",400, 550)
    win.setBackground("white")
    message = Text(Point(80, 80), "Histogram Results")
    message.draw(win)

    message = Text(Point(120, 505), f"{total_outcomes} outcomes in total.")
    message.draw(win)

    line = Line(Point(360, 455), Point(10, 455))
    line.draw(win)

    shape = Rectangle(Point(100, progress_height), Point(30, 453))
    shape.setFill("#aef8a1")
    shape.setOutline("#aef8a1")
    shape.draw(win)
    message = Text(Point(65, (progress_height-10)), progress_count)
    message.draw(win)
    message = Text(Point(65, 465), "Progress")
    message.draw(win)

    shape = Rectangle(Point(185, trailer_height), Point(110, 453))
    shape.setFill("#a8e297")
    shape.setOutline("#a8e297")
    shape.draw(win)
    message = Text(Point(150, (trailer_height-10)), trailer_count)
    message.draw(win)
    message = Text(Point(145, 465), "Trailer")
    message.draw(win)

    shape = Rectangle(Point(265, retriver_height), Point(192, 453))
    shape.setFill("#a3b777")
    shape.setOutline("#a3b777")
    shape.draw(win)
    message = Text(Point(230, (retriver_height-10)), retriver_count)
    message.draw(win)
    message = Text(Point(230, 465), "Retriever")
    message.draw(win)

    shape = Rectangle(Point(340, exclude_height), Point(272, 453))
    shape.setFill("#d2b6b5")
    shape.setOutline("#d2b6b5")
    shape.draw(win)
    message = Text(Point(305, (exclude_height-10)), exclude_count)
    message.draw(win)
    message = Text(Point(310, 465), "Excluded")
    message.draw(win)

    win.getMouse()
    win.close()

# Function to write progression data to a file
def write_progression_data(file_name, progression_data):
    f = open(file_name, 'w')
    for data in progression_data:
        f.write(f"{data[0]} - {data[1]}, {data[2]}, {data[3]}\n")
        f.close

# Function to read progression data from a file
def read_progression_data(file_name):
    f = open(file_name, 'r')
    for line in f:
        print(line.rstrip('\n'))

valid_values = [0,20,40,60,80,100,120]

# List to store progression data
progression_data = []
progress_count = 0
trailer_count = 0
retriver_count = 0
exclude_count = 0

# User input to determine if student or staff
print("Are you a student or staff member?")
choosing_version = str(input("If you are a student, please enter 'student', if you are a staff member, please enter 'staff: "))

if choosing_version.lower() == "student":
    try:
    # Student input for credits
        pass_credits = int(input("\nPlease enter your credits at pass: "))
        if pass_credits in range(0, 121):
            if pass_credits in valid_values:
                defer_credits = int(input("Please enter your credits at defer: "))
                if defer_credits in range(0, 121):
                    if defer_credits in valid_values:
                        fail_credits = int(input("Please enter your credits at fail: "))
                        if fail_credits in range(0,121):
                            if fail_credits in valid_values:
                                if pass_credits + defer_credits + fail_credits == 120:
                                    if pass_credits == 120 and defer_credits == 0 and fail_credits == 0:
                                        print("Progress")
                                    elif (pass_credits == 100 and defer_credits == 20 and fail_credits == 0)or(pass_credits == 100 and
                                        defer_credits == 0 and fail_credits == 20):
                                        print("Progress(module trailer)")
                                    elif (pass_credits == 80 and defer_credits == 40 and fail_credits == 0)or(pass_credits == 80 and
                                        defer_credits == 20 and fail_credits == 20)or(pass_credits == 80 and defer_credits == 0 and fail_credits == 40)or(pass_credits == 60 and
                                        defer_credits == 60 and fail_credits == 0)or(pass_credits == 60 and defer_credits == 40 and fail_credits == 20)or(pass_credits == 60 and
                                        defer_credits == 20 and fail_credits == 40)or(pass_credits == 60 and defer_credits == 0 and fail_credits == 60)or(pass_credits == 40 and
                                        defer_credits == 80 and fail_credits == 0)or(pass_credits == 40 and defer_credits == 60 and fail_credits == 20)or(pass_credits == 40 and
                                        defer_credits == 40 and fail_credits == 40)or(pass_credits == 40 and defer_credits == 20 and fail_credits == 60)or(pass_credits == 20 and
                                        defer_credits == 100 and fail_credits == 0) or (pass_credits == 20 and defer_credits == 80 and fail_credits == 20)or(pass_credits == 20 and
                                        defer_credits == 60 and fail_credits == 40)or(pass_credits == 20 and defer_credits == 40 and fail_credits == 60)or(pass_credits == 0 and
                                        defer_credits == 120 and fail_credits == 0)or(pass_credits == 0 and defer_credits == 100 and fail_credits == 20)or(pass_credits == 0 and
                                        defer_credits == 80 and fail_credits == 40)or(pass_credits == 0 and defer_credits == 60 and fail_credits == 60):
                                        print("Do not progress - module retriever")
                                    elif (pass_credits == 40 and defer_credits == 0 and fail_credits == 80) or (pass_credits == 20 and
                                        defer_credits == 20 and fail_credits == 80)or(pass_credits == 20 and defer_credits == 0 and fail_credits == 100)or(pass_credits == 0 and
                                        defer_credits == 40 and fail_credits == 80)or(pass_credits == 0 and defer_credits == 20 and fail_credits == 100)or(pass_credits == 0 and
                                        defer_credits == 0 and fail_credits == 120):
                                        print("Exclude")
                                    else:
                                        print("Incorrect Values")
                                else:
                                    print("Total incorrect")
                            else:
                                print("Incorrect Values")
                        else:
                            print("out of range")
                    else:
                        print("Incorrect Values")
                else:
                    print("out of range")
            else:
               print("Incorrect Values")
        else:
           print("out of range")
    except ValueError:
        print("Integer required")

elif choosing_version.lower() == "staff":
    # Staff input for credits
    while True:
        try:
            pass_credits = int(input("\nEnter your total PASS credits: "))
            if pass_credits in range(0, 121):
                if pass_credits in valid_values:
                    defer_credits = int(input("Enter your total DEFER credits: "))
                    if defer_credits in range(0, 121):
                        if defer_credits in valid_values:
                            fail_credits = int(input("Enter your total FAIL credits: "))
                            if fail_credits in range(0,121):
                                if fail_credits in valid_values:
                                    if pass_credits + defer_credits + fail_credits == 120:
                                        if pass_credits == 120 and defer_credits == 0 and fail_credits == 0:
                                            print("Progress")
                                            progress_count += 1
                                            progression_data.append(("Progress", pass_credits, defer_credits, fail_credits))
                                        elif (pass_credits == 100 and defer_credits == 20 and fail_credits == 0)or(pass_credits == 100 and
                                            defer_credits == 0 and fail_credits == 20):
                                            print("Progress(module trailer)")
                                            trailer_count += 1
                                            progression_data.append(("Progress (module trailer)", pass_credits, defer_credits, fail_credits))
                                        elif (pass_credits == 80 and defer_credits == 40 and fail_credits == 0)or(pass_credits == 80 and
                                            defer_credits == 20 and fail_credits == 20)or(pass_credits == 80 and defer_credits == 0 and fail_credits == 40)or(pass_credits == 60 and
                                            defer_credits == 60 and fail_credits == 0)or(pass_credits == 60 and defer_credits == 40 and fail_credits == 20)or(pass_credits == 60 and
                                            defer_credits == 20 and fail_credits == 40)or(pass_credits == 60 and defer_credits == 0 and fail_credits == 60)or(pass_credits == 40 and
                                            defer_credits == 80 and fail_credits == 0)or(pass_credits == 40 and defer_credits == 60 and fail_credits == 20)or(pass_credits == 40 and
                                            defer_credits == 40 and fail_credits == 40)or(pass_credits == 40 and defer_credits == 20 and fail_credits == 60)or(pass_credits == 20 and
                                            defer_credits == 100 and fail_credits == 0) or (pass_credits == 20 and defer_credits == 80 and fail_credits == 20)or(pass_credits == 20 and
                                            defer_credits == 60 and fail_credits == 40)or(pass_credits == 20 and defer_credits == 40 and fail_credits == 60)or(pass_credits == 0 and
                                            defer_credits == 120 and fail_credits == 0)or(pass_credits == 0 and defer_credits == 100 and fail_credits == 20)or(pass_credits == 0 and
                                            defer_credits == 80 and fail_credits == 40)or(pass_credits == 0 and defer_credits == 60 and fail_credits == 60):
                                            print("Module retriever")
                                            retriver_count += 1
                                            progression_data.append(("Module retriever", pass_credits, defer_credits, fail_credits))
                                        elif (pass_credits == 40 and defer_credits == 0 and fail_credits == 80) or (pass_credits == 20 and
                                            defer_credits == 20 and fail_credits == 80)or(pass_credits == 20 and defer_credits == 0 and fail_credits == 100)or(pass_credits == 0 and
                                            defer_credits == 40 and fail_credits == 80)or(pass_credits == 0 and defer_credits == 20 and fail_credits == 100)or(pass_credits == 0 and
                                            defer_credits == 0 and fail_credits == 120):
                                            print("Exclude")
                                            exclude_count += 1
                                            progression_data.append(("Exclude", pass_credits, defer_credits, fail_credits))
                                        else:
                                            print("Incorrect Value")
                                    else:
                                        print("Total incorrect")
                                else:
                                    print("Incorrect Values")
                            else:
                                print("out of range")
                        else:
                            print("Incorrect Values")
                    else:
                        print("out of range")
                else:
                    print("Incorrect Values")
            else:
                print("out of range")
            print(" ")
            
            print("Would you like to enter another set of data?")

            continue_program = str(input("Enter 'y' for yes or 'q' to quit and view results: "))

            if continue_program.lower() != "y":
                print("\nPart 2:")

                categories = ["Progress", "Progress (module trailer)", "Module retriever", "Exclude"]

                for data in progression_data:
                    print(f"{data[0]} - {data[1]}, {data[2]}, {data[3]}")

                print("\nPart 3:")

                file_name = "progression_data.txt"
                write_progression_data(file_name, progression_data)
                read_progression_data(file_name)
                histogram(progress_count, trailer_count, retriver_count, exclude_count)
                break

        except ValueError:
            print("Integer required")
else:
    print("Invalid choice!")