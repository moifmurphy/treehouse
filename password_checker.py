# DO NOT TRY THIS AT HOME
import sys

MASTER_PASSWORD = 'password'
password = input("Enter your password:  ")
attempt_count = 1
while password != MASTER_PASSWORD:
    if attempt_count > 3:
        sys.exit("Game over, insert coin to continue")
    password = input("Incorrect, retry:  ")
    attempt_count += 1
print("Welcome, would you like to play a game?")