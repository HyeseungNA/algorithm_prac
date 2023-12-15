function solution(n, m, section) {
    let answer = 0;
    let part = 0;
    section.forEach((num) => {
        if (num > part) {
            part = num + m - 1;
            answer +=1;
        }
    })
    return answer;
    }
    
