while True:
    import os,sys;s=input();b="";os.system("cls"if sys.platform=="win32"else"clear");print(s)
    for r in s.split("."):b+=chr(int(r.split("/")[0])-int(r.split("/")[1]))
    print(f"\n{b}\n")
