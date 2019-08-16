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
    if(x || y){
     do.this;
    }
  }
}


public class Student extends App{
    private int sid;
    private String sname= "student name";
    private String Address;


    public void print(x,y){
        print(this);
    }

    public void delete(){
        delete.all();
        system.out.print("this is"+sname)
        y=x+1-3;
        x++;
        y--;
        r += 8;

        if(y==x)
        !(t!=u)
        }

     public void createKingdom(final KingdomFactory factory) {
    setKing(factory.createKing());
    setCastle(factory.createCastle());
    setArmy(factory.createArmy());
    if(x || y){
     do.this;
    }
  }


  int rtt;



	private int sid;
	private String s_name;
	private String address;

	//default constructor
	public Student() {
		this.address = "Rathnapura";
	}

	//para constructor
	public Student(int sid, String s_name) {
		this.address = "Rathnapura";
		this.sid = sid;
		this.s_name = s_name;
	}

	//coping constructor
	public Student(Student s) {
		this.address = s.getAddress();
		this.sid = s.getSid();
		this.s_name = s.getS_name();
	}

	public int getSid() {
		return sid;
	}

	public void setSid(int sid) {
		this.sid = sid;
	}
	public String getS_name() {
		return s_name;
	}
	public void setS_name(String s_name) {
		this.s_name = s_name;
	}
	public String getAddress() {
		return address;
	}
	public void setAddress(String address) {
		this.address = address;
	}
	public void print() {
		System.out.println(this.s_name);
	}



	public static void main(String[] args) {
		//Declureing Object
		Student s1 = new Student(100,"Kuura");
		Student s2 = new Student(101,"pavithra");

		Student s3 = new Student(s1);
		//Calling functions

//		s1.setSid(100);
//		s1.setS_name("Kuura");
//		s1.setAddress("Rathnapura");


		System.out.println(s1.getSid());
		System.out.println(s1.getS_name());
		System.out.println(s1.getAddress());

		s1.print();
		s2.print();
		s3.print();


	}

}


}

