package class04;

import java.util.List;
import java.util.ArrayList;
import java.util.Stack;

public class Code02_MonotonousStack {
	// 给定arr，i -> arr[i]
	// 返回的结果
	// int 含义：
	// [
	// 		[0],[1] 长度为2
	// 		[0],[1] 长度为2
	// 		[0],[1] 长度为2
	// ]
	public static int[][] getNearLessNoRepeat(int[] arr) { // 无重复值的
		int[][] res = new int[arr.length][2];
		Stack<Integer> stack = new Stack<>();
		for (int i = 0; i < arr.length; i++) { // i -> arr[i]
			// arr[stack.peek()] > arr[i] 栈顶数>当前数弹出，因为从小->大
			while (!stack.isEmpty() && arr[stack.peek()] > arr[i]) {
				int popIndex = stack.pop(); // 弹出的东西popIndex ->代表的数是arr[popIndex]
				// 判断左边压没压东西
				int leftLessIndex = stack.isEmpty() ? -1 : stack.peek(); // 栈为空则-1，栈不为空则是栈顶
				res[popIndex][0] = leftLessIndex;
				res[popIndex][1] = i;
			}
			stack.push(i);
		}
		while (!stack.isEmpty()) { // 遍历完成后，栈里还有东西，扫尾阶段
			int popIndex = stack.pop();
			int leftLessIndex = stack.isEmpty() ? -1 : stack.peek(); // 栈为空则-1，栈不为空则是栈顶
			res[popIndex][0] = leftLessIndex;
			res[popIndex][1] = -1;
		}
		return res;
	}

	// arr可以有重复值，也可无重复值
	public static int[][] getNearLess(int[] arr) {
		int[][] res = new int[arr.length][2];
		Stack<List<Integer>> stack = new Stack<>();
		for (int i = 0; i < arr.length; i++) {
			//arr[stack.peek().get(0)] > arr[i] 从列表中随便拿出一个与当前值比较
			while (!stack.isEmpty() && arr[stack.peek().get(0)] > arr[i]) {
				List<Integer> popIs = stack.pop();
				// 取位于下面位置的列表中，最晚加入的那个
				int leftLessIndex = stack.isEmpty() ? -1 : stack.peek().get(
						stack.peek().size() - 1); // get下个列表中最后那个位置
				for (Integer popi : popIs) {
					res[popi][0] = leftLessIndex;
					res[popi][1] = i;
				}
			}
			// i位置开始进栈
			// 如果栈顶数跟你一样，你们加一起
			// 否则重新建列表，加进去（就是正常加）
			if (!stack.isEmpty() && arr[stack.peek().get(0)] == arr[i]) {
				stack.peek().add(Integer.valueOf(i));
			} else { // arr[i] 一定大于当前栈顶代表数字
				ArrayList<Integer> list = new ArrayList<>();
				list.add(i);
				stack.push(list);
			}
		}
		while (!stack.isEmpty()) { // 收尾阶段
			List<Integer> popIs = stack.pop();
			// 取位于下面位置的列表中，最晚加入的那个
			int leftLessIndex = stack.isEmpty() ? -1 : stack.peek().get(
					stack.peek().size() - 1);
			for (Integer popi : popIs) {
				res[popi][0] = leftLessIndex;
				res[popi][1] = -1;
			}
		}
		return res;
	}

	// for test
	public static int[] getRandomArrayNoRepeat(int size) {
		int[] arr = new int[(int) (Math.random() * size) + 1];
		for (int i = 0; i < arr.length; i++) {
			arr[i] = i;
		}
		for (int i = 0; i < arr.length; i++) {
			int swapIndex = (int) (Math.random() * arr.length);
			int tmp = arr[swapIndex];
			arr[swapIndex] = arr[i];
			arr[i] = tmp;
		}
		return arr;
	}

	// for test
	public static int[] getRandomArray(int size, int max) {
		int[] arr = new int[(int) (Math.random() * size) + 1];
		for (int i = 0; i < arr.length; i++) {
			arr[i] = (int) (Math.random() * max) - (int) (Math.random() * max);
		}
		return arr;
	}

	// for test
	public static int[][] rightWay(int[] arr) {
		int[][] res = new int[arr.length][2];
		for (int i = 0; i < arr.length; i++) {
			int leftLessIndex = -1;
			int rightLessIndex = -1;
			int cur = i - 1;
			while (cur >= 0) {
				if (arr[cur] < arr[i]) {
					leftLessIndex = cur;
					break;
				}
				cur--;
			}
			cur = i + 1;
			while (cur < arr.length) {
				if (arr[cur] < arr[i]) {
					rightLessIndex = cur;
					break;
				}
				cur++;
			}
			res[i][0] = leftLessIndex;
			res[i][1] = rightLessIndex;
		}
		return res;
	}

	// for test
	public static boolean isEqual(int[][] res1, int[][] res2) {
		if (res1.length != res2.length) {
			return false;
		}
		for (int i = 0; i < res1.length; i++) {
			if (res1[i][0] != res2[i][0] || res1[i][1] != res2[i][1]) {
				return false;
			}
		}

		return true;
	}

	// for test
	public static void printArray(int[] arr) {
		for (int i = 0; i < arr.length; i++) {
			System.out.print(arr[i] + " ");
		}
		System.out.println();
	}

	public static void main(String[] args) {
		int size = 10;
		int max = 20;
		int testTimes = 2000000;
		for (int i = 0; i < testTimes; i++) {
			int[] arr1 = getRandomArrayNoRepeat(size);
			int[] arr2 = getRandomArray(size, max);
			if (!isEqual(getNearLessNoRepeat(arr1), rightWay(arr1))) {
				System.out.println("Oops!");
				printArray(arr1);
				break;
			}
			if (!isEqual(getNearLess(arr2), rightWay(arr2))) {
				System.out.println("Oops!");
				printArray(arr2);
				break;
			}
		}
	}
}
