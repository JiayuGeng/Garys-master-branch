package class07;

public class Code04_HorseJump {

	public static int getWays(int x, int y, int step) {
		return process(x, y, step);
	}

	// 跳了多少步step
	// x，y在的位置
	// 从（0，0）出发跳了step后，来到（x，y）位置有多少种，
	public static int process(int x, int y, int step) {
		if (x < 0 || x > 8 || y < 0 || y > 9) {
			return 0;
		}
		// 把后续无效的返回0
		if (step == 0) {
			return (x == 0 && y == 0) ? 1 : 0;
		}
		return process(x - 1, y + 2, step - 1)
				+ process(x + 1, y + 2, step - 1)
				+ process(x + 2, y + 1, step - 1)
				+ process(x + 2, y - 1, step - 1)
				+ process(x + 1, y - 2, step - 1)
				+ process(x - 1, y - 2, step - 1)
				+ process(x - 2, y - 1, step - 1)
				+ process(x - 2, y + 1, step - 1);
	}

	// 三维表
	public static int dpWays(int x, int y, int step) {
		if (x < 0 || x > 8 || y < 0 || y > 9 || step < 0) {
			return 0;
		}
		int[][][] dp = new int[9][10][step + 1];
		dp[0][0][0] = 1;
		for (int h = 1; h <= step; h++) { // 层

			for (int r = 0; r < 9; r++) {
				for (int c = 0; c < 10; c++) {
					dp[r][c][h] += getValue(dp, r - 1, c + 2, h - 1); // 每一个在h层[r][c]的东西只依赖下一层的位置
					dp[r][c][h] += getValue(dp, r + 1, c + 2, h - 1);
					dp[r][c][h] += getValue(dp, r + 2, c + 1, h - 1);
					dp[r][c][h] += getValue(dp, r + 2, c - 1, h - 1);
					dp[r][c][h] += getValue(dp, r + 1, c - 2, h - 1);
					dp[r][c][h] += getValue(dp, r - 1, c - 2, h - 1);
					dp[r][c][h] += getValue(dp, r - 2, c - 1, h - 1);
					dp[r][c][h] += getValue(dp, r - 2, c + 1, h - 1);
				}
			}
		}
		return dp[x][y][step];
	}

	// 记忆表
	public static int getValue(int[][][] dp, int row, int col, int step) {
		if (row < 0 || row > 8 || col < 0 || col > 9) {
			return 0;
		}
		return dp[row][col][step];
	}

	public static void main(String[] args) {
		int x = 7;
		int y = 7;
		int step = 10;
		System.out.println(getWays(x, y, step));
		System.out.println(dpWays(x, y, step));
	}
}
