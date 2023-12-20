function solution(X, Y) {
    let answer = ''
    X = X.split("")
    Y = Y.split("")
    // 해당 숫자가 얼마나 있는지 확인해서 더 낮은만큼 정답 문자열에 더함
    for(let i = 0 ; i < 10 ; i ++) {
        const curX = X.filter(a => Number(a) === i).length
        const curY = Y.filter(a => Number(a) === i).length
        answer+=String(i).repeat(Math.min(curX, curY))
    }
    if(answer === '') return "-1"
    if(Number(answer) === 0) return "0"
    
    return answer.split("").sort().reverse().join("")
}