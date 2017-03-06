#Title "Fraction Tutor"
"""
Design Prolog 

Author:Karthik Nayak

Date: 17th Sept 2015

Purpose: to present random fraction problems for a student to answer,
and to give feedback on the student's answer

Pre conditions:
   user gives name and difficulty level, user gives answer to presented problem

Post conditions;
   program prompts for input, then presents problem for user, gives feedback
   to user on correctness of answer 

"""

from graphics import *
from random import *

def main():

#Creating the main window 
    win = GraphWin("Entry", 500, 600)

#Displaying text and entry box to get name and dificulty from use
    msg = Text(Point(250, 50), "Fraction Tutor")

    msg.setSize(25)

    msg.setFill('green')

    msg.draw(win)    



    txt = Text(Point(250, 100), "What's is your name?")

    txt.setSize(20)

    txt.draw(win)

    

    entry = Entry(Point(250, 135), 20)  

    entry.setFill("white") 

    entry.draw(win)    

    

    txt2 = Text(Point(250, 250), "What difficulty do you want?(1-3)")

    txt2.setSize(20)

    txt2.draw(win)       

    

    entry2 = Entry(Point(250, 285), 20)

    entry2.setText("1")  

    entry2.setFill("white") 

    entry2.draw(win)         

       

#Storing the inputs in variables 
    win.getMouse()

    name = entry.getText() 

    difficulty = entry2.getText()

    
    txt.undraw()

    txt2.undraw()

    entry.undraw()

    entry2.undraw()

    

#Displaying name and selected difficulty 
    msg = "Student: " + name

    msg1 = Text(Point(100, 100), msg)

    msg1.setSize(15)

    msg1.draw(win)  

    

    msg = "Difficulty: " + difficulty

    msg2= Text(Point(400, 100), msg)

    msg2.setSize(15)

    msg2.draw(win)   

    

# Getting four random numbers for the two fractions for the problem
    if difficulty == '3':

        num1 = randrange(11,26)

        den1 = randrange(11,26)

        num2 = randrange(11,26)

        den2 = randrange(11,26)                 

    

    elif difficulty == '2':

        num1 = randrange(6,16)

        den1 = randrange(6,16)

        num2 = randrange(6,16)

        den2 = randrange(6,16)      

    

    else:

        num1 = randrange(1,11)

        den1 = randrange(1,11)

        num2 = randrange(1,11)

        den2 = randrange(1,11)

        

# Select a random operator to use for the problem.
    operator = choice("+-*/")

    if operator == '+':

        ans_numerator = num1*den2 + den1*num2

        ans_denominator = den1*den2

        

    elif operator == '-':

        ans_numerator = num1*den2 - den1*num2

        ans_denominator = den1*den2        

    

    elif operator == '*':

        ans_numerator = num1*num2

        ans_denominator = den1*den2        

    
    else:

        ans_numerator = num1*den2

        ans_denominator = den1*num1       

    

#Displaying the faction 
    numerator1 = Text(Point(100, 180), num1)

    numerator1.setSize(15)

    numerator1.draw(win)     

    

    dash1 = Text(Point(100, 185), "____")

    dash1.setSize(15)

    dash1.draw(win)     

    

    denominator1 = Text(Point(100, 210), den1)

    denominator1.setSize(15)

    denominator1.draw(win)  

 

    numerator2 = Text(Point(200, 180), num2)

    numerator2.setSize(15)

    numerator2.draw(win)     

    

    dash2 = Text(Point(200, 185), "____")

    dash2.setSize(15)

    dash2.draw(win)     

    

    denominator2 = Text(Point(200, 210), den2)

    denominator2.setSize(15)

    denominator2.draw(win)   

    

    symbol = Text(Point(150, 195), operator)

    symbol.setSize(25)

    symbol.draw(win)     



    equals = Text(Point(250, 195), "=")

    equals.setSize(25)

    equals.draw(win)  



    entry_ans1 = Entry(Point(300, 180), 5)  

    entry_ans1.setFill("white") 

    entry_ans1.draw(win)    

    

    entry_ans2 = Entry(Point(300, 210), 5)  

    entry_ans2.setFill("white") 

    entry_ans2.draw(win)

    

    dash3 = Text(Point(300, 185), "____")

    dash3.setSize(15)

    dash3.draw(win)

    

# getting answers for numerator and denominator from user and, storing them into variables
    win.getMouse()

    ans1 = entry_ans1.getText() 

    ans2 = entry_ans2.getText()    

    

# Checking users answers and giving feedback 
    if (int(ans1) == ans_numerator) and (int(ans2) == ans_denominator):

        happy = Image(Point(250,350),"happy.gif")

        happy.draw(win)        

        display = "You are right!! " + name

        msg3= Text(Point(250, 420), display)

        msg3.setSize(20)

        msg3.draw(win)      

    

    if int(ans1) != ans_numerator:

        sad = Image(Point(250,350),"sad.gif")

        sad.draw(win)        

        display = name + ", your numerator should be " + str(ans_numerator)

        msg3= Text(Point(250, 500), display)

        msg3.setSize(20)

        msg3.draw(win)

    

    if int(ans2) != ans_denominator:

        sad = Image(Point(250,350),"sad.gif")

        sad.draw(win)        

        display = name + ", your denominator should be " + str(ans_denominator)

        msg3= Text(Point(250, 530), display)

        msg3.setSize(20)

        msg3.draw(win)    
            

    win.getMouse()

    win.close()
main()    
