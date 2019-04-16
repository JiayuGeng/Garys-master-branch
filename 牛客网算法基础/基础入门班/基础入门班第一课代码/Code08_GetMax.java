package class01;

public class Code08_GetMax {

	public static int getMax(int[] arr) {
		return process(arr, 0, arr.length - 1);
	}

	// arr[L...R]范围内找最大值
	public static int process(int[] arr, int L, int R) {
		if (L == R) {
			return arr[L];
		}
		int mid = L + ((R - L) >> 1);//除去调用子过程之外的时间复杂度是O(1)
		int leftMax = process(arr, L, mid);//子过程的数据规模是减了一半是O(N/2)
		int rightMax = process(arr, mid + 1, R);//子过程的数据规模是减了一半是O(N/2)，总共2个子过程所以是2*T(N/2)
		return Math.max(leftMax, rightMax);//除去调用子过程之外的时间复杂度是O(1)
	}

}
