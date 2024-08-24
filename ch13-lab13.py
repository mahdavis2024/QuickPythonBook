'''Lab 13: Final fixes to wc
If you look at the man page for the wc utility, you see two command­line options that do
very similar things. ­c makes the utility count the bytes in the file, and ­m makes it
count characters (which in the case of some Unicode characters can be two or more
bytes long). In addition, if a file is given, it should read from and process that file, but if
no file is given, it should read from and process stdin.
Rewrite your version of the wc utility to implement both the distinction between bytes
and characters and the ability to read from files and standard input.'''

import sys

def wc(filename = None ):
    if filename == None:
        content = sys.stdin.read()
    else:
        with open(filename, 'r') as file:
            content = file.read()

    lines = content.splitlines()
    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    char_count = len(content)

    return line_count, word_count, char_count

if __name__ == "__main__":
    filename = input('Enter your text file name example.txt: ')
    lines, words, chars = wc(filename)
    print(f"Lines: {lines}, Words: {words}, Characters: {chars}")



    

'''The `if __name__ == "__main__":` line is a special construct in Python that allows you to execute code only when the script is run directly (i.e., not when it's imported as a module by another script).

When you run a Python script, Python assigns a special variable `__name__` to the script. The value of `__name__` is the name of the script, including the file extension.

When you run a script directly, `__name__` is set to `"__main__"`. When you import a script as a module, `__name__` is set to the name of the module.

So, when you write `if __name__ == "__main__":`, you're checking if the current script is being run directly (i.e., `__name__ == "__main__"`). If it is, then the code inside the `if` block is executed.

In other words, this construct allows you to write code that can be executed both when the script is run directly and when it's imported as a module by another script. It's often used to define "main" entry points for scripts, or to provide functionality that can be used by other scripts.

Here's an example:

```
# my_script.py
print("Hello, world!")

if __name__ == "__main__":
    print("This is the main entry point!")
```

If you run `my_script.py` directly, it will print:

```
Hello, world!
This is the main entry point!
```

But if you import `my_script` as a module in another script, it will only print:

```
Hello, world!
```

Because the code inside the `if __name__ == "__main__":` block is only executed when the script is run directly.
'''