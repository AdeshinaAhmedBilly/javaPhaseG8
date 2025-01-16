public class PhaseGateFactors {


 public long factorialOf(int integer) {
        
        if (integer == 0) {
            return 1;
        }
        long result = 1;
        for (int i = 1; i <= integer; i++) {
            result *= i;
        }
        return result;
    }
System.out.println("factorOf(10): " + kata.factorOf(10));

System.out.println("factorialOf(5): " + kata.factorialOf(5));