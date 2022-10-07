import sys

stack = []
if_result = []
while_loops = []
procs = {}
temp_vars = {}
perm_vars = {}
in_proc = None
if_skip = False
fn_skip = False
is_in_string = False
conId = 0

string = ""
code = []

FILE_EXT = ".ml"

def builtins(word, index):
    """
    Built-in functions

    :param str word: The word to check
    """

    global in_proc, code, if_skip, fn_skip, if_result

    if word != "" and word[0] != '"':
        word = word.lower()

    # T_SWAP
    if word == "swap":
        a, b = stack.pop(), stack.pop()
        stack.append(a)
        stack.append(b)

    # T_ROT
    elif word == "rot":
        a, b, c = stack.pop(), stack.pop(), stack.pop()
        stack.append(a)
        stack.append(c)
        stack.append(b)

    # T_POP
    elif word == "pop":
        stack.pop()
    
    # T_ADD
    elif word == "add":
        b, a = stack.pop(), stack.pop()
        stack.append(a + b)

    # T_SUB
    elif word == "sub":
        b, a = stack.pop(), stack.pop()
        stack.append(a - b)

    # T_MUL
    elif word == "mul":
        b, a = stack.pop(), stack.pop()
        stack.append(a * b)

    # T_DIV
    elif word == "div":
        b, a = stack.pop(), stack.pop()
        stack.append(a / b)

    # T_MOD
    elif word == "mod":
        b, a = stack.pop(), stack.pop()
        stack.append(a % b)

    # T_DUP
    elif word == "dup":
        a = stack.pop()
        stack.append(a)
        stack.append(a)

    # T_VAR
    elif word == "var":
        name = stack.pop()
        perm_vars[name] = stack.pop()

    # T_VARGET
    elif word == "varget":
        name = stack.pop()

        if name in perm_vars.keys():
            stack.append(perm_vars[name])
        else:
            stack.append(0)

    # T_VARDEL
    elif word == "vardel":
        name = stack.pop()

        if name in perm_vars.keys():
            del perm_vars[name]
        else:
            stack.append(0)

    # T_OVER
    elif word == "over":
        a, b = stack.pop(), stack.pop()
        stack.append(b)
        stack.append(a)
        stack.append(b)

    # T_LEN
    elif word == "ln":
        a = stack.pop()
        stack.append(len(a))

    # T_STR
    elif word == "str":
        stack.append(str(stack.pop()))

    # T_INT
    elif word == "int":
        stack.append(int(stack.pop()))

    # T_FLOAT
    elif word == "float":
        stack.append(float(stack.pop()))

    # T_PRINT
    elif word == "print":
        to_print = stack.pop()

        if type(to_print) == str:
            print(to_print.replace("\\n", "\n").replace("\\t", "\t").replace("\e", ""), end="")
        else:
            print(to_print)

    # T_PRINTLN
    elif word == "println":
        to_print = stack.pop()

        if type(to_print) == str:
            print(to_print.replace("\\n", "\n").replace("\\t", "\t").replace("\e", ""))
        else:
            print(to_print)

    # T_EQ
    elif word == "eq":
        a, b = stack.pop(), stack.pop()
        stack.append(int(a == b))

    # T_NEQ
    elif word == "neq":
        a, b = stack.pop(), stack.pop()
        stack.append(int(a != b))

    # T_GT
    elif word == "gt":
        a, b = stack.pop(), stack.pop()
        stack.append(int(b > a))

    # T_LT
    elif word == "lt":
        a, b = stack.pop(), stack.pop()
        stack.append(int(b < a))

    # T_GTE
    elif word == "gte":
        a, b = stack.pop(), stack.pop()
        stack.append(int(b >= a))

    # T_LTE
    elif word == "lte":
        a, b = stack.pop(), stack.pop()
        stack.append(int(b <= a))

    # T_AND
    elif word == "and":
        a, b = stack.pop(), stack.pop()
        stack.append(int(a and b))

    # T_OR
    elif word == "or":
        a, b = stack.pop(), stack.pop()
        stack.append(int(a or b))

    # T_NOT
    elif word == "not":
        a = stack.pop()
        stack.append(int(not a))

    # T_IF
    elif word == "if":
        if_skip = not stack.pop()
        if_result.append({})
        if_result[-1][index] = int(not if_skip)

    # T_ENDIF
    elif word == "endif":
        if_skip = False

        if if_result:
            if_result.pop()

    # T_ELSE
    elif word == "else":
        res = if_result[-1].popitem()
        if_result[-1][res[0]] = res[1]

        if_skip = bool(res[1])

    elif word == "finally":
        key = None

        for i in if_result[-1].keys():
            key = i
            break

        if key is None: return

        if if_result[-1][key]: if_skip = False

    # T_WHILE
    elif word == "while":
        c = []

        cod = code.copy()

        while True:
            word = cod.pop(index + 1)

            if word == "do":
                break
            c.append(word)
        
        c2 = []

        cod2 = code.copy()

        while True:
            word = cod2.pop(index + len(c) + 2)

            if word == "end":
                break

            c2.append(word)
        
        while_loops.append(c2)
        procs[f"while_loop_{len(while_loops)}"] = {"code": c2, "return": 0}
        __code = code.copy()
        _code = f"proc while_loop_{len(while_loops)} do {' '.join(c)} if {' '.join(c2)} finally endif endif while_loop_{len(while_loops)} endif end".split(" ")
        code = f"{' '.join(_code)} while_loop_{len(while_loops)} {' '.join(code[index + len(c) + len(c2) + 2:])}".split(" ")

        print(" ".join(__code),"\n\n"," ".join(_code),"\n\n"," ".join(code))

        # proc while_loop_1 do index 100 lt if index 1 add "index" var index 3 mod 0 eq "fizz" var index 5 mod 0 eq "buzz" var fizz buzz and if "FizzBuzz" println else fizz if "Fizz" println else buzz if "Buzz" println else index print endif end

        #print(_code)

        add_thread(_code)

        code = f"\"while_loop_{len(while_loops)}\" call {' '.join(__code[index + len(c) + len(c2) + 3:])}".split(" ")

        #print(code)

        add_thread(code)

        del procs[f"while_loop_{len(while_loops)}"]
        while_loops.pop()


    # T_PROC
    elif word == "proc":
        c = []

        cod = code.copy()
        name = cod.pop(index + 1)

        while True:
            word = cod.pop(index + 2)
            #print(word)

            c.append(word)
            if word == "end":
                break
        
        procs[name] = {"code": c, "return": 0}
        code.append("end")

        fn_skip = True

    # T_CALL
    elif word == "call":
        proc = stack.pop()

        if proc in procs:
            in_proc = proc

            code = procs[proc]["code"] + code[index + 1:]
            add_thread(code)

    # T_GET
    elif word == "get":
        names = []

        while True:
            w = code.pop(1)
            if w == "do":
                break
            names.append(w)

        removed = []

        for name in names:
            to_remove = stack.pop(0)

            temp_vars[name] = to_remove
            removed.append(to_remove)

        for r in removed:
            stack.append(r)

    # T_SET
    elif word == "set":
        names = []

        while True:
            w = code.pop(1)
            if w == "do":
                break
            names.append(w)

        for name in names:
            temp_vars[name] = stack.pop(0)

    # T_EXIT
    elif word == "exit":
        exit()

    # T_STACK
    elif word == "stack":
        stack.append(stack)

    # T_STACKP
    elif word == "stackp":
        print(stack)

    # T_END
    elif word == "end":
        if in_proc != "":
            in_proc = ""

        temp_vars.clear()
        fn_skip = False
        
    # T_RETURN
    elif word == "return":
        r = stack.pop()
        p = stack.pop()

        procs[p] = {"code": procs[p]["code"], "return": r}

    # T_INCLUDE
    elif word == "include":
        filename = stack.pop()

        c = []

        with open(filename + FILE_EXT, "r") as f:
            c = remove_comments(f.read()).replace("\n", " ").split(" ") + " ".join(code).replace(f"\"{filename}\" include", "").split(" ")

        _code = code.copy()
        code = c + _code

        add_thread(c)

    else:
        return -1

