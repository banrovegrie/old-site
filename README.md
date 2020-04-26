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

Completed: Yes
Created: Apr 15, 2020 3:42 PM
Notes: My Digit DP Implementation
Property: Alapan Chaudhuri
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
    if (**cnt > k**) return 0;
    
		if (**pos == num.size()**)
    {
        if (**cnt == k**) return 1;
        else return 0;
    }

    if (f[pos][cnt][flag] != -1) return f[pos][cnt][flag];
    f[pos][cnt][flag] = 0;

    **int limit = 9;
    if (flag == 0)
        limit = num[pos];**

    for (int i = 0; i <= **limit**; i++)
    {
        **int next_flag = flag, next_cnt = cnt;

        if (i < limit) next_flag = 1;
        if (i == d) next_cnt++;

        f[pos][cnt][flag] += call(pos + 1, next_cnt, next_flag);**
    }
    return f[pos][cnt][flag];
}

```
