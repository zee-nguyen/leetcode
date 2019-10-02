// https://leetcode.com/problems/perfect-number/


class PerfectNumber {
    public boolean checkPerfectNumber(int num) {
        if (num == 1 || num == 0) {
            return false;
        }
        // find all divisors of num then check for sum
        int sum = 0;
        
        for (int i = 1; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                if (i != 1) {
                    sum += num/i;
                }
                sum += i;
            }
        }
        
        return sum == num;
    }
}