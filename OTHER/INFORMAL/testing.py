class WInput:
    '''
    I h8 pylint
    '''

    def __init__(self, i):
        self.i = input(i)
    def __enter__(self):
        return self.i
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


with WInput("Enter your name: ") as name:
    print(f"Hello, {name}!")
    