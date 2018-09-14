# DO NOT TRY THIS AT HOME
import sys

password = input("Enter your password:  ")
attempt_count = 1
while password != 'password':
    if attempt_count > 3:
        sys.exit("Unlucky")
    password = input("Incorrect, retry:  ")
    attempt_count += 1
print("Welcome, would you like to play a game?")