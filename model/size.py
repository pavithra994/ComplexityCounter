import re

def sizeComplexity(code_line):
    '''
    separate  " Strings "  - (\".*\")
    separate operators +,-,., ++ (replace with spaces)
    split into keywords
    calculate

    '''
    keywords = re.findall(r"[\w']+",code_line)

    print(keywords)