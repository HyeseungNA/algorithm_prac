function solution(money) {
    var answer = [];
    cup = Math.trunc(money / 5500)
    rest = money -= cup * 5500
    answer.push(cup, rest)
    return answer;
}