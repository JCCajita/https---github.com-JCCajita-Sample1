show_instructions = "hi"

while show_instructions == "hi":
    show_instructions = input("have you played this game before? ").lower()

    if show_instructions == "yes" or show_instructions == "y":
        print("program continues")
    elif show_instructions == "no" or show_instructions == "n":
        print("display instructions")
    else:
        print("yes or no")

print("hi")
print("hello")
print("hello and hi")