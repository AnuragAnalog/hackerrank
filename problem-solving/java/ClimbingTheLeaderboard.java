public class ClimbingTheLeaderboard {
    static int j;

    // Complete the climbingLeaderboard function below.
    static int[] climbingLeaderboard(int[] scores, int[] alice) {
        ArrayList<Integer> am=new ArrayList<Integer>();
        am.add(scores[0]);
        for (int i = 1; i <scores.length ; i++) {
            if (scores[i]!=scores[i-1])
                am.add(scores[i]);
        }
        Integer sc[]=new Integer[am.size()];
                sc=am.toArray(sc);
        j=sc.length-1;
        int ans[]=new int[alice.length];
        for (int i = 0; i <alice.length ; i++) {
            ans[i]=rank(alice[i],sc);
        }
        return ans;
    }

    //Helper Function that finds out the current Rank
    static int rank(int x,Integer[] scores){

        if (x>=scores[0]){
            return 1;
        }
        if (x<scores[scores.length-1]) {
            return scores.length+1;
        }
        if (x==scores[scores.length-1]) {
            return scores.length;
        }
        for (; j>0 ; j--) {
            if(scores[j]<=x && scores[j-1]>x)
                return j+1;
        }
        return -1;
}
