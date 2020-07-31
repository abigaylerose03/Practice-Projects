import java.util.*;
public class APTest {
	
	public static int arraySum(int[] arr) {
		int sum = 0;
		for(int i = 0; i < arr.length; i++) {
			sum += arr[i];
		}
		return sum;
	} 
	
	public static int[] rowSums(int[][] arr2D) {
		int[] sum = new int[arr2D.length];
		int index = 0;
		for(int[] arr : arr2D) {
			sum[index] = arraySum(arr);
			index++;
		}
		return sum;
		
	}
	
	public static boolean isDiverse(int[][] arr2D) {

		int[] sums = rowSums(arr2D);

		Arrays.sort(sums);

		for (int i = 0; i <  sums.length - 1; i++) // we need to subtract the length so that it is inclusive
			if (sums[i] == sums[i + 1]) // + 1 because it goes through the array to check the one to the right of the given index 
				return false;

		return true;
	}

	
	
	public static void main(String[] args) {
		int[] myArr = {4, 5, 3, 2};
		int[][] my2DArr = {{2, 5, 2, 52, 2, }, {2, 41, 5, 1}, {523, 2, 1}};
		System.out.println(arraySum(myArr));
		System.out.println(rowSums(my2DArr));
		
		System.out.println(isDiverse(my2DArr));
		
		int[] oldArray = {1, 2, 3, 4, 5, 6, 7, 8, 9};
		int[][] newArray = new int[3][3];
		
		int row = 0;
		int col = 0;
		
		for(int value : oldArray) {
			newArray[row][col] = value;
			row++;
			if((row % 3) == 0) {
				col++;
				System.out.println(row);
				row = 0;
			}
		}
		System.out.println(newArray[0][2]);
	}

}


