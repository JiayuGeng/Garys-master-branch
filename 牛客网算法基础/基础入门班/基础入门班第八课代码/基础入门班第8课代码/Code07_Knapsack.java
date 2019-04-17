package class08;

public class Code07_Knapsack {

	public static int maxValue1(int[] weights, int[] values, int bag) {
		return process1(weights, values, 0, 0, bag);
	}

	// i ... 往后的货物自由选择，形成最大价值返回
	// 重量不要超过bag
	// process1 ——》之前做的决定所达到的重量
	public static int process1(int[] weights, int[] values, int i, int alreadyweight, int bag) {
		if (alreadyweight > bag) {
			return 0;
		}
		if (i == weights.length) { // 没超重，但是没货了，价值=0
			return 0;
		}
		return Math.max(
				// 不要i货，获得不了value[i], alreadyweight重量不会增加，i+1位置再去决定
				process1(weights, values, i + 1, alreadyweight, bag),
				// 要i货物 我就能得到value[i]， 后续value是i+1做决定，并且alreadyweight + weight[i]，带着新的负担，让i+1做选择
				values[i] + process1(weights, values, i + 1, alreadyweight + weights[i], bag));
	}

	public static int maxValue2(int[] c, int[] p, int bag) {
		int[][] dp = new int[c.length + 1][bag + 1];
		for (int i = c.length - 1; i >= 0; i--) {
			for (int j = bag; j >= 0; j--) {
				dp[i][j] = dp[i + 1][j];
				if (j + c[i] <= bag) {
					dp[i][j] = Math.max(dp[i][j], p[i] + dp[i + 1][j + c[i]]);
				}
			}
		}
		return dp[0][0];
	}

	public static void main(String[] args) {
		int[] weights = { 3, 2, 4, 7 };
		int[] values = { 5, 6, 3, 19 };
		int bag = 11;
		System.out.println(maxValue1(weights, values, bag));
		System.out.println(maxValue2(weights, values, bag));
	}

}
