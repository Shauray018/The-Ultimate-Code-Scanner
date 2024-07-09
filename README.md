# 🚀 Super Awesome Lox Tokenizer: The Ultimate Code Scanner 🚀

Hey there! Welcome to the Tokenizer Script README. This script is designed to read a file and tokenize its contents. It supports various tokens like parentheses, braces, operators, and more. Plus, it can handle numbers, strings, and even identifiers! Let's dive right in.

## Usage

First things first, you need to run this script from the command line. Here's the command you'll use:

```bash
./your_program.sh tokenize <filename> 
```
Replace `<filename>` with the name of the file you want to tokenize.

## What It Does

When you run the script, it reads the file and spits out tokens. These tokens are basically small pieces of the file's content that the script recognizes. For example, things like `(`, `)`, `{`, `}`, numbers, strings, and even reserved keywords (like `if`, `else`, `while`, etc.) are all turned into tokens.

## Example
Let's say you have a file named `test.lox` with the following content:
```
Copy123 123.456 .456 123.
// expect: NUMBER 123 123.0
// expect: NUMBER 123.456 123.456
// expect: DOT .
// expect: NUMBER 456 456.0
// expect: NUMBER 123 123.0
// expect: DOT .
// expect: EOF null
```
When you run the script like this:
```bash
bashCopy./your_program.sh tokenize test.lox
```
You'll get the following output:
```
CopyNUMBER 123 123.0
NUMBER 123.456 123.456
DOT .
NUMBER 456 456.0
NUMBER 123 123.0
DOT .
EOF null
```
## Handling Errors

The script is pretty smart and will catch some common errors. For example, if it finds an invalid number or an unterminated string, it'll let you know with an error message. And yes, it'll even give you the line number where it found the error!

## Exit Codes

The script uses exit codes to indicate success or failure:

-`0`: Everything went well!

-`65`: Oops, something went wrong.

## Important Notes

-This script assumes the input file uses the `.lox` extension, but feel free to use any file you like.

-It handles comments, so anything after `//` on a line will be ignored.

-It recognizes reserved keywords and will output them in uppercase.

## Final Thoughts
That's pretty much it! This script is a handy tool for tokenizing your files, and it's pretty straightforward to use. If you run into any issues or have any questions, feel free to tweak the code and see what happens. Happy coding!

Enjoy your tokenizing adventures!