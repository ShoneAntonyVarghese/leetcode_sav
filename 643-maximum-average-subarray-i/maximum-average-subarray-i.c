double findMaxAverage(int* nums, int numsSize, int k) {
    double window_sum=0,max_sum=0;
    int i;
    for(i=0;i<k;i++){

        window_sum +=nums[i];
       
    }
    max_sum = window_sum;
    
    for(i = k;i<numsSize;i++){
        window_sum += nums[i] - nums[i - k];
        if(window_sum > max_sum){

            max_sum = window_sum;
        }
    }
    return max_sum/k;
}