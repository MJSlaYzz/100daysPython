# Day 27 #
# use Tkinter to create Graphical User Interface (GUI)

#import tkinter
# Or we can Wildcard tkinter: import it like <from tkinter import *> to denote import every single class.
from tkinter import *
def introduction_to_tkinter():
    # window = tkinter.Tk()
    window = Tk()
    window.title("My First GUI Program")
    # the window is going to scale to fit everything inside of it but we can set a minimum size to it by using .minsize()
    window.minsize(width= 500, height=300)

# Tkinter Widgets: Label, Button, Entry, Text Entry box, Spinbox, Scale(Slider), Checkbutton/Checkbox, Radiobutton, Listbox.
    #Lebel
    # my_label = tkinter.Label(text = "I Am A Label", font =("Arial",24, "italic")) # write a label (that is not enough to display it)
    my_label = Label(text = "I Am A Label", font =("Arial",24, "italic"))
    # my_label.pack() #display it on the screen and place it in the middle of the screen
    my_label.pack(side = "top") # can change the side of the text
    # my_label.pack(expand= True) # it's now trying to take the entire hight and width of the available screen size

    # update the my_label text:
    my_label["text"] = "New Text"
    # OR
    my_label.config(text = "Newer Text")

    # create a button

    # button = tkinter.BU
    def button_clicked():
        print("I got clicked")
        my_label.config(text = "Button Got Clicked!")

        new_text = input.get()
        if new_text.strip() != "":
            my_label.config(text = new_text.strip())
    
    button = Button(text = "Click Me", command = button_clicked)
    button.pack() # using pack() to show it in window.

    # create Entry

    input = Entry(width = 10)
    input.pack() # using pack() to show it in window.
    # get the input and print it in the terminal.
    # input.get() # to return the input as a string. needs to be written in the button click function.

    #rest of the of the widgets will be at tinker_widgets module.
    #-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

    # instead of using a while loop with a listing method inside we use the method .mainloop() from Tkinter
    window.mainloop() #this line of code should always be at the bottom of your program.
def tkinter_layout_managers():
    # window = tkinter.Tk()
    window = Tk()
    window.title("My First GUI Program")
    # add Padding around the entire window:
    window.config(padx = 100, pady = 200)
    # the window is going to scale to fit everything inside of it but we can set a minimum size to it by using .minsize()
    window.minsize(width= 500, height=300)

    def button_clicked():
        print("I got clicked")
        new_label.config(text = "Button Got Clicked!")
        new_text = new_input.get()
        if new_text.strip() != "":
            new_label.config(text = new_text.strip())

    new_label = Label(text = "I Am A New Label", font =("Arial",10, "italic"))
    new_button = Button(text = "Click Me", command = button_clicked)
    new_button2 = Button(text = "No, Click Me")
    new_input = Entry(width = 10)

    # Tkinter Layout Managers:
    # the most important 3 are : pack()    place()      grid()

    # pack() : packs the widgets next to each other in a vaguely logical format.
    # by default it will start from the top and pack each other widget below the previous one.
    # it's hard to specify a precise position using Pack()
    #new_label.pack()

    # place(): place is all about precise positioning.
    # place() is so specif and you have to always be careful when using coordinates.
    #new_label.place(x= 100, y= 100)

    #grid(): it treats your entire program as a grid and you can divide it into any number of columns | and rows __
    # the grid system is relative to the other components.
    # So event if we changed the first column to 5 and row to 5 it still won't change the layout because there's not widget in column 4, 3, 2 or 1.
    # so the best thing is to start with the widget we want on the top left first.
    # YOU CAN NOT MIX GRID AND PACK IN THE SAME PROGRAM!!!

    # add Padding around a specific widget: a good way to add space around your widgets
    new_label.config(padx= 50, pady=50)

    new_label.grid(column = 0, row = 0)
    new_button.grid(column = 1, row = 1) # using pack() to show it in window.
    new_button2.grid(column = 2, row = 0)
    new_input.grid(column = 3, row = 2) # using pack() to show it in window.

    
    # instead of using a while loop with a listing method inside we use the method .mainloop() from Tkinter
    window.mainloop() #this line of code should always be at the bottom of your program.

