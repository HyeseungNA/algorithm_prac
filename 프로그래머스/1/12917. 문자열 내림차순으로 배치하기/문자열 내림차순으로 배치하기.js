function solution(s) {
    var answer = '';
    lst = s.split('')
    answer = lst.sort().reverse().join('')
    return answer;
}