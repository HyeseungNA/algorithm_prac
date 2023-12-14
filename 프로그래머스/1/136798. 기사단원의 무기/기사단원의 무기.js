function solution(number, limit, power) {
    var answer = 0;
    for (let i = 1; i <= number; i ++) {
        let tmp = 0
        
        for (let j = 1; j <= Math.sqrt(i); j++) {
            if (i % j == 0) {
                tmp += 1
                
                if (j < Math.floor(i / j)) {
                tmp += 1
            }
            } 
        }
        console.log(tmp)
        if (tmp <= limit) {
            answer += tmp
        } else {
            answer += power
        }
    }
    return answer;
}