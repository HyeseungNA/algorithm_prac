function solution(n, arr1, arr2) {
    var answer = []; // 이진수 배열 넣기
    for (let i = 0; i < n; i++) {
        let num1 = arr1[i];
        let num2 = arr2[i];
        let line = '';
        for (let j = 0; j < n; j ++){
            line = (num1 % 2 + num2 % 2) === 0? ' '+line : '#'+line;
            num1 = Math.floor(num1 / 2);
            num2 = Math.floor(num2 / 2);
        }
        answer.push(line);
    }
    
    return answer;
}
