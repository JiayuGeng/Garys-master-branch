package class08;

import java.util.ArrayList;
import java.util.List;

public class Code02_PrintAllSubsquences {

	public static void printAllSubsquence(String str) {
		char[] chs = str.toCharArray();
		process(chs, 0);
	}

	// 当前来到i位置，要和不要，走两条路
	// 之前的选择，所形成的结果，是str
	public static void process(char[] chs, int i) {
		if (i == chs.length) {
			System.out.println(String.valueOf(chs));
			return;
		}
		process(chs, i + 1); // 要当前字符的路
		char tmp = chs[i]; // 当前字符记一下
		chs[i] = 0; // 把i位置改成0
		process(chs, i + 1); // 不要当前字符的路（因为chs中i位置是0，所以就是不要当前字符）。两条路是通过chs空间的复用实现的
		chs[i] = tmp;
	}

	public static void function(String str) {
		char[] chs = str.toCharArray();
		process(chs, 0, new ArrayList<Character>());
	}

	// str 出发，当前来到i位置，要和不要，走两条路
	// res是之前的选择，所形成的列表
	public static void process(char[] chs, int i, List<Character> res) {
		if(i == chs.length) { // 当来到终止位置的时候，之前做的选择打印一下
			printList(res);
		}
		List<Character> resKeep = copyList(res); // 把之前选择copy出新的一份
		resKeep.add(chs[i]); // 把当前字符加进去
		process(chs, i+1, resKeep); // 去做后续过程。这条路是：要当前字符的路
		List<Character> resNoInclude = copyList(res);
		process(chs, i+1, resNoInclude); // 不要当前字符的路
	}

	public static void printList(List<Character> res) {
		// ...;
	}

	public static List<Character> copyList(List<Character> list){
		return null;
	}


	public static void main(String[] args) {
		String test = "abc";
		printAllSubsquence(test);
	}

}
