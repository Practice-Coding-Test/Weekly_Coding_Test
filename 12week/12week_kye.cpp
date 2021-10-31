#include <iostream>
#include<algorithm>
#include<vector>

using namespace std;
bool visited[8];
int permutation(int cnt, int idx, vector<vector<int>>dungeons, int k)
{
    int answer = -1;
    if (cnt == dungeons.size())//존재하는 던전을 모두 방문했으면
    {
        return idx;
    }
    for (int i = 0; i < dungeons.size(); i++)
    {
        if (visited[i])//이미방문했으면 건너뛰기
            continue;
        int result;
        visited[i] = true;//방문 표시
        if (k >= dungeons[i][0])//최소필요보다 더 크면 즉, 방문가능한 던전이면
        {
            result = permutation(cnt + 1, idx + 1, dungeons, k - dungeons[i][1]);//재귀실시 이때, 방문한 던전갯수,idx+1할것
            if (result > answer)
                answer = result;
        }
        result = permutation(cnt + 1, idx, dungeons, k);//방문은 안했지만, 방문이 불가능한 던전이라면 던전갯수 추가하지 않고 재귀
        visited[i] = false;//순열을 위해 false
        if (result > answer)
            answer = result;
    }
    //방문이 불가능한 던전에서 재귀를 실시하지 않으면,
    //2번이 그런 던전이라면, 1 3 2로 방문하는 경우의 수는 체크하지만 1 3 만 방문하는 경우는 체크되지 않게 된다.
    return answer;
}
int solution(int k, vector<vector<int>> dungeons)
{
    int answer = -1;
    permutation(0, 0, dungeons, k);

    return answer;
}
