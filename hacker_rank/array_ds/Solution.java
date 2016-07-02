import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner input = new Scanner(System.in);
        int n;
        int arr[];
        
        n = input.nextInt();
        arr = new int [n];
        
        for(int i = 0; i < n; i++) {
            arr[i] = input.nextInt();
        }
        
        for(int i = n-1; i >= 0; i--) {
            System.out.print(arr[i] + " ");
        }
    }
}