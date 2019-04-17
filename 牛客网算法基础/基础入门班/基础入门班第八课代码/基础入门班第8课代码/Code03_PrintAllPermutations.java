package class08;

import java.util.ArrayList;

public class Code03_PrintAllPermutations {

	public static ArrayList<String> Permutation(String str) {
		ArrayList<String> res = new ArrayList<>();
		if (str == null || str.length() == 0) {
			return res;
		}
		char[] chs = str.toCharArray();
		process(chs, 0, res);
		res.sort(null);
		return res;
	}
	// str[i...]范围上，所有的字符都可以在i位置，后续都去尝试
	// str[0..i-1]范围上，是之前做的选择
	// 请把所有的字符串形成的全排列加到res里去
	public static void process(char[] chs, int i, ArrayList<String> res) {
		if (i == chs.length) {
			res.add(String.valueOf(chs));
		}
		boolean[] visit = new boolean[26]; // visit[0...25] => 代表a这个东西我试没试过...
		for (int j = i; j < chs.length; j++) {
			if (!visit[chs[j] - 'a']) { // 这个字符我之前没试过，因为visit[chs[j] = a，a的ask - a的ask =0, !visit[chs[j] - 'a' = 0才开始试，=1则不试
				visit[chs[j] - 'a'] = true; // 把它标记成试过
				swap(chs, i, j); // i往后所有的字符都可以来到i位置
				process(chs, i + 1, res); // 谁在i位置在str中就改过来，然后走i的分支后续
				swap(chs, i, j); // 交换回来，形成原来的样子
			}
		}
	}

	public static void swap(char[] chs, int i, int j) {
		char tmp = chs[i];
		chs[i] = chs[j];
		chs[j] = tmp;
	}

}
