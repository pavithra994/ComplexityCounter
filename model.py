"""
    here we implement all logics in ComplexityCounter
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


class Model:
    def __init__(self):
        pass

    def classRecognizer(self,code):
        self.classesList= []

    def readLineByLine(self,code):
        self.LineList = []
        start = 0
        for i,char in enumerate(code):
            if char == ';' or char == '{' or char == '}':
                self.LineList.append(code[start:i+1])
                start = i+1

        return self.LineList




