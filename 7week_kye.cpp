#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
using namespace std;

vector<int> solution(vector<int> enter, vector<int> leave) {
    vector<int> answer(enter.size(), 0);
    set<int>room;//�ߺ����Ÿ� ���� set ���
    vector<vector<int>>visited(enter.size() + 1, vector<int>(enter.size() + 1, 0));//2���� ���� �����, �湮 Ȯ�ο�
    int inidx = 0;
    int outidx = 0;
    while (outidx < leave.size())//��� ������ �������� ������ ����. �� ���� ������
    {
        //room�� ��� ������ ����� ���°��
        while (room.find(leave[outidx]) == room.end())
        {
            answer[enter[inidx] - 1] += room.size(); // ���� �Խ��ϸ� ���� �� �ִ� ����� ��
            for (int i : room)//room�� �ִ� ����� ���� ǥ��
            {
                answer[i - 1]++;
            }
            room.insert(enter[inidx]);//�Խ� ������ �ִ� ��� ��������
            inidx++;
        }
        //��Ǽ����� ����� ������ while�� �����.
        //room�� ��� ������ ����� �ִ� ���
        while ((outidx < leave.size()) && (room.find(leave[outidx]) != room.end()))
            // outidx�� ��������ϴ� ���� vector out of range �߻�
        {
            room.erase(leave[outidx]);//�濡�� ����
            outidx++;
        }
    }
    return answer;

}
int main()
{
    vector<int> enter;
    vector<int>leave;
    int num;
    for (int i = 0; i < 3; i++)
    {
        cin >> num;
        enter.push_back(num);
    }
    for (int i = 0; i < 3; i++)
    {
        cin >> num;
        leave.push_back(num);
    }
    solution(enter, leave);
}