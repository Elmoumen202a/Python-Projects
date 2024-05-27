def draw_unicorn():
    print("Welcome to the Draw Unicorn game!")
    print("Draw a unicorn using ASCII art.")
    print("When you're done, type 'END' on a new line to finish.")
    
    drawing = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        drawing.append(line)
    
    print("\nHere is your unicorn drawing:")
    for line in drawing:
        print(line)

if __name__ == "__main__":
    draw_unicorn()
