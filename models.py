"""
    here we implement all logic in ComplexityCounter
        complexity measuring functions
            - calculateBySize
            - calculateTypeOfControl
            - calculateNestingOfControl
            - calculateByInheritance
            - calculateTotalWeight
            - calculateProgramStatementComplexity
            - calculateByRecursion
            - calculateComplexityOfProgram (final output)

        code reading functions
            - trimming ( remove unnecessary code lines like comments import)
            - languageRecognizer ( return either cpp or java, also validate)
            - readLineByLine ( divided into line using ; , { , }  )
            - readWordByWord ( divided into word using <space> , <,> , <.> , ( , ), <operators> )
            - classRecognizer (returns class name and class code segments)
            - methodRecognizer (returns method all code segments)
            - parameterRecognizer ???
"""
import configurations


class CodeComplexity:
    def __init__(self,code):
        self.code = code
        self.classList = []
        self.setClassList()

    def commentRemover(self,code):
        pass

    def setClassList(self):
        pass


class JavaComplexity(CodeComplexity):
    def commentRemover(self, code):
        super().commentRemover(code)

    def setClassList(self):
        super().setClassList()


class CppComplexity(CodeComplexity):
    pass





class Class:
    def __init__(self, name, _body, parent_class):
        self.className = name
        # self.body = body
        self.parentClass = parent_class
        self.methodList = []
        self.attributeList = []
        self.complexity = 0
        # setMethodListAndAttributeList need to implement in CodeComplexity class
        self.setMethodListAndAttributeList(_body)

    def set_complexity(self,value):
        self.complexity = value


class Method:
    def __init__(self, name, _code):
        self.methodName = name
        self.codeList = _code
