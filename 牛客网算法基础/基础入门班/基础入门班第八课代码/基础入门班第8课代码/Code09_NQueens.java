package class08;

public class Code09_NQueens {

	public static int num1(int n) {
		if (n < 1) {
			return 0;
		}
		int[] record = new int[n]; // record[i] = i行的皇后放在了第几列
		return process1(0, record, n); // 第0行放皇后，所有信息计入在record，不要超过n行
	}

	public static int process1(int i, int[] record, int n) {
		if (i == n) {
			return 1; // i来到终止位置说明之前做的选择找到一种合法的
		}
		int res = 0;
		for (int j = 0; j < n; j++) {
			// 当前i行的皇后，放在j列，会不会和0～i-1的皇后共行，列，斜线？
			// 如果是，则无效
			// 如果不是，则有效
			if (isValid(record, i, j)) { // 检查第i行j列的皇后和0～i-1行（记录者record里的）每一个皇后是否都不共列，斜线
				record[i] = j; // 如果是有效的，那么就在这一列上点上i行的皇后
				res += process1(i + 1, record, n); // 后续继续试
			}
		}
		return res;
	}

	// record[0~i-1]位置你需要看
	public static boolean isValid(int[] record, int i, int j) {
		for (int k = 0; k < i; k++) {
			// 0～i-1是否跟当前j共列，是false，|| 共斜线(列数相减的绝对值 == 行数相减的绝对值 y-y == x-x)
			if (j == record[k] || Math.abs(record[k] - j) == Math.abs(i - k)) {
				return false;
			}
		// 如果都不返回false 有效
		}
		return true;
	}

	public static int num2(int n) {
		if (n < 1 || n > 32) {
			return 0;
		}
		int upperLim = n == 32 ? -1 : (1 << n) - 1;
		return process2(upperLim, 0, 0, 0);
	}

	public static int process2(int upperLim, int colLim, int leftDiaLim,
			int rightDiaLim) {
		if (colLim == upperLim) {
			return 1;
		}
		int pos = 0;
		int mostRightOne = 0;
		pos = upperLim & (~(colLim | leftDiaLim | rightDiaLim));
		int res = 0;
		while (pos != 0) {
			mostRightOne = pos & (~pos + 1);
			pos = pos - mostRightOne;
			res += process2(upperLim, colLim | mostRightOne,
					(leftDiaLim | mostRightOne) << 1,
					(rightDiaLim | mostRightOne) >>> 1);
		}
		return res;
	}

	public static void main(String[] args) {
		int n = 14;

		long start = System.currentTimeMillis();
		System.out.println(num2(n));
		long end = System.currentTimeMillis();
		System.out.println("cost time: " + (end - start) + "ms");

		start = System.currentTimeMillis();
		System.out.println(num1(n));
		end = System.currentTimeMillis();
		System.out.println("cost time: " + (end - start) + "ms");

	}
}
