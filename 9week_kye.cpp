#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;


int cnt = 1;
vector<int>visited;
vector<int>net[101];
int dfs(int start, int check)//Ž�� ���� ���, ���ܽ��Ѿ��� ���
{
    visited[start] = 1;//�湮 üũ
    for (int i = 0; i < net[start].size(); i++)
    {
        if (!visited[net[start][i]] && net[start][i] != check)//�湮�� ���� �ʾҰ�, �� ��尡 v2, �� �ٸ� ����ž�� ���۳�尡 �ƴ϶��
        {
            cnt++;
            dfs(net[start][i], check);//�� ��带 �������� Ž�� ����
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
        net[u].push_back(v);//����� ���� ���� �ش�.
        net[v].push_back(u);
    }
    int v1, v2;
    int result;
    int v1_num, v2_num;
    int ans = 101;
    for (int i = 0; i < n - 1; i++)
    {
        v1 = wires[i][0];//�� ����ž ���� ���
        v2 = wires[i][1];//�� ����ž ���۳��
        visited.assign(n + 1, 0);//���� �ϳ� ���� ������ visited�� �ʱ�ȭ
        cnt = 1;//ī���� �ʱ�ȭ
        v1_num = dfs(v1, v2);//v1�� ���������� dfs�ǽ�-> ����� ��� ��带 ã�´�.�� v2 ����
        cnt = 1;
        v2_num = dfs(v2, v1);//v2�� ���������� dfs�ǽ�-> ����� ��� ��带 ã�´�.�� v1 ����
        result = abs(v1_num - v2_num);//���� ����
        ans = min(ans, result);//�ּڰ�

    }
    return ans;
}