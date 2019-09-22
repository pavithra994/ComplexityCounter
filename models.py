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
        self.global_nc = 0
        self.ignore_text_list = []
        self.set_ignore_text_list()
        self.setClassList()


    def set_ignore_text_list(self):
        pass

    def setClassList(self):
        pass

    def type_of_control_complexity(self,_line,_class):
        pass

    def nested_control_complexity(self):
        pass

    def inheritance_complexity(self, _class):
        pass

    def recursion_complexity(self,_line, _class,cps):
        pass

class JavaComplexity(CodeComplexity):

    # def __init__(self, code):
    #     super().__init__(code)

    def set_ignore_text_list(self):
        # TODO: check indexes are correct
        for indexes in re.finditer('\/\/.*', self.code):
            # comment = [indexes.start(), indexes.end()]
            for index in range(indexes.start(), indexes.end()):
                self.ignore_text_list.append(index)

        # string finder
        for indexes in re.finditer('"([^\\"]|\\")*"', self.code):
            for index in range(indexes.start(), indexes.end()):
                self.ignore_text_list.append(index)


    def setClassList(self):
        _end = 0
        for class_index in re.finditer("\sclass\s*", self.code):
            if class_index.start() in self.ignore_text_list:
                continue
            pstart, pend = indexOfParenthesis(self.code, class_index.end())
            class_seg = self.code[class_index.end():pstart].split(' ', 1)
            # class_seg[0] is class name and if there is parent class class_seg[1] is that keywords
            class_name = class_seg[0]
            try:
                parent_name = parentClassFinder(class_seg[1])
            except IndexError:
                parent_name = 'Object'
            class_body = self.code[_end:pend].strip()
            self.classList.append(Class(class_name, '\n'+class_body, parent_name))
            _end = pend

        if len(self.classList) is 0:
            self.classList.append(Class('None', '\n'+self.code, 'None'))


    def functionRecognizer(self,_line):
        # _func = re.match()
        return None

    def type_of_control_complexity(self,_line,_class):
        body = self.classList[_class].body
        tc = 0
        func_set = re.findall('\w*\s*\(.*\)', body[_line[0]:_line[1]])
        for func in func_set:
            func_name = func.split('(',1)[0].strip()
            func_condition = func.split('(',1)[1].strip()
            if func_name == 'if':
                tc +=1
            if func_name == 'for':
                tc +=2
            if func_name == 'while':
                tc +=2
            if func_name == 'catch':
                tc += 1
            condition_set = re.findall('&&|\|\|', func_condition)
            for _condition in condition_set:
                tc += 1
        # TODO: switch case
        return tc

    def nested_control_complexity(self,_line,_class):
        body = self.classList[_class].body
        nc = 0
        func_set = re.findall('\w*\s*\(.*\)', body[_line[0]:_line[1]])
        for func in func_set:
            func_name = func.split('(', 1)[0].strip()
            if func_name == 'if':
                self.global_nc += 1
        if re.search('}',body[_line[0]:_line[1]]) and self.global_nc > 0:
            self.global_nc -= 1
        return self.global_nc


    def inheritance_complexity(self,_class):
        class_obj = self.classList[_class]
        if class_obj.parentClass == 'None':
            return 1
        if class_obj.parentClass == "Object":
            return 2
        else:
            for i,cl in enumerate(self.classList):
                if cl.className == class_obj.parentClass:
                    return self.inheritance_complexity(i) + 1

    def recursion_complexity(self,_line, _class,cps):
        for method in self.classList[_class].methodList:
            if method.codeList[0] <= _line[0] <= method.codeList[1]:
                if method.hasRecurtion():
                    return cps*2
        return '-'

