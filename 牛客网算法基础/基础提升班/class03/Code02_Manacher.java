package class03;

public class Code02_Manacher {

	public static char[] manacherString(String str) {
		char[] charArr = str.toCharArray();
		char[] res = new char[str.length() * 2 + 1];
		int index = 0;
		for (int i = 0; i != res.length; i++) {
			res[i] = (i & 1) == 0 ? '#' : charArr[index++];
		}
		return res;
	}

	public static int maxLcpsLength(String str) {
		if (str == null || str.length() == 0) {
			return 0;
		}
		char[] charArr = manacherString(str); // 1221 -> #1#2#2#1#
		int[] pArr = new int[charArr.length]; // 回文半径数组
		int R = -1; // R是回文半径右边界再下一个位置，C..R-1 是最后回文半径区域
		int C = -1; // 取得R时候的中心
		int max = Integer.MIN_VALUE; // 发现的最大回文半径

		for (int i = 0; i != charArr.length; i++) {
			// i位置的回文半径，至少是多长
			// R是回文半径再下一个位置，如果成立表示i在R内
			// pArr[2 * C - i] 是i'的回文半径，这两个谁小要睡
			// 四种情况，至少返回一个结果
			pArr[i] = R > i ? Math.min(pArr[2 * C - i], R - i) : 1;

			// 所有情况都适用，小2小3情况中了的话就直接break
			// 正常小2小3不需要扩，但是带着，这样代码短
			while (i + pArr[i] < charArr.length && i - pArr[i] > -1) {
				if (charArr[i + pArr[i]] == charArr[i - pArr[i]]) //扩成功
					pArr[i]++; // 回文半径增加
				else {
					break;
				}
			}


			if (i + pArr[i] > R) { // R跟C有没有同步更新
				R = i + pArr[i];
				C = i;
			}
			max = Math.max(max, pArr[i]); // 记录最大的回文半径
		}
		return max - 1; // 原始串长度=半径-1 1221 -> #1#2#2#1#, 5-1 = 4
	}

	public static void main(String[] args) {
		String str1 = "abc1234321ab";
		System.out.println(maxLcpsLength(str1));
	}

}
