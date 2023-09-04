def decorators(func):
    def wrapping(x):
        print("Before:")
        func(x)
        print("After:")
    return wrapping

@decorators
def functi(name):
    print(f"Hey Buddy {name}")


functi("Dhana")