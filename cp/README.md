- [Digit DP](#digit-dp)
- [Number of Sub-arrays with Sum = k](#number-of-sub-arrays-with-sum-equal-to-k)
- [Calculating pre-xors in a Tree (DSU application)](#calculating-prexors-in-a-tree-as-a-dsu-application)
- [Interesting Application of Binary Searching](#interesting-application-of-binary-searching)

# Digit DP

Notes: My Digit DP Implementation

Tags: CP 

```cpp
/*dp[pos][cnt][flag] -> dp form with states*/

int solve(int b)
{
    num.clear();
    while (b > 0)
        num.pb(b % 10), b /= 10;
    reverse(all(num));
    return call(0, 0, 0);
}

int call(int pos, int cnt, int flag)
{
    if (cnt > k) return 0;
    
        if (pos == num.size())
    {
        if (cnt == k) return 1;
        else return 0;
    }

    if (f[pos][cnt][flag] != -1) return f[pos][cnt][flag];
    f[pos][cnt][flag] = 0;

    int limit = 9;
    if (flag == 0)
        limit = num[pos];

    for (int i = 0; i <= limit; i++)
    {
        int next_flag = flag, next_cnt = cnt;

        if (i < limit) next_flag = 1;
        if (i == d) next_cnt++;

        f[pos][cnt][flag] += call(pos + 1, next_cnt, next_flag);
    }
    return f[pos][cnt][flag];
}

```

# Number of Sub-arrays with Sum equal to k

Notes: A solution

Tags: CP, Work

```cpp
int Sum(int arr[], int n, int sum = 1)
{
    unordered_map<int, int> prevSum;
    int res = 0;

    int curr_sum = 0;
    for (int i = 0; i < n; i++)
    {
        curr_sum += arr[i];

        if (curr_sum == sum) res++;

        if (prevSum.find(curr_sum - sum) != prevSum.end())
            res += (prevSum[curr_sum - sum]);

        prevSum[curr_sum]++;
    }

    return res;
}
```

# Calculating prexors in a Tree as a DSU application

Tags: CP

This is related to a problem I came across in OJ 4 (DSA) and the following is the solution:

```cpp
int n, m, k;
map<int, int> parent, val;
int net = 0, ans = INF;

int power(int x, int N)
{
    int y = 1;
    while (N > 0)
    {
        if (N & 1)
            y = (y * x) % MOD;
        N /= 2;
        x = (x * x) % MOD;
    }

    return y;
}

int Get(int i)
{
    if (!parent.count(i)) parent[i] = i, val[i] = 0;
    return parent[i];
}

int Find(int x)
{
    int p = Get(x);
    if (p == x) return x;

    int r = (parent[x] = Find(p));
    val[x] ^= val[p];
    return r;
}

void Union(int i, int j, int x)
{
    int a = Find(i), b = Find(j);
    x ^= val[i] ^ val[j];

    if (a != b)
    {
        parent[a] = b;
        val[a] = x;

        net--;

    } else
    {
        if (x == 0) return;
        else
            ans = 0;
    }
}

signed main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m >> k;
    net = n + m - 1;

    while (k--)
    {
        int i, j, x;
        cin >> i >> j >> x;
        j = 1005 + j;

        if (ans != 0)
            Union(i, j, x);
    }

    if (ans == 0)
        cout << 0 << endl;
    else
    {
        ans = power(2, 30);
        ans = power(ans, net);
        cout << ans << endl;
    }
    return 0;
}
```

# Interesting Application of Binary Searching

Notes: An interesting application of binary searching that can be applied to greedy graph algorithms like MST and Flows

Tags: CP

## What is done?

*In, normal binary search we search for first/suitable occurence of the correct answer. Here also we do something similar.*

## Problem

You are to form an MST such that the no. of edges in the MST that are connected to the index 1 is k which is given.

Simply put, 
        
$$Edges \in MST\ connected\ to\ 1\ =\ k$$

## Solution

We introduce the following idea - **to prioritize the edges connected to 1 we add a separate suitable**

**weight to the edges that have the node 1 in them** (during the formation of the MST).

Now we binary search over the suitable weight. 

- **Code**

    ```cpp
    int n, m, k;
    int net, connections;
    vi parent, ans;

    struct node
    {
        int u, v, w, weight, index;
    };

    vector<node> edge;

    bool cmp(node a, node b)
    {
        if (a.weight == b.weight)
            return a.u < b.u;
        else
            return a.weight < b.weight;
    }

    int Find(int a)
    {
        if (parent[a] == a)
            return a;
        return parent[a] = Find(parent[a]);
    }

    void Union(int mid)
    {
        net = 0, connections = 0;

        for (int i = 1; i <= n; i++)
            parent[i] = i;

        for (int i = 0; i < m; i++)
        {
            edge[i].weight = edge[i].w;

            if (edge[i].u == 1)
                edge[i].weight += mid;
        }
        sort(all(edge), cmp);

        for (int i = 0; i < m; i++)
        {
            if (net >= n)
                break;

            int a = Find(edge[i].u), b = Find(edge[i].v);
            int c = connections;

            if (a != b)
            {
                if (edge[i].u == 1)
                    c++;

                if (c <= k)
                {
                    ans[++net] = edge[i].index;
                    parent[a] = b;
                    connections = c;
                }
            }
        }
    }

    signed main()
    {
        cin >> n >> m >> k;
        parent.resize(n + 1), ans.resize(n + 1), edge.resize(m);

        vi bandwidth;
        bandwidth.pb(0);
        for (int i = 0; i < m; i++)
        {
            cin >> edge[i].u >> edge[i].v >> edge[i].w;
            edge[i].index = i + 1;

            bandwidth.pb(edge[i].w);

            if (edge[i].u > edge[i].v)
                swap(edge[i].u, edge[i].v);
        }

        int start = -MAX, end = MAX;
        while (start < end)
        {
            int mid = (start + end + 1) / 2;
            Union(mid);

            if (connections == k) start = mid;
            else end = mid - 1;
        }
        Union(start);

        if (net < n - 1 || connections < k)
            cout << -1 << endl;
        else
        {
            int sum = 0;
            for (int i = 1; i <= net; i++)
                sum += bandwidth[ans[i]];

            cout << sum << endl;
        }
        return 0;
    }    
    ```

<script async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.6/MathJax.js?config=TeX-AMS_CHTML"></script>
