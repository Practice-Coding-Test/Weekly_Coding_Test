#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;


int cnt = 1;
vector<int>visited;
vector<int>net[101];
int dfs(int start, int check)//탐색 시작 노드, 제외시켜야할 노드
{
    visited[start] = 1;//방문 체크
    for (int i = 0; i < net[start].size(); i++)
    {
        if (!visited[net[start][i]] && net[start][i] != check)//방문을 하지 않았고, 그 노드가 v2, 즉 다른 송전탑의 시작노드가 아니라면
        {
            cnt++;
            dfs(net[start][i], check);//그 노드를 기준으로 탐색 시작
        }
    }
    return cnt;
}
int solution(int n, vector<vector<int>>wires)
{
    int u, v;
    for (int i = 0; i < n - 1; i++)
    {
        u = wires[i][0];
        v = wires[i][1];
        net[u].push_back(v);//양방향 연결 시켜 준다.
        net[v].push_back(u);
    }
    int v1, v2;
    int result;
    int v1_num, v2_num;
    int ans = 101;
    for (int i = 0; i < n - 1; i++)
    {
        v1 = wires[i][0];//각 송전탑 시작 노드
        v2 = wires[i][1];//각 송전탑 시작노드
        visited.assign(n + 1, 0);//간선 하나 끊을 때마다 visited는 초기화
        cnt = 1;//카운팅 초기화
        v1_num = dfs(v1, v2);//v1을 시작점으로 dfs실시-> 연결된 모든 노드를 찾는다.단 v2 제외
        cnt = 1;
        v2_num = dfs(v2, v1);//v2을 시작점으로 dfs실시-> 연결된 모든 노드를 찾는다.단 v1 제외
        result = abs(v1_num - v2_num);//값의 차이
        ans = min(ans, result);//최솟값

    }
    return ans;
}