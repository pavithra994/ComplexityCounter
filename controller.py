from models import *
from model.size import *
# from model.inheritence import *

class ComplexityController:
    def __init__(self,_code,language):
        # _class => indices
        self.code_complexity = None
        self.openSourceCode(_code,language)
        self.parenthesis_stack = []
        self.total_complexity = 0

    def calComplexityByLine(self,_line,_class):
        # _line => indices[start:end], _class => index
        cs, tc, nc, ci, TW, cps, cr = 0, 0, 0, 0, 0, 0, 0
        selected_class_body = self.code_complexity.classList[_class].body
        s,e = _line[0], _line[1]
        if self.checkValideLine(_line,_class):
            cs = self.code_complexity.size_complexity(_line,_class)
            tc = self.code_complexity.type_of_control_complexity(_line,_class)
            nc = self.code_complexity.nested_control_complexity(_line,_class)
            ci = self.code_complexity.inheritance_complexity(_class)
            TW = tc + nc + ci
            cps = TW * cs
            cr = self.code_complexity.recursion_complexity(_line,_class,cps)
        return cs, tc, nc, ci, TW, cps, cr

    def cal_total_complexity(self,cps,cr):
        if cr == '-':
            self.total_complexity += int(cps)
        else:
            self.total_complexity += int(cr)



    def openSourceCode(self,code,language):
        if language.lower() == 'java':
            self.code_complexity = JavaComplexity(code)
        elif language.lower() == 'cpp':
            self.code_complexity = CppComplexity(code)
        else:
            print("error")
            raise Exception('ComplexityCounter support JAVA and C++ only')
    def getClassList(self):
        return self.code_complexity.classList

    def calSize(self,line):
        return sizeComplexity(line)

    def checkValideLine(self,_line,_class):
        s,e = _line[0], _line[1]
        line = self.code_complexity.classList[_class].body[s:e]
        if re.search('\w',line):
            return True
        return False
    def reset_all(self):
        self.code_complexity.global_nc = 0
        self.total_complexity = 0