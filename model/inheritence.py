from model.complexity import *

code = '''class Employee{  
 float salary=40000;  
}  
class Programmer extends Employee{  
 int bonus=10000;  
 public static void main(String args[]){  
   Programmer p=new Programmer();  
   System.out.println("Programmer salary is:"+p.salary);  
   System.out.println("Bonus of Programmer is:"+p.bonus);  
}  
}  '''

C = parentClassFinder(code)

def checkInheritence(i):
    for i in C.classList:
        if Class.className == "Object":
            return 1

        else:
            return Class.className.match +1

# ashimi try this
    
def calCi(class_obj,class_list):
    if class_obj.parentClass == "Object":
        return 2
    else:
        for cl in class_list:
            if cl.className == class_obj.parentClass:
                return calCi(cl, class_list) + 1

c1 = Class("a","some text","Object")
c2 = Class("b","some text","a")
c3 = Class("c","some text","b")
c4 = Class("d","some text","c")

clist = [c1,c2,c3,c4]

calCi(c3,clist)
