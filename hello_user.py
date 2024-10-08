import tm1637
import time

tm = tm1637.TM1637(clk=21, dio=16)

clear = [0, 0, 0, 0] #Sets the default state of the display

tm.write(clear)
time.sleep(1)

name  = input("What is your name? ") #Gets user's name
name  = name.upper() #Capitalilzes the letters to make the message more readable

s = f"Hello {name}" #Creating the message

tm.scroll(s) #Print Message
time.sleep(2)
tm.write(clear)




