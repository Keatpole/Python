# If i divisible from 3 without remainder: Fizz
# If i disvisble from 5 without remainder: Buzz
# If both: Fizzbuzz
# If none: i

for i in range(1, 100):
    a = (i % 3 == 0)
    b = (i % 5 == 0)

    if a and b:
        print("FizzBuzz")
    elif a:
        print("Fizz")
    elif b:
        print("Buzz")
    else:
        print(i)