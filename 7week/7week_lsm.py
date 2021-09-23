def solution_7(enter, leave):
    result = [0] * len(enter)

    check = []

    idx = 0
    for i in leave:
        # ����� ����� �濡 ���� ������ �Խ�
        while i not in check:
            check.append(enter[idx])
            idx += 1
        # ����� ����� �濡 ���´ٸ�, �ش� ��� ���
        check.remove(i)

        # ���� �濡 �ִ� ������� ���� ��� ���� 1�� ������
        for j in check:
            result[j-1] += 1
        
        # ����� ����� ���� ��� ���� ���� �� �ο����� ������
        result[i-1] += len(check)

    return result

print(solution_7([1,4,2,3], [2,1,3,4]))

