package class08;

public class Code01_Hanoi {

	public static void hanoi(int n) {
		if (n > 0) {
			func(n, n, "left", "mid", "right");
		}
	}

	public static void func(int rest, int down, String from, String help, String to) {
		if (rest == 1) { // rest = 1 就是代表只剩下最上面的圆盘了，直接就是from到to
			System.out.println("move " + down + " from " + from + " to " + to);
		} else {
			func(rest - 1, down - 1, from, to, help);// 把i-1都从from移动到help，to做了帮助函数，方便i移动到to
			func(1, down, from, help, to); // 直接执行打印，什么都不做
			func(rest - 1, down - 1, help, from, to); // 1～i-1从help挪到to那里，from作为了帮助函数
		}
	}

	public static void main(String[] args) {
		int n = 3;
		hanoi(n);
	}

}
