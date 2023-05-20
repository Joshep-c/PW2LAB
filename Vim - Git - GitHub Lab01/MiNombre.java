import java.util.Scanner;
public class BienvenidoAlCurso{
  public static void (String args []){
    Scanner scan = new Scanner(System.in);
    String name;
    
    System.out.println("Ingrese su nombre:");
    name = scan.nextLine();
    
    System.out.println("Bienvenido " + name);
  }
}
