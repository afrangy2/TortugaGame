# raj game 1.0 


import turtle 
from time import sleep
import random 


def newline():
  print(" ")

print("Welcome to the game. You will be faced with a series of choices to make. Do not fuck up or la tortuga will die");
newline();
sleep(3);

tortuga = turtle.Turtle();

tortuga.shape("turtle");
tortuga.fd(1);

print("this is raj. He's a friendly tortuga. ");
newline();
sleep(3);




def rajColorPick():
    while True:
        rajColor = str(input("What color would you like raj to be?"))
        if rajColor in ["purple", "pink", "red", "blue", "green"]:
            tortuga.color(rajColor)
            return
        print("Invalid color selection. Try again")


rajColorPick();


sleep(3);
newline();
print("Ok. nice. now he has a color! So what do you want to do with this lil guy?");
sleep(3);
newline();
print("Raj can move around, he can dance, he can do all sorts of stuff. Now unfortunately you don't get too many options here ok? I will be doing most of the moving around so.. yeah.");
newline();
sleep(3);

print("so.. let's say that if your little tortuga was to hit that circle over there, he'd die.");
dCircle = turtle.Turtle();
dCircle.penup();
dCircle.shape("circle");
dCircle.fd(50);
dCircle.right(90);
dCircle.fd(50);

newline();
print("We wouldn't want little rajito to die now would we?");
newline();
sleep(3);
print("no. that would be bad!!!! so you have to make a choice. for every choice you make, raj will move left or right. The circle will also move randomly every time you move. If you touch the circle, you die. Good luck.")
newline();
sleep(3);

def rajMoveChoice(direction, amount): 
  



