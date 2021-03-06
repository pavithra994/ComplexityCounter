import re

############### Type of Control structure #################

def identifyControlStructure(code):
    totalCount = 0
    # for num, line in enumerate(code,1):
    if re.search('(if)\s*\(.*\)\s*\{',code):
        # Ctc = 0
        # Ctc += 1
        totalCount += 1
        # print("In code number : ",num,"-> Ctc with only if : ",Ctc)
        
        if re.search("\s*\(.*(&&).*\)\s*{", code) or re.search("\s*\(.*\||\.\)\s",code):
            # Ctc += 1
            totalCount += 1
            # print("In code number : ",num,"-> Ctc with if and && or ||: ",Ctc)

    elif re.search('(while)\s*\(.*\)\s*\{',code):
        # Ctc = 0
        # Ctc += 2
        totalCount += 2
        # print("In code number : ",num,"-> Ctc with only while : ",Ctc)
        
        if re.search("\s*\(.*(&&).*\)\s*{", code) or re.search("\s*\(.*\||\.\)\s",code):
            # Ctc += 2
            totalCount += 2
            # print("In code number : ",num,"-> Ctc with while and && or ||: ",Ctc)

    elif  re.search('(for)\s*\(.*\)\s*\{',code) :
        # Ctc = 0
        # Ctc += 2
        totalCount += 2
        # print("In code number : ",num,"-> Ctc with only for : ",Ctc)
        
        if re.search("\s*\(.*(&&).*\)\s*{", code) or re.search("\s*\(.*\||\.\)\s",code):
            # Ctc += 2
            totalCount += 2
            # print("In code number : ",num,"-> Ctc with for and && or ||: ",Ctc)

    elif  re.search('(do)\s*\{',code) :
        # Ctc = 0
        # Ctc += 2
        totalCount += 2
        # print("In code number : ",num,"-> Ctc with only do while : ",Ctc)
        
        if re.search("\s*\(.*(&&).*\)\s*{", code) or re.search("\s*\(.*\||\.\)\s",code):
            # Ctc += 2
            totalCount += 2
            # print("In code number : ",num,"-> Ctc with do while and && or ||: ",Ctc)

    elif  re.search('(catch)\s*\(.*\)\s*\{',code) :
        # Ctc = 0
        # Ctc += 1
        totalCount += 1
        # print("In code number : ",num,"-> Ctc with catch : ",Ctc)

    else:
        Ctc = 0
        # print (num," -> Ctc : ",Ctc,code)
    
    return totalCount        


############### Nested Control structure #################

def lineCounterOfNestedController(code):
    count = 0
    stack = 0
    line_number = 0

    for num, line in enumerate(code,1):
        if re.search('(while)\s*\(.*\)\s*\{',line):
            
            if re.search('\s*\(.*\)\s*\{',line):
                
                stack += 1
            if stack == 1:
                line_number += 1 
        
        if line_number > 0 :
            if stack == 1:
                if re.search('\s*\;',line):
                    line_number += 1
                    # print(num)
            if re.search('\s*\}',line):
                if stack == 1:
                    # print (line_number)
                    return line_number
                    stack =0
                    line_number=0
