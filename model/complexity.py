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
        self.classDivider()

    def classDivider(self):
        # divide codes into classes and assign to classList

        temp_code = self.code
        start_index = 0
        className = None
        while temp_code.find(" class ") is not -1:
            temp_code = temp_code[temp_code.find(" class ") + 7:]
            # len(' class ') = 7
            # remove public, static like key words with 'class'
            temp = temp_code.split(' ', 1)
            # divide into parts in first space
            # NameOfClass extend NameOfParentClass {......}
            # temp[0]     | temp[1]
            className = temp[0]
            temp_code = temp[1]
            start, end = indexOfParenthesis(temp_code, 0)
            # indexOfParenthesis(code,stop_index) returns index of first '{' and index of couple '}'
            classBody = temp_code[start:end]
            temp_code = temp_code[end:]
            self.classList.append(Class(className, classBody, parentClassFinder(temp_code[:start+1])))

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
        self.methodDivider(body)

    def methodDivider(self, body):
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
                        self.methodList.append(Method(name, body[s - i + 1:e]))
                        body_without_methods = body_without_methods.replace(body[s - i + 1:e], '')
                        break
        # attributes divider
        for codeline in body_without_methods.strip('{}').split(';'):
            if codeline.strip() != '':
                self.attributeList.append(codeline.strip())


class Method:
    def __init__(self, name, code_list):
        self.methodName = name
        self.codeList = code_list

    def printMethod(self):
        print("method name is {}".format(self.methodName))
        print("---------------")
        print(self.codeList)


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



