#! python3
# mapIt.py - Open Google Map in browser with address from sys arg or clipboard
import sys
import pyperclip
import webbrowser
import urllib.parse
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
    address = urllib.parse.quote_plus(address, safe='')
    webbrowser.open(f'https://www.google.com/maps/place/{address}')
else:
    address = pyperclip.paste()
    address = urllib.parse.quote_plus(address, safe=''
    webbrowser.open(f'https://www.google.com/maps/place/{address}')
