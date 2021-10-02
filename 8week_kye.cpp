
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
#include<iostream>
#include<algorithm>
#include <string>
#include <vector>

using namespace std;


2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
#include<iostream>
#include<algorithm>
#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int answer,max_num,min_num;
    int max_max = 0;
    int min_max = 0;
    for (int i = 0; i < sizes.size(); i++)
    {
        if (sizes[i][0] > sizes[i][1])
        {
            max_num = sizes[i][0];
            min_num = sizes[i][1];
        }
        else
        {
            max_num = sizes[i][1];
            min_num = sizes[i][0];
        }
        if (max_num > max_max)
            max_max = max_num;
        if (min_num > min_max)
            min_max = min_num;
    }
    answer = min_max * max_max;
    return answer;
}
