import markdown
import sys

filename = sys.argv[1]

header = """| [Home](https://ccrma.stanford.edu/~iran) 
            | [Research](https://ccrma.stanford.edu/~iran/research) 
            | [Teaching](https://ccrma.stanford.edu/~iran/teaching) 
            | [Notes](https://ccrma.stanford.edu/~iran/notes) |\n""" 

with open(filename+'.md', 'r') as f:
    text = f.read()
    html = markdown.markdown(header+text)

with open(filename+'.html', 'w') as f:
    f.write('<body style="font-family: sans-serif">\n')
    f.write(html)
