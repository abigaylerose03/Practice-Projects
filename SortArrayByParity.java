import java.util.*;

public class SortArrayByParity {
	public int[] sortArrayByParity(int[] A) {
		for(int j = 0, i = 0; j < A.length; j++) {
			// A[j] is even: SWAP A[j] with A[i]increment j and i 
			// A[j] is odd: just increment j 
			if(A[j] % 2 == 0) { 
				int temp = A[i]; // the swapper
				A[i++] = A[j];
				A[j] = temp;
			}

		} 
		return A;
	}

	public void printArray(int[] A) {
		System.out.println("Your array is " + Arrays.toString(A));
	}

	public static void main(String[] args) {
		int[] my_arr = {14, 2, 4, 5, 7, 345, 1, 3, 5, 44};
		SortArrayByParity ans = new SortArrayByParity();

		ans.sortArrayByParity(my_arr);
		ans.printArray(my_arr);

		// System.out.println("test");

	}
}