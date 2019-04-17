package class04;

import java.util.LinkedList;

public class Code01_SlidingWindowMaxArray {

	public static int[] getMaxWindow(int[] arr, int w) {
		if (arr == null || w < 1 || arr.length < w) {
			return null;
		}
		LinkedList<Integer> qmax = new LinkedList<Integer>();
		int[] res = new int[arr.length - w + 1]; // 最终要收集多少结果； 8-3+1=6
		int index = 0;
		for (int i = 0; i < arr.length; i++) { // 窗口滑动；i是窗口R（右边届）
			// i -> arr[i]
			// arr[qmax.peekLast()] <= arr[i] 双端队列尾巴位置小于当前数时，从尾巴弹出，弹到不能再弹，加数进去
			while (!qmax.isEmpty() && arr[qmax.peekLast()] <= arr[i]) {
				qmax.pollLast();
			}
			qmax.addLast(i);

			// i-w是过期的下标，过期了就弹出
			if (qmax.peekFirst() == i - w) {
				qmax.pollFirst();
			}
			if (i >= w - 1) { // 窗口形成了
				res[index++] = arr[qmax.peekFirst()];
			}
		}
		return res;
	}

	// for test
	public static void printArray(int[] arr) {
		for (int i = 0; i != arr.length; i++) {
			System.out.print(arr[i] + " ");
		}
		System.out.println();
	}

	public static void main(String[] args) {
		int[] arr = { 4, 3, 5, 4, 3, 3, 6, 7 };
		int w = 3;
		printArray(getMaxWindow(arr, w));

	}

}
