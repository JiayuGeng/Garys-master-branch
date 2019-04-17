package class08;

public class Code06_ConvertToLetterString {

	public static int number(String str) {
		if (str == null || str.length() == 0) {
			return 0;
		}
		return process(str.toCharArray(), 0);
	}

	// i之前的位置如何转化已经做过决定了
	// i...后有多少转化的结果
	public static int process(char[] chs, int i) {
		if (i == chs.length) { // i到最后了，之前做的那些决定都有效
			return 1;
		}
		if (chs[i] == '0') { // i=0，之前做的决定让我现在变成无效的状态，所以0种
			return 0;
		}
		if (chs[i] == '1') {
			int res = process(chs, i + 1); // i单独自己作为有效部分，后续有多少方法
			if (i + 1 < chs.length) {
				res += process(chs, i + 2); // (i和i+1)作为单独部分，后续有多少有效方法，从i+2开始自由选择。累加返回，就是当前i=1时候的答案
			}
			return res;
		}
		if (chs[i] == '2') {
			int res = process(chs, i + 1); // i自己作为单独的部分，后续有多少有效方法
			// i和i+1作为单独的部分且和没有超过26，后续有多少种做法
			if (i + 1 < chs.length && (chs[i + 1] >= '0' && chs[i + 1] <= '6')) {
				res += process(chs, i + 2);
			}
			return res;
		}
		// 当前i是3～9范围上，只有一种决定；str[i] = '3'~'9'
		return process(chs, i + 1);
	}

	public static void main(String[] args) {
		System.out.println(number("11111"));
	}

}
