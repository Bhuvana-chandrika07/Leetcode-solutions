class Solution {
    public int findTheDistanceValue(int[] arr1, int[] arr2, int d) {

        int answer = arr1.length;
        Arrays.sort(arr2);

        for(int i = 0; i < arr1.length; ++i) {
            int leftBound = arr1[i] - d;
            int rightBound = arr1[i] + d;

            boolean elemExistsInBounds = binaryBoundCheck(arr2, leftBound, rightBound);

            if(elemExistsInBounds)
                answer--;
        }

        return answer;
    }

    private boolean binaryBoundCheck(int[] arr, int leftBound, int rightBound) {
        int left = 0;
        int right = arr.length - 1;

        while(left <= right) {
            int mid = left + (right - left) / 2;

            // Both boundaries are inclusive
            if(leftBound <= arr[mid] && arr[mid] <= rightBound)
                return true;
            else if(rightBound < arr[mid])
                right = mid - 1;
            else
                left = mid + 1;
        }

        return false;
    }
}