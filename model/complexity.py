import re

"""
        pass the code as parameter when creating an instance of the ComplexityFactory class.
         c =   ComplexityFactory(some-java-code)
         for cl in c.classList:
            for met in cl.methodList:
                # do something
                # run complexity measuring functions on met   
"""


class CodeFactory:
    def __init__(self, code):
        self.code = code
        self.classList = []
        # self.classDivider()
        self.setClassList()

    # def classDivider(self):
    #     # divide codes into classes and assign to classList
    #
    #     temp_code = self.code
    #     start_index = 0
    #     className = None
    #
    #     while temp_code.find(" class ") is not -1:
    #         temp_code = temp_code[temp_code.find(" class ") + 7:]
    #         # len(' class ') = 7
    #         # remove public, static like key words with 'class'
    #         temp = temp_code.split(' ', 1)
    #         # divide into parts in first space
    #         # NameOfClass extend NameOfParentClass {......}
    #         # temp[0]     | temp[1]
    #         className = temp[0]
    #         temp_code = temp[1]
    #         start, end = indexOfParenthesis(temp_code, 0)
    #         # indexOfParenthesis(code,stop_index) returns index of first '{' and index of couple '}'
    #         classBody = temp_code[start:end]
    #         temp_code = temp_code[end:]
    #         self.classList.append(Class(className, classBody, parentClassFinder(temp_code[:start+1])))

    def setClassList(self):
        temp_code = self.code
        for class_index in re.finditer("\sclass\s*",temp_code):
            pstart, pend = indexOfParenthesis(temp_code,class_index.end())
            class_seg = temp_code[class_index.end():pstart].split(' ',1)
            # class_seg[0] is class name and if there is parent class class_seg[1] is that keywords
            class_name = class_seg[0]
            try:
                parent_name = parentClassFinder(class_seg[1])
            except IndexError:
                parent_name = 'Object'
            class_body = temp_code[pstart:pend].strip(' {}')
            self.classList.append(Class(class_name,class_body , parent_name))

    def __str__(self):
        line1 = ""
        for i,cls in enumerate(self.classList,1):
            line1 += str(i) + ".\t"+ cls.__str__() +"\n"
        return line1







    # def classDivider(code):
    #     print("function running --")
    #     print(code)
    #     temp_code = code
    #     start = 0
    #     while start is not -1:
    #         print("inside loop")
    #         start = temp_code.find(" class ")
    #         temp_code = temp_code[start + 6:]
    #         print(temp_code)


class Class:
    def __init__(self, name, body, parent_class):
        self.className = name
        # self.body = body
        self.parentClass = parent_class
        self.methodList = []
        self.attributeList = []
        self.setMethodListAndAttributeList(body)

    def setMethodListAndAttributeList(self, body):
        body_without_methods = body
        for indexes in re.finditer("\w*\s*\(.*\)\s*\{", body):
            # need will return functions and also  if, while, for, catch
            name = body[indexes.start():indexes.end()].split('(', 1)[0]
            # print(name)
            if name != 'if':
                # print("function name is {}".format(name))
                s, e = indexOfParenthesis(body, indexes.end() - 1)
                # print(body[s:e])
                for i, c in enumerate(body[s::-1]):
                    if c == '}' or c == ';':
                        self.methodList.append(Method(name, body[s - i + 1:e].strip()))
                        body_without_methods = body_without_methods.replace(body[s - i + 1:e], '')
                        break
        # attributes divider
        for codeline in body_without_methods.strip('{}').split(';'):
            if codeline.strip() != '':
                self.attributeList.append(codeline.strip())

    def __str__(self):
        attr = ""
        for at in self.attributeList:
            attr += at +"\n"

        meth = ""
        for m in self.methodList:
            meth += m.__str__() + "\n"
        return "class name\t: "+ self.className+ "\tparent name\t: "+self.parentClass + "\n\n"+ attr+"\n"+meth

class Method:
    def __init__(self, name, code_list):
        self.methodName = name
        self.codeList = code_list

    def printMethod(self):
        print("method name is {}".format(self.methodName))
        print("---------------")
        print(self.codeList)

    def __str__(self):
        return self.codeList

