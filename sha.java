import java.io.*;
import java.util.*;
import java.math.*;
import java.security.*;
import java.nio.charset.*;

public class SHA {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        try{
            Scanner sc = new Scanner(System.in);
            String s = sc.nextLine();
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            byte[] hashBytes = md.digest(s.getBytes(StandardCharsets.UTF_8));
            StringBuilder sb = new StringBuilder();

            for(byte b : hashBytes) {
                sb.append(String.format("%02x", b));
            }

            System.out.println(sb.toString());
        }catch(NoSuchAlgorithmException e){
            System.out.println("Something Wrong");
        }
    }
}

