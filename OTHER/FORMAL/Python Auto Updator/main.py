import runner

if not runner.run("http://localhost/test/code.py"):
    print("Oops!")