while True: 
    import random,os,sys;i=input();b="";os.system("cls"if sys.platform=="win32"else"clear");print(i)
    for c in i:d=random.randint(1,9);b+=f"{ord(c)+d}/{d}."
    print(f"\n{b[:-1]}\n")