function solution(s, n) {
    const l = "abcdefghijklmnopqrstuvwxyz";
    const u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    let answer = '';

    s.split('').forEach((ch) => {
        let idx;

        if (l.includes(ch)) {
            idx = (l.indexOf(ch) + n) % 26;
            answer += l[idx];
        } else if (u.includes(ch)) {
            idx = (u.indexOf(ch) + n) % 26;
            answer += u[idx];
        } else {
            answer += ' ';
        }
    });

    return answer;
}

// 예제 사용법
console.log(solution("abcde", 3));
