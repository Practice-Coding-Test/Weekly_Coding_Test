import java.util.*;

class Solution {
    public int[] solution(int[] enter, int[] leave) {
        int[] answer = new int[enter.length];

        Set<Integer> room = new HashSet<>();
        int enterIdx = 0;
        int leaveIdx = 0;
        int endIdx = enter.length;

        while(enterIdx < endIdx || leaveIdx < endIdx ) {
            // 퇴실하는 사람: 방에 남은 사람들 수 만큼 만남 += room.size()-1
            // 남은 사람: 퇴실하는 사람 만남 += 1
            if (room.contains(leave[leaveIdx])) {
                answer[leave[leaveIdx] - 1] += room.size() - 1;
                room.remove(leave[leaveIdx]);

                Iterator<Integer> iter = room.iterator();
                while (iter.hasNext()) {
                    answer[iter.next() - 1]++;
                }

                leaveIdx++;
            } else {
                room.add(enter[enterIdx]);
                enterIdx++;
            }
        }
<<<<<<< HEAD
        return answer;
    }
}
=======
        return answer; 
    }
}
>>>>>>> d563b7985ce2d32b3f7c111bc86c182449e250fe
