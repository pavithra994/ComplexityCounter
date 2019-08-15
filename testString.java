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

}