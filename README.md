## Alapan Chaudhuri, student of Mathematics and Computer Science

### I am currently a student at the International Institute of Information Technology, Hyderabad - pursuing integrated Masters in Computational Sciences (by Research) with B.Tech in Computer Science and Engineering.

### This wiki is my attempt to dump all my Notes in one place which is not only easily available but also easily searchable.

How to connect to me?

- Google Account : [ac.ala.arya@gmail.com](mailto:ac.ala.arya@gmail.com)
- Academic E-mail : [alapan.chaudhuri@research.iiit.ac.in](mailto:alapan.chaudhuri@research.iiit.ac.in)
- GitHub : [banrovegrie](https://github.com/banrovegrie)

***Aliases**:*
1. *Arjo, Arya, Dada*
2. *banrovegrie (Dāritys Morgho ban Rōvēgrie), alathedarkwiz (cringey yes i know)*

## My Notes and Writings

- [Mathematics and Sciences](https://www.notion.so/3314082755ce41ebb0b5fd26f0e9661b)

- [Arts and Letters](https://www.notion.so/09db23e4229a4be6a4c46f5374912b4b)

- [banrovegrie/Notebooks](http://github.com/banrovegrie/Notebooks)


# Digit DP

Created: Apr 15, 2020 3:42 PM

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

# Introduction to Internet of Things

Created: Apr 24, 2020 9:55 PM

Notes: This is a summary of the IoT course taught in college

Tags: IoT, Study

## Intro Part

- history of iot
- what is iot
- information flow in iot (sensors, local processing, local storage, network, internet, cloud processing, cloud storage)
- IoT buzz words: low cost chips, faster comm tech, fog/edge computing, advances in AI and BigData, flex of IPv6
- **Data→info→knowledge→wisdom**
- current m2m: connectivity, content
- evolution in iot: cloud, context, collab, cognition
- Importance of IoT: gathers useful **data**, focuses on **automation and control**, **monitoring**, increases **efficiency**, improves quality of life
- Challenges: too much data, privacy/security, complexity, connectivity
- sensor
- transducers
- sensor features
- sensor resolution
- resolution *\prop* accuracy of precision
- resolution *\prop* accuracy of sensor
- Sensor Classes: o/p (analog and digital), data type (scalar and vector), intermediate stages (direct and indirect), power req (active and passive), reference (absolute and relative), stimulus (contact and on contact)
- Sensor Characteristics: Range and Span, Accuracy, Resolution, Precision, Errors (Random (breadth of random ness) and Systematic (diff from centre))
- Sensitivity = dY/dX
- Linearity
- Hysteresis: difference in output for the same input reached through different trajectories
- DHT11 works on the basis of thermistor

## Processing

- Microcontroller: compact IC
- difference from conventional less expensive and less power
- Elements of a Microcontroller: Memory, Processor, I/O
- Processor Architecture: von Neumann Architecture, Harvard Architecture
- ADC, DAC, System Bus
- Microcontroller Features: Bits, RAM, Flash, GPIO, Connectivity, Power Consumption
- Examples: Particle.io, ESP8266, Arduino, Raspberry Pi

## Architecture

- Perception Layer: devices and sensors
- Network Layer: Secure Transmission
- Middleware Layer: Database, Computing
- Application Layer: Smart Applications
- Business Layer: Business Models, Graphs, Charts, System Management
- IoT Protocols: reliable byte streams **TCP**
- Publisher/Subscriber Approach: MQTT, AMQP, XMPP (Broker serves as a third component)
- MQTT: Message Queuing Telemetry Transport
- MQTT topics are structured in an hierarchical order as with modern computer file systems e.g., myhome/ground-floor/living-room/temperature, and Subscriptions may have wildcards as well like + for matches at a given tree level and # matches with a whole subtree
- messages published with a QoS/Quality of service level
- level of service: QoS 0<1<2
- 0: PUBLISH
- 1: PUBLISH, PUBACK
- 2: PUBLISH, PUBREC, PUBREL, PUBCOM

## Protocols

- DDS: Data Distribution Service
- Middleware protocol
- API; OS and Architecture indifferent
- Data-Centric  Publish Subscribe
- Global Data Space Abstraction
- minimal local storage usage
- autonomous asynchronous reading and writing
- spatial and temporal decoupling
- Dynamic Discovery
- isolates apps from network topology and connectivity details
- enables plug and play
- decentralised data space
- topic <name, type, qos> define/rep data streams in DDS
- information scopes and domains
- volatile, transient, durable
- best effort, last n-values, reliable
- Stream Reliability: Best Effort, Last n-values, Reliable
- MQTT and DDS: centralised vs decentralised, DDS provides more QoS aspects than MQTT
- Complexity: MQTT is simpler up front but assumes future, while DDS requires up front investment but minimizes future complexity

# Number of Sub-arrays with Sum = k

Created: Apr 09, 2020 11:00 PM

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

# Calculating pre-xors in a Tree (DSU application)

Created: Apr 09, 2020 10:54 PM

Tags: CP

This is related to a problem I came across in OJ 4 (DSA) and the following is the solution:

```cpp
*int n, m, k;
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
}*

**int Find(int x)
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
}**

*signed main()
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
}*
```

# Interesting Application of Binary Searching

Created: Apr 02, 2020 5:19 PM

Notes: An interesting application of binary searching that can be applied to greedy graph algorithms like MST and Flows

Tags: CP

## What is done?

*In, normal binary search we search for first/suitable occurence of the correct answer. Here also we do something similar.*

## Problem

You are to form an MST such that the no. of edges in the MST that are connected to the index 1 is k which is given.

$$Edges \in MST\ connected\ to\ 1\ =\ k$$

## Solution

We introduce the following idea - **to prioritize the edges connected to 1 we add a separate suitable**

**weight to the edges that have the node 1 in them** (during the formation of the MST).

Now we binary search over the suitable weight. 

- **Code**

    ```cpp
    int =n, m, k;
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

- **Chat that might clear doubts**

    [Screenshot 2020-04-03 at 1.26.08 AM.png](Interesting%20Application%20of%20Binary%20Searching/Screenshot_2020-04-03_at_1.26.08_AM.png)

    [Screenshot 2020-04-03 at 1.26.20 AM.png](Interesting%20Application%20of%20Binary%20Searching/Screenshot_2020-04-03_at_1.26.20_AM.png)

    [Screenshot 2020-04-03 at 1.26.32 AM.png](Interesting%20Application%20of%20Binary%20Searching/Screenshot_2020-04-03_at_1.26.32_AM.png)

    [Screenshot 2020-04-03 at 1.26.52 AM.png](Interesting%20Application%20of%20Binary%20Searching/Screenshot_2020-04-03_at_1.26.52_AM.png)

    [Screenshot 2020-04-03 at 1.27.03 AM.png](Interesting%20Application%20of%20Binary%20Searching/Screenshot_2020-04-03_at_1.27.03_AM.png)

![Interesting%20Application%20of%20Binary%20Searching/Screenshot_(1).png](Interesting%20Application%20of%20Binary%20Searching/Screenshot_(1).png)