class CppComplexity(CodeComplexity):
    def set_ignore_text_list(self):
        for indexes in re.finditer('\/\/.*', self.code):
            # comment = [indexes.start(), indexes.end()]
            for index in range(indexes.start(), indexes.end()):
                self.ignore_text_list.append(index)

        # string finder
        for indexes in re.finditer('"([^\\"]|\\")*"', self.code):
            for index in range(indexes.start(), indexes.end()):
                self.ignore_text_list.append(index)

    def setClassList(self):
        _end = 0
        for class_index in re.finditer("\sclass\s*", self.code):
            if class_index.start() in self.ignore_text_list:
                continue
            pstart, pend = indexOfParenthesis(self.code, class_index.end())
            class_seg = self.code[class_index.end():pstart].split(' ', 1)
            # class_seg[0] is class name and if there is parent class class_seg[1] is that keywords
            class_name = class_seg[0]
            try:
                parent_name = parentClassFinder(class_seg[1])
            except IndexError:
                parent_name = 'Object'
            class_body = self.code[_end:pend].strip()
            self.classList.append(Class(class_name, '\n' + class_body, parent_name))
            _end = pend

        if len(self.classList) is 0:
            self.classList.append(Class('None', '\n' + self.code, 'None'))

    def type_of_control_complexity(self,_line,_class):
        body = self.classList[_class].body
        tc = 0
        func_set = re.findall('\w*\s*\(.*\)', body[_line[0]:_line[1]])
        for func in func_set:
            func_name = func.split('(', 1)[0].strip()
            func_condition = func.split('(', 1)[1].strip()
            if func_name == 'if':
                tc += 1
            if func_name == 'for':
                tc += 2
            if func_name == 'while':
                tc += 2
            if func_name == 'catch':
                tc += 1
            condition_set = re.findall('&&|\|\|', func_condition)
            for _condition in condition_set:
                tc += 1
        # TODO: switch case
        return tc

    def nested_control_complexity(self,_line,_class):
        body = self.classList[_class].body
        nc = 0
        func_set = re.findall('\w*\s*\(.*\)', body[_line[0]:_line[1]])
        for func in func_set:
            func_name = func.split('(', 1)[0].strip()
            if func_name == 'if':
                self.global_nc += 1
        if re.search('}', body[_line[0]:_line[1]]) and self.global_nc > 0:
            self.global_nc -= 1
        return self.global_nc

    def inheritance_complexity(self, _class):
        class_obj = self.classList[_class]
        if class_obj.parentClass == 'None':
            return 1
        if class_obj.parentClass == "Object":
            return 2
        else:
            for i, cl in enumerate(self.classList):
                if cl.className == class_obj.parentClass:
                    return self.inheritance_complexity(i) + 1

    def recursion_complexity(self, _line, _class, cps):
        for method in self.classList[_class].methodList:
            if method.codeList[0] <= _line[0] <= method.codeList[1]:
                if method.hasRecurtion():
                    return cps * 2
        return '-'

class Class:
    def __init__(self, name, _body, parent_class):
        self.className = name
        self.body = _body
        self.parentClass = parent_class
        self.methodList = []
        self.attributeList = []
        self.complexity = 0
        self.commentList = [] # comment = [start index, end index]
        self.setMethodsList()
        self.setCommentList()
        # setMethodListAndAttributeList need to implement in CodeComplexity class
        # self.setMethodListAndAttributeList(_body)

    def set_complexity(self,value):
        self.complexity = value

    def setMethodsList(self):
        for indexes in re.finditer("\w*\s*\(.*\)\s*\{", self.body):
            # for comment in self.commentList:
            #     if not (comment[0] <= indexes.start() <= comment[1]):
            name = self.body[indexes.start():indexes.end()].split('(', 1)[0]

            if (name != 'if') and (name != 'for') and (name != 'while'):
                # print("function name is {}".format(name))
                s, e = indexOfParenthesis(self.body, indexes.end() - 1)
                _s=s
            for c in self.body[_s::-1]:
                if c == '\n':
                    break
                s -= 1

            self.methodList.append(Method(name,[s+1,e],self))

    def setCommentList(self):
        for indexes in re.finditer('\/\/.*',self.body):
            commnet = [indexes.start(),indexes.end()]
            self.commentList.append(commnet)

class Method:
    def __init__(self, name, _code, _class):
        self.methodName = name
        self.codeList = _code
        self._class = _class

    def hasRecurtion(self):
        pattern = self.methodName + '\s*\('
        s, e = indexOfParenthesis(self._class.body,self.codeList[0])
        print(s)
        print(e)
        code = self._class.body[s:e]
        if re.search(pattern,code) is None:
            return False
        return True


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

def indexConverter(index,text):
    _line, _char, _index = 0, 0, 0
    # if insert 'line.colunm' return str index
    if type(index) is str:
        r, c = index.split('.')
        _line = 1
        for ch in text:
            _index += 1
            if ch == '\n':
                _line +=1
            if _line == int(r):
                if _char == int(c):
                    break
                _char +=1
        if int(r)==1:
            return _index - 1
        return _index
    for line in text[:index].split('\n'):
        _char = 0
        _line +=1
        for c in line:
            _char +=1
    return str(_line)+'.'+str(_char)

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
        //delete.all();
    }

}'''

c = JavaComplexity(code)

