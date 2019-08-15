import re

def sizeComplexity(code_line):
    '''
    separate  " Strings "  - (\".*\")
    separate operators +,-,., ++ (replace with spaces)
    split into keywords
    calculate
    '''
    line = code_line.strip(';')
    total_size = 0
    total_size, line = countStrings(line)
    # find and count relational, logical, assignment operators and replace <<space>>
    pattern ='\+\+|\-\-|\+=|\-=|\*=|\/=|==|!=|>|<|<=|>=|&&|\|\||!'
    total_size += len(re.findall(pattern,line))
    line = re.sub(pattern," ", line)
    print(line)
    pattern = '=|\+|\-|\*|\/|\%|\,|\.'
    total_size += len(re.findall(pattern,line))
    line = re.sub(pattern," ", line)

    # replace all ; {} () with space
    pattern=';|{|}|\(|\)'
    line = re.sub(pattern," ", line)
    # split into keywords
    keywords = line.split()

    # total_size += len(keywords)
    for keyword in keywords:
        if keyword == 'new' or keyword == 'delete' or keyword == 'throw' or keyword == 'throws':
            total_size += 2
        else:
            total_size += 1


    return total_size


def stringFinder(line):
    start_index = -1
    end_index = -1
    count = 0
    for i,char in enumerate(line):
        if char == '"':
            if count == 0:
                start_index = i
                count=1
                continue
            if count == 1:
                end_index = i+1
                return start_index,end_index
    return None


    # strings = re.findall(pattern_string,code_line)
    # keywords = re.findall(r"[\w']+",code_line)
strings='System.out.println("test" +"bla")'

def countStrings(line):
    count = 0
    temp = line
    while stringFinder(temp) is not None:
        s,e = stringFinder(temp)
        temp = temp[:s]+temp[e:]
        count+=1
    return count,temp

# sizeComplexity('System.out.println("test" +"bla")')
# s,e = stringFinder(strings)
# print(strings[:s]+strings[e:])
# print(countStrings('sdfg'))