import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);
        int value = input.nextInt();
        int size = input.nextInt();
        int arr[] = new int [size];
        
        for(int i = 0; i < size; i++) {
            arr[i] = input.nextInt();
        }
        
        int index = -1;
        for(int i = 0; i < size; i++) {
            if(value == arr[i]) {
                index = i;
                break;
            }
        }
        
        System.out.print(index);
    }
}