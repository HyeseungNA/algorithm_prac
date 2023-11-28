function solution(n) {
    var answer = 2;
    const Root = Math.floor(Math.sqrt(n))
    for (let i = 0; i <= Root; i++) {
        if (i ** 2 === n) {
            answer = 1
        }
    }
    return answer;
}