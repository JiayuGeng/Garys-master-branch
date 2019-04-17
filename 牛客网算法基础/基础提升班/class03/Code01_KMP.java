package class03;

public class Code01_KMP {

	public static int getIndexOf(String s, String m) {
		if (s == null || m == null || m.length() < 1 || s.length() < m.length()) {
			return -1;
		}
		char[] str1 = s.toCharArray();
		char[] str2 = m.toCharArray();
		int i1 = 0;
		int i2 = 0;
		int[] next = getNextArray(str2); 		// 关于str2求解next数组
		while (i1 < str1.length && i2 < str2.length) { // 当x不越界，y也不越界
			// if y 越界了，某个位置配出了str2
			if (str1[i1] == str2[i2]) {
				i1++;
				i2++;
			} else if (next[i2] == -1) { // x位置和Y没配上。Y -> 跳到str2[0]
				i1++;
			} else { // y不在0位置上
				i2 = next[i2];
			}
		}
		return i2 == str2.length ? i1 - i2 : -1;
	}

	public static int[] getNextArray(char[] ms) { // str2 长度是M o(M)
		if (ms.length == 1) {
			return new int[] { -1 };
		}
		int[] next = new int[ms.length]; //长度就是>=2
		next[0] = -1; // 人为规定
		next[1] = 0;
		int i = 2; // 当前来到的位置，要求next值的位置
		int cn = 0; // 比对的位置，是i-1位置跳出来的前缀的下一个位置，和i-1位置字符比对（也是i-1的长度）
		while (i < next.length) {
			if (ms[i - 1] == ms[cn]) { // 配上了
				next[i++] = ++cn; // cn+1
			} else if (cn > 0) { //没配上，如果cn>0，所以还可以往前跳
				cn = next[cn]; // 跳到这
			} else { // 没配上，cn已经跳到0，不能再往前跳了
				next[i++] = 0;
			}
		}
		return next;
	}

	public static void main(String[] args) {
		String str = "abcabcababaccc";
		String match = "ababa";
		System.out.println(getIndexOf(str, match));

	}

}
