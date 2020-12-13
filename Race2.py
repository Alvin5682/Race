import turtle 
import random
import time
screen=turtle.getscreen()
def choosecolor():
    red=random.random()
    green=random.random()
    blue=random.random()
    return red,green,blue
def Race(number):
    players=["a","b","c","d","e","f","g","h","i","k","j","u","o","p","s","l","x","z","v","m"]
    end=1
    for i in range(0,number):
        players[i]=turtle.Turtle()
        players[i].shape("turtle")
        players[i].color(choosecolor())
        players[i].speed(7)
        players[i].penup()
        players[i].goto(500,300-70*i)
        players[i].pendown()
        players[i].circle(30)
        players[i].penup()
        players[i].goto(-500,330-70*i)
        players[i].pendown()
    while(True):
            for g in range(0,number):
                if end<0:
                    break
                else:
                    player_dice=random.randint(1,6)
                    players[g].fd(player_dice*20)
                    time.sleep(0.5)
                    if players[g].pos()>=(500,330-70*i):
                        print("Player ",g+1," wins")
                        end=end-100
                        break
    screen.exitonclick()
Race(5)