# def indexOfParenthesis(code):
#     start_index = -1
#     end_index = -1
#     par = 0
#     for i,char in enumerate(code):
#         if char is '{':
#             par += 1
#             if par is 1:
#                 start_index = i
#         if char is '}':
#             par -= 1
#             if par is 0:
#                 end_index = i+1
#                 break
#     return start_index, end_index


def indexOfParenthesis(code, start):
    start_index = -1
    end_index = -1
    par = 0
    for i, char in enumerate(code):
        if i >= start:
            # print(i)
            if char is '{':
                par += 1
                if par is 1:
                    start_index = i
            if char is '}':
                par -= 1
                if par is 0:
                    end_index = i + 1
                    break
    return start_index, end_index


def parentClassFinder(code):
    keywords = code.split(' ')
    for i, segment in enumerate(keywords):
        if segment == 'extend':
            return keywords[i+1]
    return 'Object'

############### Nested Control structure #################

def lineCounterOfNestedController(code):
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
    return count

# code = open("java.java")
# print (lineCounterOfNestedController(code))
code.close()
            
############### Type of Control structure #################

def identifyControlStructure(code):
    for num, line in enumerate(code,1):
        if re.search('(if)\s*\(.*\)\s*\{',line):
            Ctc = 0
            Ctc += 1
            print("In line number : ",num,"-> Ctc with only if : ",Ctc)
            
            if re.search("\s*\(.*(&&).*\)\s*{", line) or re.search("\s*\(.*\||\.\)\s",line):
                Ctc += 1
                print("In line number : ",num,"-> Ctc with if and && or ||: ",Ctc)

        elif re.search('(while)\s*\(.*\)\s*\{',line):
            Ctc = 0
            Ctc += 2
            print("In line number : ",num,"-> Ctc with only while : ",Ctc)
            
            if re.search("\s*\(.*(&&).*\)\s*{", line) or re.search("\s*\(.*\||\.\)\s",line):
                Ctc += 2
                print("In line number : ",num,"-> Ctc with while and && or ||: ",Ctc)

        elif  re.search('(for)\s*\(.*\)\s*\{',line) :
            Ctc = 0
            Ctc += 2
            print("In line number : ",num,"-> Ctc with only for : ",Ctc)
            
            if re.search("\s*\(.*(&&).*\)\s*{", line) or re.search("\s*\(.*\||\.\)\s",line):
                Ctc += 2
                print("In line number : ",num,"-> Ctc with for and && or ||: ",Ctc)

        elif  re.search('(do)\s*\{',line) :
            Ctc = 0
            Ctc += 2
            print("In line number : ",num,"-> Ctc with only do while : ",Ctc)
            
            if re.search("\s*\(.*(&&).*\)\s*{", line) or re.search("\s*\(.*\||\.\)\s",line):
                Ctc += 2
                print("In line number : ",num,"-> Ctc with do while and && or ||: ",Ctc)

        elif  re.search('(catch)\s*\(.*\)\s*\{',line) :
            Ctc = 0
            Ctc += 1
            print("In line number : ",num,"-> Ctc with catch : ",Ctc)

        else:
            Ctc = 0
            print (num," -> Ctc : ",Ctc,line)

code = open("java.java")
print (identifyControlStructure(code))
code.close()

# testing

code = '''
//this is testin java

public class App {

  private static final Logger LOGGER = LoggerFactory.getLogger(App.class);

  private King king;
  private Castle castle;
  private Army army;

  public void createKingdom(final KingdomFactory factory) {
    setKing(factory.createKing());
    setCastle(factory.createCastle());
    setArmy(factory.createArmy());
  }
  
  int main(string y){
    test();
  }
}

public class pavi extend parent {

  private static final Logger LOGGER = LoggerFactory.getLogger(App.class);

  private King king;
  private Castle castle;
  private Army army;

  public void createKingdom(final KingdomFactory factory) {
    setKing(factory.createKing());
    setCastle(factory.createCastle());
    setArmy(factory.createArmy());
  }
}'''
c = CodeFactory(code)

print(c)