def mile_to_kilometers_converter():
    window = Tk()
    window.title("Mile to Km Converter")
    window.minsize(width=300, height=100)
    window.config(padx= 100,pady= 10)

    # Create a entry box
    user_input = Entry(width= 10)
    user_input.grid(column= 1, row= 0)

    label = Label(text = "Miles", font =("Arial",10, "italic"))
    label.grid(column= 2, row= 0)

    result_label = Label(text = "is equal to", font =("Arial",10, "italic"))
    result_label.grid(column= 0, row= 1)

    result_output = Label(text = "0", font =("Arial",10, "italic"))
    result_output.grid(column= 1, row= 1)

    km_text = Label(text = "Km", font =("Arial",10, "italic"))
    km_text.grid(column= 2, row= 1)

    def miles_to_kilometers():
        input_in_miles = user_input.get()
        result_output.config(text = round(int(input_in_miles) * 1.60934, 2))
    
    calculate_button = Button(text="Calculate", command= miles_to_kilometers)
    calculate_button.grid(column= 1, row= 2)








    window.mainloop()



def advanced_python_arguments():
    # Keyword Arguments (we took this before)
    def my_function(a, b, c):
        pass
    my_function(c = 3, a = 1, b = 2)

    # Advanced Python Arguments

    # Arguments with Default Values:
    def my_function1(a = 1, b = 2, c = 3):
        pass
    my_function1() # i can just call the function without passing any arguments to use the default values.
    my_function1(b = 4) # or i can change one of the default methods by just passing it's argument.

    # so if i hover over any of the methods in packs and find "=...." that means that this variable/argument has a default value.
    # those are called optional arguments, and unlike the required arguments then won't give an error if they weren't given a value when called.

    # Unlimited Arguments: a function that can take any amount of arguments.
    # normal function:
    def add1(n1, n2):
        return n1 + n2
    add1( n1 = 5, n2 = 3)

    # function with unlimited arguments:
    def add(*args): # by typing one asterisk(*) and assign it a name (args is the default name)
        sum = 0
        for n in args: # loop through all of the arguments which will be in form of a tuple.
            # print(n)
            sum += n
        return sum
    add(3, 4, 5, 6)

    def multiplication(*numbers):
        print(numbers[0])
        multiplication = 1
        for n in numbers: # loop through all of the arguments which will be in form of a tuple.
            # print(n)
            multiplication *= n
        return multiplication
    print(multiplication(3, 4, 5, 6))

    # define arguments by name not by position:
    def calculate(n, **kwargs): # by adding two asterisks(**) and assign it a name (kwargs <stands for key word arguments> is the default name) to create a keyword argument.
        # unlike single asterisk arguments, this one will be in form of a dictionary.
        # for key, value in kwargs.items():
        #     print(key)
        #     print(value)

        # now we added another argument which is n
        n += kwargs["add"]
        n *= kwargs["multiply"]
        print(n)

    # calculate(add =3, multiply = 5)
    calculate(2, add =3, multiply = 5)

def optional_keyword_arguments():
    # Create a class with lots of optional keyword arguments.
    class Car:
        def __init__(self, **kw):
            # when calling the class if the user didn't pass one of the arguments the program will crash.
            # self.make = kw["make"]
            # self.model = kw["model"]
            # we avoid the crash problem when using the keyword .get()
            self.make = kw.get("make")
            self.model = kw.get("model")

    #my_car = Car() # now when i hover over the Car() call i'll only see **kw in the description
    my_car = Car(make= "Nissan", model = "GT-R")
    print(my_car.model) # output: GT-R
    my_car2 = Car(make= "BMW")
    print(my_car2.model) # output: None (instead of getting an error)

mile_to_kilometers_converter()