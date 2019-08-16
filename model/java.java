public class FibonacciMain{

    private int x;


    public static long fibonacci(long number){
        if((number == 0) ||(number==1)){
            return number;
        }
        else{
        return fibonacci(number -1) + fibonacci(number-2);
        }
    }

    public void loopTester(int y){
        for(int x=0;x<5;x++){
            System.out.print("this is for loop");
            if(y<4){
                System.out.print("this is nested if in for loop")
            }
        }

        while(true){
            System.out.print("this is while loop");
        }

        do{
            System.out.print("this is do while loop");
        }while(y)
    }

}

public class childClass extends FibonacciMain{
    private int id;
    private FibonacciMain fb;

    public static void main(String arg[]){
        id = 354;
        fb = new FibonacciMain();
         System.out.print("this is Child Class of FibonacciMain class"
    }
}