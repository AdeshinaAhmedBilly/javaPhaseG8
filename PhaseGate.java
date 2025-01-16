public class PhaseGate {

  

    public boolean isPrimeNumber(int integer) {
        
        if (integer <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(integer); i++) {
            if (integer % i == 0) {
                return false;
            }
        }
        return true;
    }
 public static void main(String[] args) {
       PhaseGate PhaseGate = new PhaseGate();

        
     
        System.out.println("isPrimeNumber(5): " + PhaseGate.isPrimeNumber(5));
        System.out.println("isPrimeNumber(10): " + PhaseGate.isPrimeNumber(10));
 	}
      }