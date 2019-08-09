import re


class ComplexityFactory:
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
            temp_code = temp_code[temp_code.find(" class ")+7:]
            temp = temp_code.split(' ', 1)
            className = temp[0]
            temp_code = temp[1]
            start, end = indexOfParenthesis(temp_code,0)
            classBody = temp_code[start:end]
            temp_code = temp_code[end:]
            self.classList.append(Class(className,classBody))




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
    def __init__(self, name, body):
        self.className = name
        # self.body = body
        self.methodList = []
        self.attributeList = []
        self.methodDivider(body)

    def methodDivider(self,body):
        for indexes in re.finditer("\w*\s*\(.*\)\s*\{",body):
            name = body[indexes.start():indexes.end()].split('(',1)[0]
            # print(name)
            s,e =indexOfParenthesis(body,indexes.end()-1)
            # print(body[s:e])
            # print('----')
            self.methodList.append(Method(name,body[s:e]))


class Method:
    def __init__(self, name, code_list):
        self.methodName = name
        self.codeList = code_list


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
    for i,char in enumerate(code):
        if i >= start:
            # print(i)
            if char is '{':
                par += 1
                if par is 1:
                    start_index = i
            if char is '}':
                par -= 1
                if par is 0:
                    end_index = i+1
                    break
    return start_index, end_index