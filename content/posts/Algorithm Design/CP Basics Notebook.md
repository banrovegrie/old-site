# Data Structures
---
## My Header File

A header files is like an additional abstraction that helps you code cleaner and faster.

```cpp
#include <bits/stdc++.h>
//#include <ext/pb_ds/assoc_container.hpp>		// uncomment before submission
//#include <ext/pb_ds/tree_policy.hpp>			// uncomment before submission
//using namespace __gnu_pbds;					// uncomment before submission
using namespace std;
//<---------------------------------------------------Template----------------------------------------------------------->
#define int long long
#define ll long long
#define ld long double
const int INF = 1e18 + 7;
const int MAX = 1e5 + 7;
const int MOD = 1e9 + 7;
typedef pair<ll, ll> ii;
typedef vector<ll> vi;                  // Vector of long long
typedef vector<vi> vvi;                 // Vector of vi
typedef vector<ii> vii;                 // Vector of pairs
typedef vector<vii> vvii;               // Vector of Vector of pairs
typedef vector<bool> vb;                // Vector of bool
#define pq priority_queue               // Max heap (To convert to min heap, use negative sign before every value)
#define ff first                        // For pairs
#define ss second                       // For pairs
#define pb push_back                    // Push back to vector
#define mp make_pair                    // Makes pairs to be stored as pair
#define endl "\n"                       // Changes endl to \n
#define all(c) (c).begin(), (c).end()   // Mainly used by me in sorting
#define range(c, r) (c).begin(), (c).begin() + (r)                // Mainly used in sorting
#define present(c, x) ((c).find(x) != (c).end())                  // for sets, maps, multi-maps
#define cpresent(c, x) (find(all(c),x) != (c).end())              // for vectors
#define testcases(T) int (T); cin>>(T); while((T)--)              // inputing testcases
#define run(x, c) for((x)=(c).begin(); (x)!=(c).end(); (x)++)     // Mainly used by me for range based loops
// ordered_set adds two new functions to set - (set).find_by_order([kth element based on zero indexing]) and order_of_key()
// order_of_key returns number of elements less that parameter. If element exists, that order is its index
#define ordered_set tree<ll, null_type, less<ll>, rb_tree_tag, tree_order_statistics_node_update>
//<----------------------------------------------------------------------------------------------------------------------->
```


## Structs vs Classes

| Classes | Structs |
| --- | --- |
| Members of a class are private by default. | Members of a structure are public by default.  |
| Memory allocation happens on the heap. | Memory allocation happens on a stack. |
| It is a reference type data type. | It is a value type data type. |
| It is declared using the class keyword. | It is declared using the struct keyword. |

## Namespaces

Namespaces are basically to allow overloading on steroids. Using namespace, you can define the context in which names are defined. In essence, a namespace defines a scope.

```cpp
// first name space
namespace first_space {
   void func() {
      cout << "Inside first_space" << endl;
   }
}

// second name space
namespace second_space {
   void func() {
      cout << "Inside second_space" << endl;
   }
}
```

## Templates

Templates: generalization of functionality based on generalizing type-setting.

- Stuff done in compile time and each instance of a template contains its own static variable!
- Templates are expanded at compiler time. This is like macros. The difference is, the compiler does type checking before template expansion. The idea is simple, source code contains only function/class, but compiled code may contain multiple copies of same function/class.

```cpp
template<typename T, int N>
class Meow {
		// stuff to do
};

template<class T>
class Bhow {
		// stuff to do
};
```

## Linked List

Any linked-list type data structure (with explicit pointers and structures) can be represented using vectors in higher dimensions.

Most data structures can be manipulated to look and behave like a grpah. Thus, they can be implemented using methods like adjacency lists.

