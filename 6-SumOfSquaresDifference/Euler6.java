
/**
 * 
 * he sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
 *
 */
public class Euler6 {

    static long sumToN(int n)
    {
        return (n*(n+1))/2;
    }
    
    static long squareOfSum(int n)
    {
        long sum = sumToN(n);
        return sum*sum;
    }
    
    //Is there a closed-form expression of this?
    static long sumOfSquares(int n)
    {
        long sum = 385; // start at n = 10
        
        for (int i = 11; i <= n; i++)
        {
            sum = sum + (i * i);
        }
        
        return sum;
    }
    
    /**
     * @param args
     */
    public static void main(String[] args) {
        System.out.println(sumToN(10));
        System.out.println(squareOfSum(10));
        System.out.println(sumOfSquares(10));
        System.out.println(squareOfSum(100));
        System.out.println(sumOfSquares(100));
        System.out.println(squareOfSum(100) - sumOfSquares(100));
    }

}

