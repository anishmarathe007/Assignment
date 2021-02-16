from word_count import compute
from word_count import ExtensionNotSupportedError

fname = input("Enter the filename\n")

try:
    compute(fname)
except FileNotFoundError as e:
    print(e)
except ExtensionNotSupportedError as e1:
    print(e1)
