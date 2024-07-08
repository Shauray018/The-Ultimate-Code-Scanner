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
    tokens = []
    error_messages = []
    line = 1

    for i in range(length):
        if skip_next:
            skip_next = False
            continue

        c = file_contents[i]
        next_c = file_contents[i + 1] if i + 1 < length else None  # Peek at the next character

        if c == "(":
            tokens.append("LEFT_PAREN ( null")
        elif c == ")":
            tokens.append("RIGHT_PAREN ) null")
        elif c == "{":
            tokens.append("LEFT_BRACE { null")
        elif c == "}":
            tokens.append("RIGHT_BRACE } null")
        elif c == "*":
            tokens.append("STAR * null")
        elif c == ".":
            tokens.append("DOT . null")
        elif c == ",":
            tokens.append("COMMA , null")
        elif c == "+":
            tokens.append("PLUS + null")
        elif c == "-":
            tokens.append("MINUS - null")
        elif c == ";":
            tokens.append("SEMICOLON ; null")
        elif c == "=":
            if next_c == "=":
                tokens.append("EQUAL_EQUAL == null")
                skip_next = True
            else:
                tokens.append("EQUAL = null")
        elif c == "!":
            if next_c == "=":
                tokens.append("BANG_EQUAL != null")
                skip_next = True
            else:
                tokens.append("BANG ! null")
        elif c == "<":
            if next_c == "=":
                tokens.append("LESS_EQUAL <= null")
                skip_next = True
            else:
                tokens.append("LESS < null")
        elif c == ">":
            if next_c == "=":
                tokens.append("GREATER_EQUAL >= null")
                skip_next = True
            else:
                tokens.append("GREATER > null")
        elif c == "/":
            if next_c == "/":
                break  # Ignore the rest of the line for a comment
            else:
                tokens.append("SLASH / null")
        elif c == " " or c == "\t" or c == "\n":
            pass  # Ignore whitespace characters
        else:
            error = True
            line_number = file_contents.count("\n", 0, file_contents.find(c)) + 1
            error_messages.append("[line %s] Error: Unexpected character: %s" % (line_number, c))

    tokens.append("EOF null")

    for error_message in error_messages:
        print(error_message, file=sys.stderr)
    for token in tokens:
        print(token)

    if error:
        exit(65)
    else:
        exit(0)

if __name__ == "__main__":
    main()