```cpp
template<typename T>
struct node
{
	T data;
	struct node* next;
	struct node* prev;
};

template<typename T>
class LinkedList
{
	public:
	node<T> *head, *tail;
	
	// Constructor
	LinkedList()
	{
		head = NULL;
		tail = NULL;
	}

	// Print
	void display(node<T> *head)
	{
		if (head == NULL)
		{
			cout << endl;
		}
		else
		{
			cout << head->data << " ";
			display(head->next);
		}
	}

	// Push Back
	void push_back(T n)
	{
		node<T> *temp = new node<T>;
		temp->data = n;
		temp->next = NULL;
		temp->prev = NULL;

		if (head == NULL)
		{
			head = temp;
			tail = temp;
		}
		else
		{
			tail->next = temp;
			temp->prev = tail;
			tail = tail->next;
		}
	}

	// Push Front
	void push_front(T n)
	{
		node<T> *temp = new node<T>;
		temp->data = n;
		temp->next = NULL;
		temp->prev = NULL;

		if (head == NULL)
		{
			head = temp;
			tail = temp;        
		}
		else
		{
			head->prev = temp;
			temp->next = head;
			head = head->prev;
		}
	}

	// Pop Front
	void pop_front()
	{
		if (head == NULL)
		{
			cout << "Empty list\n";
		}
		else
		{
			head = head->next;
			node<T> *temp = head->prev;
			delete temp;
		}
	}

	// Pop Back
	void pop_back()
	{
		if (head == NULL)
		{
			cout << "Empty list\n";
		}
		else
		{
			tail = tail->prev;
			node<T> *temp = tail->next;
			delete temp;
		}
	}
};
```


## Stack, Queue and Deque

Stacks, queues and deques are important data structures. However, you can almot always implement them using vectors or arrays (similar as in the case of linkedlists).

- Find the smallest element of the stack in $O(1)$

```cpp
// Stack is re-defined as stack<pair<int, int>> st;
// Add Element
int new_min = new_elem;
if (!st.empty())
		new_min = min(new_elem, st.top().second);
st.push({new_elem, new_min});

// Delete
int removed_element = st.top().first;
st.pop();

// Find the minimum
int minimum = st.top().second;
```

- Finding the maximum for all subarrays of fixed length.

```cpp
std::deque<int> Q(k);
int i = 0;
for (; i < k; i++)
{
		while(!Q.empty() and arr[i] >= arr[Q.back()])
				Q.pop_back();
}

for (; i < n; i++) 
{
	cout << arr[Q.front()] << " ";
	while (!Q.empty() && Q.front() <= i - k)
		Q.pop_front();
	while ((!Q.empty()) && arr[i] >= arr[Q.back()])
		Q.pop_back();
	Q.push_back(i);
}
cout << arr[Q.front()];
```

- Deque in python

```python
from collections import deque
de = deque()
de.append(2)
de.appendleft(3)
de.pop()
de.popleft()
de.extendleft([7,8,9])
de.reverse()
de.extend([4,5,6])
de.rotate(-3)
print(de)
```


## Set and Map structures

- set, unordered_set, multi_set
- map, unordered_map
- ordered_set

