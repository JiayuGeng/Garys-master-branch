package class01;

public class Code07_EvenTimesOddTimes {

	public static void printOddTimesNum1(int[] arr) {
		int eO = 0;
		for (int cur : arr) {
			eO ^= cur; // 把所有数异或起来
		}
		System.out.println(eO); //最终输出则是结果
	}

	public static void printOddTimesNum2(int[] arr) {
		int eO = 0, eOhasOne = 0;
		for (int curNum : arr) {
			eO ^= curNum;
		}
		// eor -> a ^ b
		int rightOne = eO & (~eO + 1);
		// 二进制中把最右侧的1提取出来（也就是视频中找出第5位是1的位置）
		//x=     01001101000
		//y=～   10110010111
		//z=～+1 10110011000
		//x^z=   00000001000
		for (int cur : arr) {
			if ((cur & rightOne) != 0) { //那个位置上是1的数异或否则不异或
				eOhasOne ^= cur; // eor'
			}
		}
		System.out.println(eOhasOne + " " + (eO ^ eOhasOne));
	}

	public static void main(String[] args) {
		int a = 5;
		int b = 7;

		a = a ^ b;
		b = a ^ b;
		a = a ^ b;

		System.out.println(a);
		System.out.println(b);

		int[] arr1 = { 3, 3, 2, 3, 1, 1, 1, 3, 1, 1, 1 };
		printOddTimesNum1(arr1);

		int[] arr2 = { 4, 3, 4, 2, 2, 2, 4, 1, 1, 1, 3, 3, 1, 1, 1, 4, 2, 2 };
		printOddTimesNum2(arr2);

	}

}
