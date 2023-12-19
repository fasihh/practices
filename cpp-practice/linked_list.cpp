#include <iostream>

using namespace std;

// class Node {
// public:
// 	string val;
// 	Node *next;

// 	Node(string inp) : val(inp), next(nullptr) {}
// };

class List {
private:
	typedef struct Node {
		string val;
		struct Node *next;
	} Node;

	Node* start;
	int len;
public:
	List() : start(nullptr), len(0) {}

	void insert(string inp) {
		Node *node = new Node();
		node->val = inp;
		len++;

		if (!start) {
			start = node;
			return;
		}

		Node *temp = start;
		while (temp->next)
			temp = temp->next;

		temp->next = node;
	}

	bool remove()
	{
		if (!start) return false;

		Node *current = start, *previous = nullptr;
		while (current->next) {
			previous = current;
			current = current->next;
		}

		delete current;
		if (previous)
			previous->next = nullptr;
		else
			start = nullptr;

		len--;
		return true;
	}

	void print() {
		Node *temp = start;
		while (temp) {
			cout << temp->val  << " -> ";
			temp = temp->next;
		}

		cout << "(null)" << endl;
	}

	string get(int n)
	{
		Node *temp = start;
		for (int i = 0; i < n && i < len; i++) 
			temp = temp->next;
		return n >= len ? "(null)" : temp->val;
	}

	int length() {
		return this->len;
	}
};

int main()
{
	List list = List();

	List *list_list = new List();

	list.insert("test1");

	list.print();

	for (int i = 0; i < list.length(); i++) {
		cout << list.get(i) << endl;
	}

	return 0;
}
