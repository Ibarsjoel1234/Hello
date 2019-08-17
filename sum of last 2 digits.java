import java.util.*; 
import java.lang.*; 
public class Main{ 
    //public static int firstDigit(int n) 
    //{
        //while (n >= 10)
        //{
          //  n /=10;
        //}
      // return n;
    //}
    public static int lastDigit(int n) 
    { 
        return (n % 10);
        
    }
    public static int lastsecond(int m)
    {
        return (m%10);
    }
    
// Main function starts here:::::::::::::::::
    public static void main(String argc[]) 
    { 
        int n,m;
        System.out.println("Enter the number");
        Scanner scn = new Scanner(System.in);
        n = scn.nextInt();
        System.out.println("second value");
        Scanner scn1 = new Scanner(System.in);
        m = scn1.nextInt();
        System.out.println("The values for firstDigit and lastDigit:");
        System.out.println(lastDigit(n) +" "+ lastsecond(m)); 
    } 
} 
