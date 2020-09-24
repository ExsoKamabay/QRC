from segno import *;
from segno import helpers;
from webview import *;
from json import *;
from url64 import *
html  = open("src/main.html","r").read();
def loadCSS(window):
    window.load_css(open("src/style.css","r").read());