Apparently, the tree supports the same operations as the `set` (at least I haven't any problems with them before), but also there are two new features — it is `find_by_order()` and `order_of_key()`.

The first returns an iterator to the k-th largest element (counting from zero), the second — the number of items in a set that are strictly smaller than our item.

```cpp
typedef tree<
int,
null_type,
// If you use greater<int>, purpose is reversed.
less<int>,
rb_tree_tag,
tree_order_statistics_node_update>
ordered_set;
```

## Basic Tree Structures

- Binary Tree

- Binary Search Tree:
  The BST has an important property: every node’s value is strictly greater than the value of its left child and strictly lower than the value of its right child. It doesn’t allow duplicates.
  
- Heap (types: binary heap, fibonacci heap):
  BST is an ordered data structure, however, the Heap is not. In computer memory, the heap is usually represented as an array of numbers. The main rule of the Max-Heap is that the subtree under each node contains values less or equal than its root node. Also, the Heap allows duplicates.  

## Hash Table with Chaining

Hash Table, also known as hash map or dictionary, is a data structure that implements a set abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found. During lookup, the key is hashed and the resulting hash indicates where the corresponding value is stored.

```python
class HashTable:  
	def __init__(self):
		self.MAX = 100
		self.arr = [None for i in range(self.MAX)]
		
	def get_hash(self, key):
		hash = 0
		for char in key:
			hash += ord(char)
		return hash % self.MAX
	
	def __getitem__(self, index):
		h = self.get_hash(index)
		return self.arr[h]
	
	def __setitem__(self, key, val):
		h = self.get_hash(key)
		self.arr[h] = val    
		
	def __delitem__(self, key):
		h = self.get_hash(key)
		self.arr[h] = None

t = HashTable()
t["march 6"] = 310
t["march 7"] = 420
print(t["march 6"])
del t["march 6"]
```

Now, chaining can be further implemented to deal with collisions.

```python
class HashTable:  
	def __init__(self):
		self.MAX = 10
		self.arr = [[] for i in range(self.MAX)]
		
	def get_hash(self, key):
		hash = 0
		for char in key:
			hash += ord(char)
		return hash % self.MAX
	
	def __getitem__(self, key):
		arr_index = self.get_hash(key)
		for kv in self.arr[arr_index]:
			if kv[0] == key:
				return kv[1]
			
	def __setitem__(self, key, val):
		h = self.get_hash(key)
		found = False
		for idx, element in enumerate(self.arr[h]):
			if len(element)==2 and element[0] == key:
				self.arr[h][idx] = (key,val)
				found = True
		if not found:
			self.arr[h].append((key,val))
		
	def __delitem__(self, key):
		arr_index = self.get_hash(key)
		for index, kv in enumerate(self.arr[arr_index]):
			if kv[0] == key:
				print("del",index)
				del self.arr[arr_index][index]
```

## Disjoint Set Union

```cpp
void make_set(int v) {
    parent[v] = v;
		size[v] = 1;
}

// Always use Path Compression.
int find_set(int v) {
    if (v == parent[v])
        return v;
    return parent[v] = find_set(parent[v]);
}

// Union by Size.
void union_sets(int a, int b) {
    a = find_set(a);
    b = find_set(b);
    if (a != b) {
        if (size[a] < size[b])
            swap(a, b);
        parent[b] = a;
        size[a] += size[b];
    }
}
```

# Dynamic Programming
---
## Approaching DP Problems

- Think with modularity (top-down or bottom up as it helps)
- Remember you need to encode all the information you have into the DP. This will help you deicde what the states of the DP should be. The answer always needs to be the global optimum, so you need to figure that out too.
- Make sure you update the DP, only when required You update the DP only when you have a “decision” to make.
- While dealing with bitwise operations, try to imagine of them in terms of Venn Diagrams.

## Knapsack

![Untitled|center|600](Algorithm%20Design/images/CP%20Basics%20Notebook%20bf3fabb7717347eab1c382d85f52b2a7/Untitled.png)

![Untitled|center|600](Algorithm%20Design/images/CP%20Basics%20Notebook%20bf3fabb7717347eab1c382d85f52b2a7/Untitled%201.png)

## Bitmasking

![Untitled|center|600](Algorithm%20Design/images/CP%20Basics%20Notebook%20bf3fabb7717347eab1c382d85f52b2a7/Untitled%202.png)

- Optimal selection

```cpp
for (int x = 0; x < k; x++) {
		total[1<<x][0] = price[x][0];
}
// Then, the recurrence translates into the following code:

for (int d = 1; d < n; d++) {
		for (int s = 0; s < (1<<k); s++) {
				total[s][d] = total[s][d-1];
				for (int x = 0; x < k; x++) {
						if (s&(1<<x))
								total[s][d] = min(total[s][d],
								total[s^(1<<x)][d-1]+price[x][d]);
				}
		}
}
```

- From permutations to subsets

```cpp
pair<int,int> best[1<<N];
best[0] = {1,0};

// stuff ...

for (int s = 1; s < (1<<n); s++) {
		// initial value: n+1 rides are needed
		best[s] = {n+1,0};
		for (int p = 0; p < n; p++) {
				if (s&(1<<p)) {
						auto option = best[s^(1<<p)];
						if (option.second+weight[p] <= x) {
								// add p to an existing ride
								option.second += weight[p];
						} else {
								// reserve a new ride for p
								option.first++;
								option.second = weight[p];
						}
						best[s] = min(best[s], option);
				}
		}
}
```

## Sum over Subsets

```cpp
for(int i = 0; i<(1<<N); i++)
		F[i] = A[i];

for(int i = 0;i < N; i++) 
		for(int mask = 0; mask < (1<<N); mask++)
				if(mask & (1<<i))
						F[mask] += F[mask^(1<<i)];
```

# Graphs
---
## BFS and DFS

```cpp
// BFS is written as follows.

q.push(s);
used[s] = true, p[s] = -1;
while (!q.empty()) {
    int v = q.front();
    q.pop();
    for (int u : adj[v]) {
        if (!used[u]) {
            used[u] = true;
            q.push(u);
            d[u] = d[v] + 1;
            p[u] = v;
        }
    }
}
```

```cpp
// DFS is written as follows.

vector<vector<int>> adj;
int n;

vector<bool> visited;

void dfs(int v) {
    visited[v] = true;
    for (int u : adj[v])
        if (!visited[u])
            dfs(u);
}
```

Connected components: Just keep doing rounds of DFS.

## Shortest Path: Floyd Warshal

```cpp
for (int k = 0; k < n; ++k)
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j)
			d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
```