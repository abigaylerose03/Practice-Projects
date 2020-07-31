import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) {
    System.out.println("Hello world!");
    int[] array = {4, 52, 3,523,5,23,5};
    sort(array);
    System.out.println(java.util.Arrays.toString(array));
  }

    public static void sort(int[] array) {
        quickSort(array, 0, array.length - 1);
    }

    private static void quickSort(int[] array, int left, int right) {
        if (left >= right) {
            return;
        }
        int pivot = array[left + (right - left) / 2];
        int index = partition(array, left, right, pivot);
        quickSort(array, left, index  - 1);
        quickSort(array, index, right);
    }

    private static int partition(int[] array, int left, int right, int pivot) {
        while (left <= right) {
            while (array[left] < pivot && left < right) {
                left++;
            }
            while (array[right] > pivot && right >= left) {
                right--;
            }
            if (left <= right) {
                swap(array, left, right);
                left++;
                right--;
            }
        }
        return left;
    }

    private static void swap(int[] array, int left, int right) {
        int i = array[left];
        array[left] = array[right];
        array[right] = i;
    }

}

