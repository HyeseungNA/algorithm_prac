function solution(num_list) {
    var answer = [];
    let result1 = 0;
    let result2 = 0;
    for ( let i = 0 ; i < num_list.length; i ++) {
        if (num_list[i] % 2 === 0) {
            result1 += 1
        }else {
            result2 += 1
        }
    }
    answer.push(result1, result2)
    return answer;
}