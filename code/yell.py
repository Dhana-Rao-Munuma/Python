def main():
    yell("This"," is"," testing00")

def yell(*phrase):
    print(*[word.upper() for word in phrase])

if __name__ == "__main__":
    main()