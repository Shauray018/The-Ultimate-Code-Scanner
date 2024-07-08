import sys

def main():
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
    skip_next = False
    tokens = []
    error_messages = []
    line_number = 1

    i = 0
    while i < len(file_contents):
        if skip_next:
            skip_next = False
            i += 1
            continue

        c = file_contents[i]
        next_c = file_contents[i + 1] if i + 1 < len(file_contents) else None  # Peek at the next character

        if c == "\n":
            line_number += 1

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
                while i < len(file_contents) and file_contents[i] != "\n":
                    i += 1
                line_number += 1
            else:
                tokens.append("SLASH / null")
        elif c == " " or c == "\t":
            pass  # Ignore whitespace characters
        elif c == "\n":
            pass  # Line number increment is already handled above
        else:
            error = True
            error_messages.append("[line %d] Error: Unexpected character: %s" % (line_number, c))

        i += 1

    tokens.append("EOF  null")

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
