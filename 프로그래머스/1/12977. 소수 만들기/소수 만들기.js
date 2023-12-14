let answer = 0;
function is_prime(number) {
    let flag = 1;
    for (let i = 2; i <= Math.sqrt(number); i ++) {
        if (number % i === 0) {
            flag = 0
        } 
    }
    return flag
}

function dfs(now,cnt, total,nums) {
    if (cnt === 3) {
        if (is_prime(total)) {
            answer += 1
            console.log(answer)
        }
        return answer
    }
    
    for (let i = now+1; i < nums.length; i++) {
        dfs(i, cnt +1, total + nums[i],nums)
    }
    
}

function solution(nums) {
     for (let i = 0; i < nums.length; i++) {
        dfs(i,1, nums[i],nums)
    }
    
    return answer;
}