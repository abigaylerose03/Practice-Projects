public class bigOPractice {

	public static void main(String[] args) {
		System.out.println(fibonacci(9));
	}

	// example of O(n^2) time 
	public static int fibonacci(int num) {
		if(num <= 1)  return num;
		return fibonacci(num - 1) + fibonacci(num - 2);
	}


}