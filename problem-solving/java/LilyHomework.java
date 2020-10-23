class lilysHomework{

// Complete the lilysHomework function below.
    static int lilysHomework(int[] arr) {
        
        int[] temp = new int[arr.length];

        for(int i=0;i<arr.length;i++)
            temp[i] = arr[i];

        Arrays.sort(arr);

        int[] rev = reverse(arr);

        int ans = (int)Math.min(minSwaps(temp,arr),minSwaps(temp,rev));

        return ans;
        
    }

    //Helper function to count the minimum number of Swaps Required
    static int minSwaps(int[] arr,int[] ordered){
        HashMap<Integer,Integer> maps = new HashMap<>();
        for (int i = 0; i <arr.length; i++) {
            maps.put(arr[i],i);
        }
        for (int i = 0; i < ordered.length; i++) {
            ordered[i] = maps.get(ordered[i]);
        }
        maps.clear();
        int swaps =0;
        for (int i = 0; i < ordered.length; i++) {
            int val = ordered[i];
            if (val < 0)
                continue;
            while(val!=i){
                int newVal = ordered[val];
                ordered[val] = -1;
                val = newVal;
                swaps++;
            }
            ordered[i] = -1;
        }
        return swaps;
    }

//Helper Function return the reverse of a given Array
    private static int[] reverse(int[] arr) {
        int len = arr.length;
        int[] rev = new int[len];
        for (int i = 0; i < len; i++) {
            rev[i] = arr[len-1-i];
        }
        return rev;
    }
}
