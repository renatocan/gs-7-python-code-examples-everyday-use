import random
import string
import argparse

parser = argparse.ArgumentParser(description="Password generator")

parser.add_argument(
    "--no-digits",
    help="generate password without digits",
    action="store_true"
)

parser.add_argument(
    "--no-special-chars",
    help="generate password without special characters",
    action="store_true",
)

parser.add_argument(
    "length", nargs="?", type=int, help="length of the password", default=None
)

arguments = parser.parse_args()

use_arguments = True if (arguments.length or
                         arguments.no_digits or
                         arguments.no_special_chars) else False
use_arguments_length = True if arguments.length else False

if use_arguments:
    use_digits = not arguments.no_digits
else:
    while True:
        use_digits_answer = input("Use digits [y]/n: ")
        if use_digits_answer.lower() not in ["", "y", "n"]:
            print("Invalid answer")
            continue
        break

    if use_digits_answer.lower() == "n":
        use_digits = False
    else:
        use_digits = True

if use_arguments:
    use_punctuation = not arguments.no_special_chars
else:
    while True:
        use_punctuation_answer = input("Use special characters [y]/n: ")
        if use_punctuation_answer.lower() not in ["", "y", "n"]:
            print("Invalid answer")
            continue
        break

    if use_punctuation_answer.lower() == "n":
        use_punctuation = False
    else:
        use_punctuation = True

if use_arguments_length:
    password_length = arguments.length
else:
    while True:
        password_length_answer = input("Length of the password [10]: ")
        if password_length_answer == "":
            password_length = 10            
            break
        else:
            try:
                password_length = int(password_length_answer)
            except:
                print("Invalid value")
                continue
            break

letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation

symbols = letters
if use_digits:
    symbols += digits
if use_punctuation:
    symbols += punctuation

password = "".join(random.choice(symbols) for i in range(password_length))
print(password)
