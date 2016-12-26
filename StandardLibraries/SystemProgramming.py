# -*-coding:Latin-1 -*

import sys, os, signal, argparse

import math

print(sys.stdin) #standard input

print(sys.stdout) #standard output

print(sys.stderr) #standard Error

print(sys.stdout.write("Test\n"))

file = open('output.txt', 'w')
sys.stdout = file
print("Somethings ...")
sys.stdout = sys.__stdout__

print(os.getcwd())


##############################################
########### HOW CALL FUNCTION WITH SIGNAL ####
def close_program(signal, frame):
    """function called when is time to close the program"""
    print("Its time to Close !")
    sys.exit(0)

signal.signal(signal.SIGINT, close_program)

print("Infinite loop")
#while True:
#    continue
#################################################

if len(sys.argv) < 2:
    print("Specify an action in parameters")
    sys.exit(1)

action = sys.argv[1]

if action == "start":
    print("You Start the operation")
elif action == "stop":
    print("You Stop the operation")
elif action == "restart":
    print("You Restart the operation")
elif action == "status":
    print("The State of operation")
else:
    print("I don't know this action !")


parser = argparse.ArgumentParser()
parser.add_argument("x", type=int, help="the number to be squared")
parser.add_argument("-v", "--verbose", action="store_true", help="increase the verbosity")
args = parser.parse_args()
x = args.x
square_of = x ** 2
if args.verbose:
    print("Pow({0}, 2) = {1}".format(x, square_of))
else:
    print(square_of)

terminal = os.system("ls -a")

print(terminal)