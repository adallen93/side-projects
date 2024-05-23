"""This is a reference for ANSI color escape sequences I frequently use.

I found this page helpful: https://gist.github.com/JBlond/2fea43a3049b38287e5e9cefc87b2124
"""

# Variables to set
REDT = "\033[91m"
REDB = "\033[41m"
GREENT = "\033[92m"
GREENB = "\033[42m"
BLUET = "\033[94m"
BLUEB = "\033[44m"
GRAYT = "\033[90m"
GRAYB = "\033[100m"
RESET = "\033[0m"

# Example usage
print(f"|{REDT}Warning message {RESET}|Normal message|")
print(f"|Another normal|{GREENB}And congratulations{RESET}|")

# Remember you can combine fonts, colors and backgrounds by placing a ';' character between the numbers
