function solution(n) {
    var answer = [];
    var result = 0;
    var num = 0;
    while (n > 0) {
        num = n % 3
        n = Math.floor(n / 3)
        answer.push(num)
    }
    console.log(answer.reverse())
    
    for (let i = 0; i < answer.length; i ++) {
        result += (3 ** i) * answer[i] 
    }
    
    return result;
}