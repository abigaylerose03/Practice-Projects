class BinarySearch {
    int binarySearch(int arr[], int l, int r, int x) {
        if(r >= l) {
            int mid = l + (r-l) / 2;

            // if the element is present at the middle itself
            if(arr[mid] == x) {
                return mid;
            }

            // if the element x is smaller than the mid,
            // it can only be present in left subarray
            if(arr[mid] > x) 
                return binarySearch(arr, l, mid - 1, x);
            return binarySearch(arr, mid + 1, r, x); 
            
        }
        return -1;
    }
    public static void main(String[] args) {
        BinarySearch bs = new BinarySearch();
        int arr[] = {2,3,4,10,15, 20, 14, 234};
        int n = arr.length;
        int x = 234;
        int result = bs.binarySearch(arr, 0, n - 1, x);
        if(result == -1) { 
            System.out.println("element not present");
        } else {
            System.out.println("element found at index: " + result);
        }
    }
}