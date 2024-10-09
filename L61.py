#Authors are Aliza Litvak & Olivia Beck
import turtle
def turtle_move(color):
    riley = turtle.Turtle()
    for side in range(5):
        riley.color(color)
        riley.forward(100)
        riley.right(144)
    

def main():
    mood = input("How do you feel? \n")
    if mood == "angry":
        turtle_move ("red")
    if mood == "sad":
        turtle_move ("blue")
    if mood == "happy":
        turtle_move ("pink")
    if mood == "meh":
        turtle_move ("green")

main()

