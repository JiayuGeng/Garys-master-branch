package class05;

public class Code02_MaxDistanceInTree {

	public static class Node {
		public int value;
		public Node left;
		public Node right;

		public Node(int data) {
			this.value = data;
		}
	}

	public static int maxDistance(Node head) {
		int[] record = new int[1];
		return posOrder(head, record);
	}

	public static class ReturnType{ // 左树右树提出同样的2个信息
		public int maxDistance;
		public int h;

		public ReturnType(int m, int h) {
			this.maxDistance = m;;
			this.h = h;
		}
	}

	public static ReturnType process(Node head) {
		if(head == null) { // 空树 max dis = 0，height = 0
			return new ReturnType(0,0);
		}
		ReturnType leftReturnType = process(head.left); // 直接得到左右的信息
		ReturnType rightReturnType = process(head.right);
		// 拆黑盒
		int includeHeadDistance = leftReturnType.h + 1 + rightReturnType.h; // 可能性3，从左扎到右，左高+右高+1（x）
		int p1 = leftReturnType.maxDistance; // 可能性1，最大高度是左树最max
		int p2 = rightReturnType.maxDistance;// 可能性2，最大高度是右树最max
		int resultDistance = Math.max(Math.max(p1, p2), includeHeadDistance);
		int hitself  = Math.max(leftReturnType.h, leftReturnType.h) + 1; // 左右树高度最大的+1就是高度
		return new ReturnType(resultDistance, hitself); // 自己要按照递归函数返回要求
	}

	public static int posOrder(Node head, int[] record) {
		if (head == null) {
			record[0] = 0;
			return 0;
		}
		int lMax = posOrder(head.left, record);
		int maxfromLeft = record[0];
		int rMax = posOrder(head.right, record);
		int maxFromRight = record[0];
		int curNodeMax = maxfromLeft + maxFromRight + 1;
		record[0] = Math.max(maxfromLeft, maxFromRight) + 1;
		return Math.max(Math.max(lMax, rMax), curNodeMax);
	}

	public static void main(String[] args) {
		Node head1 = new Node(1);
		head1.left = new Node(2);
		head1.right = new Node(3);
		head1.left.left = new Node(4);
		head1.left.right = new Node(5);
		head1.right.left = new Node(6);
		head1.right.right = new Node(7);
		head1.left.left.left = new Node(8);
		head1.right.left.right = new Node(9);
		System.out.println(maxDistance(head1));

		Node head2 = new Node(1);
		head2.left = new Node(2);
		head2.right = new Node(3);
		head2.right.left = new Node(4);
		head2.right.right = new Node(5);
		head2.right.left.left = new Node(6);
		head2.right.right.right = new Node(7);
		head2.right.left.left.left = new Node(8);
		head2.right.right.right.right = new Node(9);
		System.out.println(maxDistance(head2));

	}

}
