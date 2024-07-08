import sys

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!", file=sys.stderr)

    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

    with open(filename) as file:
        file_contents = file.read()

    error = False
    length = len(file_contents)
    skip_next = False

    for i in range(length):
        if skip_next:
            skip_next = False
            continue

        c = file_contents[i]
        next_c = file_contents[i + 1] if i + 1 < length else None  # Peek at the next character

        if c == "(":
            print("LEFT_PAREN ( null")
        elif c == ")":
            print("RIGHT_PAREN ) null")
        elif c == "{":
            print("LEFT_BRACE { null")
        elif c == "}":
            print("RIGHT_BRACE } null")
        elif c == "*":
            print("STAR * null")
        elif c == ".":
            print("DOT . null")
        elif c == ",":
            print("COMMA , null")
        elif c == "+":
            print("PLUS + null")
        elif c == "-":
            print("MINUS - null")
        elif c == ";":
            print("SEMICOLON ; null")
        elif c == "=":
            if next_c == "=":
                print("EQUAL_EQUAL == null")
                skip_next = True
            else:
                print("EQUAL = null")
        elif c == "!":
            if next_c == "=":
                print("BANG_EQUAL != null")
                skip_next = True
            else:
                print("BANG ! null")
        elif c == "<":
            if next_c == "=":
                print("LESS_EQUAL <= null")
                skip_next = True
            else:
                print("LESS < null")
        elif c == ">":
            if next_c == "=":
                print("GREATER_EQUAL >= null")
                skip_next = True
            else:
                print("GREATER > null")
        elif c == "/":
            if next_c == "/":
                break  # Ignore the rest of the line for a comment
            else:
                print("SLASH / null")
        elif c == " " or c == "\t" or c == "\n":
            pass  # Ignore whitespace characters
        else:
            error = True
            line_number = file_contents.count("\n", 0, file_contents.find(c)) + 1
            print(
                "[line %s] Error: Unexpected character: %s" % (line_number, c),
                file=sys.stderr,
            )

    print("EOF  null")
    if error:
        exit(65)
    else:
        exit(0)

if __name__ == "__main__":
    main()
