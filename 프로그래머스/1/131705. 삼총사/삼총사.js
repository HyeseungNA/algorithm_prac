function dfs(now, cnt, visited, answer, number, result) {
    if (cnt === 3) {
        if (answer === 0) {
            result++;  
        }
        return result;
    }

    for (let j = now; j < number.length; j++) {
        if (visited[j] === 0) {
            visited[j] = 1;
            result = dfs(j, cnt + 1, visited, answer + number[j], number, result);
            visited[j] = 0;  
        }
    }

    return result;
}

function solution(number) {
    let visited = new Array(number.length).fill(0);
    let result = 0;

    for (let i = 0; i < number.length; i++) {
        let answer = number[i];
        visited[i] = 1;
        result = dfs(i, 1, visited, answer, number, result);
        
    }

    return result;
}

