# Reference for Copilot:
# - swap: a, b -> b, a
# - rot: a, b, c -> c, a, b
# - pop: a, b -> a
# - add: a, b -> a + b
# - sub: a, b -> a - b
# - mul: a, b -> a * b
# - div: a, b -> a / b
# - mod: a, b -> a % b
# - dup: a -> a, a
# - var: save a in a variable
# - varget: get the value of a variable
# - vardel: delete a variable
# - over: a, b -> a, b, a
# - ln: a -> len(a)
# - str: a -> str(a)
# - int: a -> int(a)
# - float: a -> float(a)
# - print: a -> print(a, end='')
# - println: a -> print(a)
# - eq: a, b -> a == b
# - neq: a, b -> a != b
# - lt: a, b -> a < b
# - gt: a, b -> a > b
# - gte: a, b -> a >= b
# - lte: a, b -> a <= b
# - and: a, b -> a and b
# - or: a, b -> a or b
# - not: a -> not a
# - if: a -> if a:
# - endif: end if statement
# - else: else:
# - while: while a:
# - do: do:
# - proc: def a():
# - call: a()
# - exit: exit()
# - stack: a, b, c -> a, b, c, [a, b, c]
# - stackp: stack print
# - end: end while, proc
# - include: include a file

# Make a version variable that holds the current version of the language
1.0 "version" var

# Input: (float) version to exit
# Description: Exits the program if the version number is heigher or equal to the input
# Examples:
# - '2.0 outdate' (with version number 1.0) does nothing.
# - '1.5 outdate' (with version number 2.2) exits the program
# Output: (None)
proc outdate do
    version swap gte if
        "This program is outdated!" println
        exit
    endif
end

# Input: (none)
# Description: Removes all values in the stack
# Examples:
# - [1, 2, 3, 4, "test"] -> []
#                       clear
# Output: (None)
proc clear do
    while stack ln 0 gt do
        pop
    end
end