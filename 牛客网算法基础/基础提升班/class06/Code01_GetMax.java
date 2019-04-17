package class06;

public class Code01_GetMax {

	// 保证n不是1就是0
	// 0->1,1->0
	public static int flip(int n) {
		return n ^ 1;
	}

	// 如果n是非负数return1
	// 如果n是负数返回0
	public static int sign(int n) {
		return flip((n >> 31) & 1);
	}

	//
	public static int getMax1(int a, int b) {
		int c = a - b;
		int scA = sign(c); // 返回A的条件，一定是0或者1
		int scB = flip(scA); // 返回B的条件，一定是0或者1
		// scA为0，scB必为1，scA为1，scB必为0
		return a * scA + b * scB; // 在a的条件下返回a，在b的条件下返回b
	}

	public static int getMax2(int a, int b) {
		int c = a - b;
		int sa = sign(a); // a的符号
		int sb = sign(b);
		int sc = sign(c);
		int difSab = sa ^ sb; // a跟b的符号一样么？不一样为1，一样为0
		int sameSab = flip(difSab); // a跟b的符号一样么？不一样为0，一样为1
		int returnA = difSab * sa + sameSab * sc; // 当a和b符号不一样，并且a为非负数，返回a。当a和b一样，他俩做差，返回a
		int returnB = flip(returnA); // 如果不返回a，那么就返回b
		return a * returnA + b * returnB;
	}

	public static void main(String[] args) {
		int a = -16;
		int b = 1;
		System.out.println(getMax1(a, b));
		System.out.println(getMax2(a, b));
		a = 2147483647;
		b = -2147480000;
		System.out.println(getMax1(a, b)); // wrong answer because of overflow
		System.out.println(getMax2(a, b));

	}

}
