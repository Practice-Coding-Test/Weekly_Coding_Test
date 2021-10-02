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
