# Made for a Specific event , Gi3 integration Day
from turtle import Turtle, Screen, getscreen, width
import turtle
import random
from alphabet import alphabet
from turtle import *

ymken = turtle.Turtle()
ymken.hideturtle()
ymken.speed(0)
window = turtle.Screen()
window.bgcolor("#000000")
ymken.pensize(2)


def displayMessage(message, fontSize, color, x, y):
  ymken.color(color)
  message = message.upper()

  for character in message:
    if character in alphabet:
      letter = alphabet[character]
      ymken.penup()
      for dot in letter:
        ymken.goto(x + dot[0] * fontSize, y + dot[1] * fontSize)
        ymken.pendown()

      x += fontSize
    if character == " ":
      x += fontSize
    x += characterSpacing


# Main Program
fontSize = 25
fontsi = 20
characterSpacing = 5
fontColor = "#00ace6"
screen = getscreen()

screen.delay(20)
message = "HALLO CHILDREN XD"
displayMessage(message, fontSize, fontColor, -250, 20)
screen = getscreen()
screen.clear()
window.bgcolor("#000000")
screen.delay(20)

message = "CHIILDREEEEENNN "
displayMessage(message, fontSize, fontColor, -350, -60)
screen = getscreen()
screen.clear()
window.bgcolor("#000000")
screen.delay(20)

message = "CHIIIIILDREEEEEEN "
displayMessage(message, fontSize, fontColor, -350, -60)
screen = getscreen()
screen.clear()
window.bgcolor("#000000")
screen.delay(20)

message = "AND WELCOME TO THIS MEDIOCRE EVENT"
displayMessage(message, fontSize, fontColor, -500, 10)
screen = getscreen()
screen.clear()
window.bgcolor("#000000")
screen.delay(20)

message = "HOPE YOU ARE DOING GOOD "
displayMessage(message, fontSize, fontColor, -250, -60)
screen = getscreen()
screen.clear()
window.bgcolor("#000000")
screen.delay(20)


message = "AND BTW I WAS JOKING ABOUT CHILDREN STUFF"
displayMessage(message, fontsi, fontColor, -680, -60)
screen = getscreen()
screen.clear()
window.bgcolor("#000000")
screen.delay(30)

message = "HMMMMM NAAAAH I WAS NOT"
displayMessage(message, fontSize, fontColor, -350, -60)
screen = getscreen()
screen.clear()
window.bgcolor("#000000")
screen.delay(30)

message = "LETS ROCK IT ANYWAY"
displayMessage(message, fontSize, fontColor, -250, 10)

input("Made By Oussama Samoudi")