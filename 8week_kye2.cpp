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
	if (visited[worker])//�̹� �湮�� �����̸� ����
		return 0;
	visited[worker] = 1;//�湮 ǥ��
	for (int i = 0; i < graph[worker].size(); i++)
	{
		int work = graph[worker][i];//worker�� ������ ��
		if (job[work] == 0 || dfs(job[work]))//���� �� work�� �Ҵ�� ������ ����,�ִ��� �ٸ� work���� �̵���ų �� ������
		{
			job[work] = worker;//work�� �Ҵ�� worker
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
			graph[i].push_back(jobs);//i��° ������ �� �� �ִ� jobs�� ���� ���� �ش�.
		}
	}
	int cnt = 0;
	for (int i = 1; i <= n; i++)
	{
		memset(visited, 0, sizeof(visited));
		if (dfs(i))//i��° ������ �� �� �ִ� job�� �ִٸ�
			cnt++;
	}
	int rest = 0;
	int flag = 0;
	//��� ������ ������ �Ѱ��� �Ͽ� �Ҵ�Ǿ� �ִ�
	//�� ������ ������ ã��
	for (int i = 1; i <= n; i++)
	{
		while (rest < k)//�� �������� ���Ƽ� ���� �Ҵ��ص� �Ǵ� while�� loop ����
		{
			memset(visited, 0, sizeof(visited));
			if (dfs(i))
				rest++;
			else break;//���̻� i��° ������ �� �� �ִ� ���� ���µ� k���� �������� �������� ���� ��������..
			if (rest == k)//�� �Ҵ� ������ ���� ������ �� �Ҵ�Ǿ�����
			{
				flag = 1;
				break;
			}
		}
		if (flag == 1)
			break;
	}

	// ���⼭ ���� ������� loop�� ���� �ð��ʰ�
	// �Ѹ��� �����൵ �ȴٴ� ���� ����Ʈ
	cout << cnt + rest;

}