import java.util.*;

class IsBalanced {
	
	public static void main(String []arg)
	{
		Scanner sc = new Scanner(System.in);
		
		while (sc.hasNext()) {
			String input=sc.next();
            //Complete the code
        while(input.length() != (input = input.replaceAll("\\(\\)|\\[\\]|\\{\\}", "")).length());
          System.out.println(input.isEmpty());
		}
		
	}
}



