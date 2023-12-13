function solution(k, score) {
    var answer = [];
    let stack = [];
    score.forEach((el) => {
        if (stack.length < k) {
            stack.push(el)
            stack.sort((a,b) => b - a)
            answer.push(stack.slice(-1)[0])
        } else {
            stack.push(el)
            stack.sort((a,b) => b - a)
            stack.pop()
            answer.push(stack.slice(-1)[0])
            
        }
    })
    
    return answer;
}