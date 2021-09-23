#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

vector<int>graph[1001];
int job[1001] = { 0, };
int visited[1001] = { 0, };
int n, m, k;

int dfs(int worker)
{
	if (visited[worker])//이미 방문한 직원이면 리턴
		return 0;
	visited[worker] = 1;//방문 표시
	for (int i = 0; i < graph[worker].size(); i++)
	{
		int work = graph[worker][i];//worker가 가능한 일
		if (job[work] == 0 || dfs(job[work]))//아직 그 work에 할당된 직원이 없고,있더라도 다른 work으로 이동시킬 수 있으면
		{
			job[work] = worker;//work에 할당된 worker
			return 1;
		}
	}
	return 0;
}
int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cin >> n >> m >> k;
	for (int i = 1; i <= n; i++)
	{
		int num;
		cin >> num;
		for (int j = 0; j < num; j++)
		{
			int jobs;
			cin >> jobs;
			graph[i].push_back(jobs);//i번째 직원이 할 수 있는 jobs을 연결 시켜 준다.
		}
	}
	int cnt = 0;
	for (int i = 1; i <= n; i++)
	{
		memset(visited, 0, sizeof(visited));
		if (dfs(i))//i번째 직원이 할 수 있는 job이 있다면
			cnt++;
	}
	int rest = 0;
	int flag = 0;
	//모든 직원이 가능한 한개의 일에 할당되어 있다
	//더 가능한 직원을 찾기
	for (int i = 1; i <= n; i++)
	{
		while (rest < k)//한 직원에게 몰아서 일을 할당해도 되니 while로 loop 돌기
		{
			memset(visited, 0, sizeof(visited));
			if (dfs(i))
				rest++;
			else break;//더이상 i번째 직원이 할 수 있는 일이 없는데 k개에 도달하지 못했으니 다음 직원으로..
			if (rest == k)//더 할당 가능한 일의 갯수가 다 할당되었으면
			{
				flag = 1;
				break;
			}
		}
		if (flag == 1)
			break;
	}

	// 여기서 직원 순서대로 loop를 돌면 시간초과
	// 한명에게 몰아줘도 된다는 것이 포인트
	cout << cnt + rest;

}