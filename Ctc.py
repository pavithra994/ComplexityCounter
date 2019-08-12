import re
code = open("text.txt")
# Ctc = 0

for num, line in enumerate(code,1):
    if re.search('(if)\s*\(.*\)\s*\{',line):
        Ctc = 0
        Ctc += 1
        print("In line number : ",num,"-> Ctc with only if : ",Ctc)
        
        if re.search("\s*\(.*(&&).*\)\s*{", line) or re.search("\s*\(.*\||\.\)\s",line):
            Ctc += 1
            print("In line number : ",num,"-> Ctc with if and && or ||: ",Ctc)

    if re.search('(while)\s*\(.*\)\s*\{',line):
        Ctc = 0
        Ctc += 2
        print("In line number : ",num,"-> Ctc with only while : ",Ctc)
        
        if re.search("\s*\(.*(&&).*\)\s*{", line) or re.search("\s*\(.*\||\.\)\s",line):
            Ctc += 2
            print("In line number : ",num,"-> Ctc with while and && or ||: ",Ctc)

    if  re.search('(for)\s*\(.*\)\s*\{',line) :
        Ctc = 0
        Ctc += 2
        print("In line number : ",num,"-> Ctc with only for : ",Ctc)
        
        if re.search("\s*\(.*(&&).*\)\s*{", line) or re.search("\s*\(.*\||\.\)\s",line):
            Ctc += 2
            print("In line number : ",num,"-> Ctc with for and && or ||: ",Ctc)

    if  re.search('(do)\s*\{',line) :
        Ctc = 0
        Ctc += 2
        print("In line number : ",num,"-> Ctc with only do while : ",Ctc)
        
        if re.search("\s*\(.*(&&).*\)\s*{", line) or re.search("\s*\(.*\||\.\)\s",line):
            Ctc += 2
            print("In line number : ",num,"-> Ctc with do while and && or ||: ",Ctc)

    if  re.search('(catch)\s*\(.*\)\s*\{',line) :
        Ctc = 0
        Ctc += 1
        print("In line number : ",num,"-> Ctc with catch : ",Ctc)



# code = open("text.txt")

# ifCondition  = "if ("
# ifCondition2 = "if("
# whileCondition = "while("
# whileCondition2 = "while ("
# logical  = "&&"
# logical2 ="||"
# ifConditionPoint = 0
# logicalPoint = 0
# whileConditionPoint = 0
# logicWithWhileConditionPoint = 0
# Ctc = 0

# for num, line in enumerate(code,1):
#     if ifCondition in line or ifCondition2 in line:
#         print('found if in line number: ',num)
#         ifConditionPoint += 1
#         if logical in line or logical2 in line:
#             print("found && || in line number : ",num)
#             logicalPoint += 1
#     if whileCondition in line or whileCondition2 in line:
#         print('found while in line number: ',num)
#         whileConditionPoint += 2
#         if logical in line or logical2 in line:
#             print("found && || in line number : ",num)
#             logicWithWhileConditionPoint += 2


# print('ifConditionPoint',ifConditionPoint)
# print("logicalPoint",logicalPoint)
# print('whileConditionPoint',whileConditionPoint)
# print('logicWithWhileConditionPoint',logicWithWhileConditionPoint)
# Ctc = ifConditionPoint+logicalPoint
# print("Ctc ponits for if condition: ",Ctc)
# print("Ctc ponits for while condition: ",whileConditionPoint+logicWithWhileConditionPoint)