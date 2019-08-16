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
        self.code = self.commentRemover(code)
        self.classList = []
        # self.classDivider()
        self.setClassList()

    def setClassList(self):
        temp_code = self.code
        for class_index in re.finditer("\sclass\s*", temp_code):
            pstart, pend = indexOfParenthesis(temp_code, class_index.end())
            class_seg = temp_code[class_index.end():pstart].split(' ', 1)
            # class_seg[0] is class name and if there is parent class class_seg[1] is that keywords
            class_name = class_seg[0]
            try:
                parent_name = parentClassFinder(class_seg[1])
            except IndexError:
                parent_name = 'Object'
            class_body = temp_code[pstart:pend].strip(' {}')
            self.classList.append(Class(class_name, class_body, parent_name))

    def __str__(self):
        line1 = ""
        for i, cls in enumerate(self.classList, 1):
            line1 += str(i) + ".\t" + cls.__str__() + "\n"
        return line1

    def commentRemover(self,code):
        return re.sub('\/\/.*',"",code)


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
            attr += at + "\n"

        meth = ""
        for m in self.methodList:
            meth += m.__str__() + "\n"
        return "class name\t: " + self.className + "\tparent name\t: " + self.parentClass + "\n\n" + attr + "\n" + meth

    def getAttributeList(self):
        return self.attributeList

    def getMethodList(self):
        method_list = []
        for m in self.methodList:
            method_list.append(m.getCodeListLineByLine)


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

    def getCodeListLineByLine(self):
        return self.codeList.split('\n')

    def hasRecurtion(self):
        pattern = self.methodName + '\s*\('
        start, end = indexOfParenthesis(self.codeList,0)
        if re.search(pattern,self.codeList[start:end]) is None:
            return False
        return True


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
        if segment == 'extends':
            return keywords[i + 1]
    return 'Object'


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
    createKingdom(x);
  }
}


public class Student extend App{
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
c = CodeFactory(code)

print(c)

