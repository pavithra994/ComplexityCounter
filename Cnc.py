code = open("java.java")
count = 0
stack = 0
line_number = 0

for num, line in enumerate(code,1):
    # count += 1
    if re.search('(if)\s*\(.*\)\s*\{',line):
        # count -= 1
        # count += 1
        line_number = num
        if re.search('\s*\(.*\)\s*\{',line):
            stack += 1
            
    if re.search('\s*\}',line):
        # print(line)
        if stack == 1:
            count = num - line_number
            stack -= 1
            


print(count)
# print(stack)