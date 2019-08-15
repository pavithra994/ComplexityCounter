import re

############### Type of Control structure #################

def identifyControlStructure(code):
    totalCount = 0
    for num, line in enumerate(code,1):
        if re.search('(if)\s*\(.*\)\s*\{',line):
            # Ctc = 0
            # Ctc += 1
            totalCount += 1
            # print("In line number : ",num,"-> Ctc with only if : ",Ctc)
            
            if re.search("\s*\(.*(&&).*\)\s*{", line) or re.search("\s*\(.*\||\.\)\s",line):
                # Ctc += 1
                totalCount += 1
                # print("In line number : ",num,"-> Ctc with if and && or ||: ",Ctc)

        elif re.search('(while)\s*\(.*\)\s*\{',line):
            # Ctc = 0
            # Ctc += 2
            totalCount += 2
            # print("In line number : ",num,"-> Ctc with only while : ",Ctc)
            
            if re.search("\s*\(.*(&&).*\)\s*{", line) or re.search("\s*\(.*\||\.\)\s",line):
                # Ctc += 2
                totalCount += 2
                # print("In line number : ",num,"-> Ctc with while and && or ||: ",Ctc)

        elif  re.search('(for)\s*\(.*\)\s*\{',line) :
            # Ctc = 0
            # Ctc += 2
            totalCount += 2
            # print("In line number : ",num,"-> Ctc with only for : ",Ctc)
            
            if re.search("\s*\(.*(&&).*\)\s*{", line) or re.search("\s*\(.*\||\.\)\s",line):
                # Ctc += 2
                totalCount += 2
                # print("In line number : ",num,"-> Ctc with for and && or ||: ",Ctc)

        elif  re.search('(do)\s*\{',line) :
            # Ctc = 0
            # Ctc += 2
            totalCount += 2
            # print("In line number : ",num,"-> Ctc with only do while : ",Ctc)
            
            if re.search("\s*\(.*(&&).*\)\s*{", line) or re.search("\s*\(.*\||\.\)\s",line):
                # Ctc += 2
                totalCount += 2
                # print("In line number : ",num,"-> Ctc with do while and && or ||: ",Ctc)

        elif  re.search('(catch)\s*\(.*\)\s*\{',line) :
            # Ctc = 0
            # Ctc += 1
            totalCount += 1
            # print("In line number : ",num,"-> Ctc with catch : ",Ctc)

        else:
            Ctc = 0
            # print (num," -> Ctc : ",Ctc,line)
    
    return totalCount        


############### Nested Control structure #################

def lineCounterOfNestedController(code):
    count = 0
    stack = 0
    line_number = 0

    for num, line in enumerate(code, 1):
        # count += 1
        if re.search('(if)\s*\(.*\)\s*\{', line):
            # count -= 1
            # count += 1
            line_number = num
            if re.search('\s*\(.*\)\s*\{', line):
                stack += 1

        if re.search('\s*\}', line):
            # print(line)
            if stack == 1:
                count = num - line_number
                stack -= 1
    return count
