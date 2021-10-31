#include <iostream>
#include<algorithm>
#include<vector>

using namespace std;
bool visited[8];
int permutation(int cnt, int idx, vector<vector<int>>dungeons, int k)
{
    int answer = -1;
    if (cnt == dungeons.size())//�����ϴ� ������ ��� �湮������
    {
        return idx;
    }
    for (int i = 0; i < dungeons.size(); i++)
    {
        if (visited[i])//�̹̹湮������ �ǳʶٱ�
            continue;
        int result;
        visited[i] = true;//�湮 ǥ��
        if (k >= dungeons[i][0])//�ּ��ʿ亸�� �� ũ�� ��, �湮������ �����̸�
        {
            result = permutation(cnt + 1, idx + 1, dungeons, k - dungeons[i][1]);//��ͽǽ� �̶�, �湮�� ��������,idx+1�Ұ�
            if (result > answer)
                answer = result;
        }
        result = permutation(cnt + 1, idx, dungeons, k);//�湮�� ��������, �湮�� �Ұ����� �����̶�� �������� �߰����� �ʰ� ���
        visited[i] = false;//������ ���� false
        if (result > answer)
            answer = result;
    }
    //�湮�� �Ұ����� �������� ��͸� �ǽ����� ������,
    //2���� �׷� �����̶��, 1 3 2�� �湮�ϴ� ����� ���� üũ������ 1 3 �� �湮�ϴ� ���� üũ���� �ʰ� �ȴ�.
    return answer;
}
int solution(int k, vector<vector<int>> dungeons)
{
    int answer = -1;
    permutation(0, 0, dungeons, k);

    return answer;
}