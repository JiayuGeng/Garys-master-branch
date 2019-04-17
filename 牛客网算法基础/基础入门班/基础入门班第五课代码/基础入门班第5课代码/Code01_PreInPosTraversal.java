package class05;

import java.util.Stack;

public class Code01_PreInPosTraversal {

	public static class Node {
		public int value;
		public Node left;
		public Node right;

		public Node(int data) {
			this.value = data;
		}
	}

	public static void preOrderRecur(Node head) {
		if (head == null) {
			return;
		}
		// 第一次到达node
		System.out.print(head.value + " ");
		preOrderRecur(head.left);
		// 第二次到达node
		preOrderRecur(head.right);
		// 第三次到达node
	}

	public static void inOrderRecur(Node head) {
		if (head == null) {
			return;
		}
		inOrderRecur(head.left);
		System.out.print(head.value + " ");
		inOrderRecur(head.right);
	}

	public static void posOrderRecur(Node head) {
		if (head == null) {
			return;
		}
		posOrderRecur(head.left);
		posOrderRecur(head.right);
		System.out.print(head.value + " ");
	}

	public static void preOrderUnRecur(Node head) {
		System.out.print("pre-order: ");
		if (head != null) {
			Stack<Node> stack = new Stack<Node>(); // 准备个栈
			stack.add(head); // 第一步，头节点进栈
			while (!stack.isEmpty()) {
				head = stack.pop(); // 弹出
				System.out.print(head.value + " "); // 打印当前节点
				if (head.right != null) { // 先进右子树
					stack.push(head.right);
				}
				if (head.left != null) { // 再进左子树
					stack.push(head.left);
				}
			}
		}
		System.out.println();
	}
	// 中序遍历
	public static void inOrderUnRecur(Node head) {
		System.out.print("in-order: ");
		if (head != null) {
			Stack<Node> stack = new Stack<Node>();
			while (!stack.isEmpty() || head != null) { // 还有左边界的阶段，整条左边界进栈
				if (head != null) {
					stack.push(head);
					head = head.left;
				} else {
					head = stack.pop(); // 从栈弹出一个节点并打印，head右移
					System.out.print(head.value + " ");
					head = head.right;
				}
			}
		}
		System.out.println();
	}

	// 后续遍历，准备2个栈
	public static void posOrderUnRecur1(Node head) {
		System.out.print("pos-order: ");
		if (head != null) {
			Stack<Node> s1 = new Stack<Node>(); // 老栈
			Stack<Node> s2 = new Stack<Node>(); // 新栈，只做一件事：收集打印的结果
			s1.push(head);
			while (!s1.isEmpty()) { // s1弹出的顺序时中右左，s2记录的顺序就是左右中
				head = s1.pop(); // head弹出时放入s2里
				s2.push(head);
				if (head.left != null) { // 先进左子树
					s1.push(head.left);
				}
				if (head.right != null) { // 再进右子树
					s1.push(head.right);
				}
			}
			while (!s2.isEmpty()) {
				System.out.print(s2.pop().value + " ");
			}
		}
		System.out.println();
	}

	public static void posOrderUnRecur2(Node h) {
		System.out.print("pos-order: ");
		if (h != null) {
			Stack<Node> stack = new Stack<Node>();
			stack.push(h);
			Node c = null;
			while (!stack.isEmpty()) {
				c = stack.peek();
				if (c.left != null && h != c.left && h != c.right) {
					stack.push(c.left);
				} else if (c.right != null && h != c.right) {
					stack.push(c.right);
				} else {
					System.out.print(stack.pop().value + " ");
					h = c;
				}
			}
		}
		System.out.println();
	}

	public static void main(String[] args) {
		Node head = new Node(5);
		head.left = new Node(3);
		head.right = new Node(8);
		head.left.left = new Node(2);
		head.left.right = new Node(4);
		head.left.left.left = new Node(1);
		head.right.left = new Node(7);
		head.right.left.left = new Node(6);
		head.right.right = new Node(10);
		head.right.right.left = new Node(9);
		head.right.right.right = new Node(11);

		// recursive
		System.out.println("==============recursive==============");
		System.out.print("pre-order: ");
		preOrderRecur(head);
		System.out.println();
		System.out.print("in-order: ");
		inOrderRecur(head);
		System.out.println();
		System.out.print("pos-order: ");
		posOrderRecur(head);
		System.out.println();

		// unrecursive
		System.out.println("============unrecursive=============");
		preOrderUnRecur(head);
		inOrderUnRecur(head);
		posOrderUnRecur1(head);
		posOrderUnRecur2(head);

	}

}
