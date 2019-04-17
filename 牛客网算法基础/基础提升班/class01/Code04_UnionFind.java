package class01;

import java.util.HashMap;
import java.util.List;
import java.util.Stack;

public class Code04_UnionFind {

	public static class Element<V> {
		public V value;

		public Element(V value) {
			this.value = value;
		}

	}

	public static class UnionFindSet<V> {
		public HashMap<V, Element<V>> elementMap; // 一个值是否有注册
		public HashMap<Element<V>, Element<V>> fatherMap;
		public HashMap<Element<V>, Integer> rankMap; // sizeMap, 记录代表节点的记录，记录这个节点多大

		public UnionFindSet(List<V> list) {
			elementMap = new HashMap<>();
			fatherMap = new HashMap<>();
			rankMap = new HashMap<>();
			for (V value : list) {
				Element<V> element = new Element<V>(value);
				elementMap.put(value, element);
				fatherMap.put(element, element);
				rankMap.put(element, 1);
			}
		}

		private Element<V> findHead(Element<V> element) {
			Stack<Element<V>> path = new Stack<>();
			while (element != fatherMap.get(element)) { // element ！=他的父亲。就一直往上跑
				path.push(element);
				element = fatherMap.get(element);
			}
			while (!path.isEmpty()) {
				fatherMap.put(path.pop(), element);
			}
			return element;
		}

		public boolean isSameSet(V a, V b) {
			if (elementMap.containsKey(a) && elementMap.containsKey(b)) {
				// a的集合一直往上找=b集合一直往上
				return findHead(elementMap.get(a)) == findHead(elementMap.get(b));
			}
			return false;
		}

		public void union(V a, V b) {
			if (elementMap.containsKey(a) && elementMap.containsKey(b)) {
				Element<V> aF = findHead(elementMap.get(a));
				Element<V> bF = findHead(elementMap.get(b));
				if (aF != bF) {
					Element<V> big = rankMap.get(aF) >= rankMap.get(bF) ? aF : bF;//找到哪一个集合更大，就小挂大
					Element<V> small = big == aF ? bF : aF;
					fatherMap.put(small, big);//小元素的代表节点他的父亲设置为大元素
					rankMap.put(big, rankMap.get(aF) + rankMap.get(bF)); // 大集合的size必须是两个集合相加
					rankMap.remove(small);//small不会做为代表集合节点，所以删掉记录
				}
			}
		}

	}

}
