package class05;

public class Code01_MorrisTraversal {

	public static class Node {
		public int value;
		Node left;
		Node right;

		public Node(int data) {
			this.value = data;
		}
	}

	// 中序
	// 只能来到自己一次节点，直接打印，能来到2次节点，第二次打印
	public static void morrisIn(Node head) {
		if (head == null) {
			return;
		}
		Node cur1 = head;
		Node cur2 = null;
		while (cur1 != null) { // 当cur != null 继续
			cur2 = cur1.left; // mostright是cur左孩子
			if (cur2 != null) { //有左孩子执行
				while (cur2.right != null && cur2.right != cur1) { // 跑的过程中，就是找左子树最右的节点
					cur2 = cur2.right;
				}
				// 从while出来后，mostright就是cur左子树上最右的节点
				if (cur2.right == null) { // 违反了while的第一部分，说明第一次来到cur 中了2a
					cur2.right = cur1;
					cur1 = cur1.left;
					continue;
				} else { // 因为后面条件违反（cur2.right != cur1）跳出的while，第二次来到cur
					cur2.right = null;
				}
			}
			System.out.print(cur1.value + " "); // 只要节点往右移动就打印 （中序只加这一句）
			cur1 = cur1.right; // cur右移
		}
		System.out.println();
	}

	public static void morrisPre(Node head) {
		// 先序
		if (head == null) {
			return;
		}
		Node cur1 = head;
		Node cur2 = null;
		while (cur1 != null) {
			cur2 = cur1.left;
			if (cur2 != null) {
				while (cur2.right != null && cur2.right != cur1) {
					cur2 = cur2.right;
				}
				if (cur2.right == null) {
					cur2.right = cur1;
					System.out.print(cur1.value + " "); // 能回到自己两次节点，第一次就打印
					cur1 = cur1.left;
					continue;
				} else {
					cur2.right = null;
				}
			} else { // 当前cur只能来到一次，打印行为
				System.out.print(cur1.value + " ");
			}
			cur1 = cur1.right;
		}
		System.out.println();
	}

	public static void morrisPos(Node head) {
		if (head == null) {
			return;
		}
		Node cur1 = head;
		Node cur2 = null;
		while (cur1 != null) {
			cur2 = cur1.left;
			if (cur2 != null) {
				while (cur2.right != null && cur2.right != cur1) {
					cur2 = cur2.right;
				}
				if (cur2.right == null) {
					cur2.right = cur1;
					cur1 = cur1.left;
					continue;
				} else {
					cur2.right = null;
					printEdge(cur1.left); // 逆序打印左子树右边届
				}
			}
			cur1 = cur1.right;
		}
		printEdge(head); // 整棵树的右边届打印一下
		System.out.println();
	}

	public static void printEdge(Node head) {
		Node tail = reverseEdge(head);
		Node cur = tail;
		while (cur != null) {
			System.out.print(cur.value + " ");
			cur = cur.right;
		}
		reverseEdge(tail);
	}

	public static Node reverseEdge(Node from) {
		Node pre = null;
		Node next = null;
		while (from != null) {
			next = from.right;
			from.right = pre;
			pre = from;
			from = next;
		}
		return pre;
	}

	// for test -- print tree
	public static void printTree(Node head) {
		System.out.println("Binary Tree:");
		printInOrder(head, 0, "H", 17);
		System.out.println();
	}

	public static void printInOrder(Node head, int height, String to, int len) {
		if (head == null) {
			return;
		}
		printInOrder(head.right, height + 1, "v", len);
		String val = to + head.value + to;
		int lenM = val.length();
		int lenL = (len - lenM) / 2;
		int lenR = len - lenM - lenL;
		val = getSpace(lenL) + val + getSpace(lenR);
		System.out.println(getSpace(height * len) + val);
		printInOrder(head.left, height + 1, "^", len);
	}

	public static String getSpace(int num) {
		String space = " ";
		StringBuffer buf = new StringBuffer("");
		for (int i = 0; i < num; i++) {
			buf.append(space);
		}
		return buf.toString();
	}

	public static void main(String[] args) {
		Node head = new Node(4);
		head.left = new Node(2);
		head.right = new Node(6);
		head.left.left = new Node(1);
		head.left.right = new Node(3);
		head.right.left = new Node(5);
		head.right.right = new Node(7);
		printTree(head);
		morrisIn(head);
		morrisPre(head);
		morrisPos(head);
		printTree(head);

	}

}
