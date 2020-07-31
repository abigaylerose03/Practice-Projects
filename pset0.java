import java.util.*;

public class pset0 {
	// LEARN TO CODE, CHANGE THE WORLD
	public static void main(String[] args) {
		int[] arr = {15, 25, 5, 15};
		
		System.out.println(addArray(arr, 20));
	}

	public static boolean addArray(int[] arr, int k) {
		Arrays.sort(arr);
		for(int i = 0, j = arr.length - 1; i < j;) {
			int sum = arr[i] + arr[j];
			if(sum < k) 
				i++;
			 else if(sum > k)
			 	j--;
			 else 
			 	return true;
		}	
		return false;
	} 

}


