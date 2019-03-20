import sys
input_string = sys.argv[1]

sum=0
is_input_string_correct=True

for letter in input_string:
    if not letter.isdigit():
        is_input_string_correct=False
        break
    sum+=int(letter)

if is_input_string_correct:
    print(f"{sum}")
else:
    print("input string is not a number")

