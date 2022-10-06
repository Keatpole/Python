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
# - print: a -> print(a)
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

# Example:

proc add2check do
    "result" var
    "n2" var
    "n1" var
    "res" var

    n1 str print
    "\e + \e" print
    n2 str print
    res str print
    result str println
end

proc add2 do
    "result" var
    "n2" var
    "n1" var

    n1 n2 add result eq if
        "\e == \e" n1 n2 result add2check
    else
        "\e != \e" n1 n2 result add2check
    endif
end

# Test add2
5 9 14 add2 # 5 + 9 == 14: True
5 9 15 add2 # 5 + 9 == 15: False