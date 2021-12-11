import markdown
import sys
from datetime import date

today = date.today()

filename = sys.argv[1]

header = """| [Home](https://ccrma.stanford.edu/~iran) 
            | [CV](https://ccrma.stanford.edu/~iran/CV) 
            | [Research](https://ccrma.stanford.edu/~iran/research) 
            | [Teaching](https://ccrma.stanford.edu/~iran/teaching) 
            | [Notes](https://ccrma.stanford.edu/~iran/notes) |\n""" 
bottom = """--- \n &copy; """

with open(filename+'.md', 'r') as f:
    text = f.read()
    html = markdown.markdown(header+text+bottom+str(today.year)+" Iran R. Roman")

with open(filename+'.html', 'w') as f:
    f.write('<body style="font-family: sans-serif">\n')
    f.write(html)
