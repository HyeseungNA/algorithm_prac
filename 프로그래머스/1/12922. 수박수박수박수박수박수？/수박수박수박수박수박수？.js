function solution(n) {
    var answer = '';
    word = '수박'
    if (n % 2 === 0) {
        answer = word.repeat(Math.floor(n/2))
    }else {
        answer = word.repeat(Math.floor(n/2)) + '수'
    }
    return answer;
}