def run(c, id, debug=1):
    """
    Runs the code

    :param c: The code to run
    """

    global is_in_string, string, in_proc, fn_skip, code

    if debug:
        print("\n--- DEBUG ---")
        print("CID:", c, id)

    for i,word in enumerate(c):
        if debug:
            print(f"\n--- {word} ---")

            print("PROCS:", procs)

            print("SKIP_BOOLS (fn, if, res):", fn_skip, if_skip, if_result)

            print("EXIT_BOOL:", str(conId != id), conId, id)
            print("STACK:", stack)

            print("--- END ---")
        if conId != id:
            return

        if word == "":
            continue

        cont = if_skip or fn_skip

        if if_skip and word in ["endif", "else", "finally"]:
            builtins(word, i)
        if fn_skip and word in ["end"]:
            fn_skip = False
            builtins(word, i)

        if if_skip and word == "if":
            try:
                stack.append(code[i - 1])
                if_result[i] = 1
            except Exception:
                pass

        if cont:
            continue

        if is_in_string:
            string += word + " "
            if word[-1] == '"':
                is_in_string = False
                stack.append(string[1:-2])
            continue
        
        if word[0] == '"':
            if word[-1] != '"':
                is_in_string = True

                string = ""
                string += word + " "
            else:
                stack.append(word[1:-1])
                
            continue

        if len(word) < 1:
            continue

        if word.replace("-", "").isdigit():
            stack.append(int(word))
        elif word.replace(".", "").replace("-", "").isdigit():
            stack.append(float(word))

        if builtins(word, i) == -1:
            if word.replace("@", "") in procs and code[i - 1] != "proc":
                if word[0] == "@":
                    stack.append(procs[word[1:]]["return"])
                else:
                    in_proc = word

                    code = procs[word]["code"] + code[i + 1:]

                    add_thread(code)
            if word in temp_vars:
                stack.append(temp_vars[word])
            if word in perm_vars:
                stack.append(perm_vars[word])

def add_thread(code):
    """
    Starts a new thread to run code on
    
    :param code: The code to run
    """
    global conId

    conId += 1
    run(code, conId)

def remove_comments(co):
    """
    Removes comments from code

    :param co: The code to remove comments from
    """

    _code = []

    for c in co.split("\n"):
        if c.startswith(("#", "//")):
            continue
        elif c.find("//") != -1:
            _code.append(c[:c.find("//")])
        elif c.find("#") != -1:
            _code.append(c[:c.find("#")])
        else:
            _code.append(c)

    #print(_code)

    return " ".join(_code)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            code = remove_comments(f.read()).replace("\n", " ").strip().split(' ')

            run(code, conId)
    else:
        while True:
            code = remove_comments(input(">> ")).strip().split(" ")

            run(code, conId)

            temp_vars.clear()

            for k, v in procs.items():
                if k.startswith("while_loop_"):
                    del procs[k]
