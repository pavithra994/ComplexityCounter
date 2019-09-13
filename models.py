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
import  re
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
        _end = 0
        for class_index in re.finditer("\sclass\s*", self.code):
            pstart, pend = indexOfParenthesis(self.code, class_index.end())
            class_seg = self.code[class_index.end():pstart].split(' ', 1)
            # class_seg[0] is class name and if there is parent class class_seg[1] is that keywords
            class_name = class_seg[0]
            try:
                parent_name = parentClassFinder(class_seg[1])
            except IndexError:
                parent_name = 'Object'
            class_body = self.code[_end:pend].strip()
            self.classList.append(Class(class_name, class_body, parent_name))
            _end = pend



class CppComplexity(CodeComplexity):
    pass


class Class:
    def __init__(self, name, _body, parent_class):
        self.className = name
        self.body = _body
        self.parentClass = parent_class
        self.methodList = []
        self.attributeList = []
        self.complexity = 0
        # setMethodListAndAttributeList need to implement in CodeComplexity class
        # self.setMethodListAndAttributeList(_body)

    def set_complexity(self,value):
        self.complexity = value


class Method:
    def __init__(self, name, _code):
        self.methodName = name
        self.codeList = _code


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
        if segment == 'extends':
            return keywords[i + 1]
    return 'Object'


### test codes here ###

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
    createKingdom(x);
  }
}public class Student extends App{
    private int sid;
    private String sname;
    private String Address;

    public void print(){
        print.all();
    }

    public void delete(){
        delete.all();
    }

}'''

c = JavaComplexity(code)