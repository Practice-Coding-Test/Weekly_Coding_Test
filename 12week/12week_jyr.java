mport java.lang.Math;

class Solution {
	public boolean is_visited[];
	public int answer = 0;
		    
	public int solution(int k, int[][] dungeons) {
		is_visited = new boolean[dungeons.length];
				            
		dfs(k, dungeons, 0);
					            
		return answer;
	}
		        
	public void dfs(int currK, int[][] dungeons, int cnt){
		for(int i = 0; i < dungeons.length; i++) {
			if(!is_visited[i] && dungeons[i][0] <= currK) {
				is_visited[i] = true;
				dfs(currK - dungeons[i][1], dungeons, cnt+1);
				is_visited[i] = false;
			}
		}
		answer = Math.max(answer, cnt);
	}
}
