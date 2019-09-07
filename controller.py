from models import *


class ComplexityController:
    def __init__(self,_code):
        # _class => indices
        self.code_complexity = None

    def calComplexityByLine(self,_line):
        # _line => indices
        ctc, cnc, cs = 0
        return ctc, cnc, cs

    def openSourceCode(self,code,language):
        if language.lower() == 'java':
            self.code_complexity = JavaComplexity(code)
        elif language.lower() == 'cpp':
            self.code_complexity = CppComplexity(code)
        else:
            print("error")

    def getClassList(self):
        return self.code_complexity.classList
