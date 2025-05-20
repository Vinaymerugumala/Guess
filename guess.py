# cook your dish here
secret = "Vinay"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

while secret != guess and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter your guess: ")
        if secret == guess:
            print(" you Won")
        else:
            print("another guess")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Unsuccessful Guess — You lost")
else:
    print("Successful Guess!")
