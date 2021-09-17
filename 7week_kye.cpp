#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
using namespace std;

vector<int> solution(vector<int> enter, vector<int> leave) {
    vector<int> answer(enter.size(), 0);
    set<int>room;//중복제거를 위해 set 사용
    vector<vector<int>>visited(enter.size() + 1, vector<int>(enter.size() + 1, 0));//2차원 벡터 만들기, 방문 확인용
    int inidx = 0;
    int outidx = 0;
    while (outidx < leave.size())//퇴실 순서를 기준으로 루프를 돈다. 다 돌면 끝난다
    {
        //room에 퇴실 순서인 사람이 없는경우
        while (room.find(leave[outidx]) == room.end())
        {
            answer[enter[inidx] - 1] += room.size(); // 현재 입실하면 만날 수 있는 사람의 수
            for (int i : room)//room에 있는 사람들 만남 표시
            {
                answer[i - 1]++;
            }
            room.insert(enter[inidx]);//입실 순서에 있는 사람 들어오도록
            inidx++;
        }
        //퇴실순서인 사람이 들어오면 while문 벗어난다.
        //room에 퇴실 순서인 사람이 있는 경우
        while ((outidx < leave.size()) && (room.find(leave[outidx]) != room.end()))
            // outidx가 계속증가하다 보면 vector out of range 발생
        {
            room.erase(leave[outidx]);//방에서 제거
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