class LinkedList {
	static Node head;

	static class Node {
		int data;
		Node next;

		Node(int d) {
			data = d;
			next = null;

		}
	}

	Node reverse(Node node) {
		Node prev = null;
		Node current = node;
		Node next = null;

		while(current != null) {
			next = current.next;
			current.next  = prev;
			prev = current;
			current = nex;
		}
	node = prev;
	return node;
	}
}