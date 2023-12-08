function solution(s) {
    const words = [
        ['zero', 0],
        ['one', 1],
        ['two', 2],
        ['three', 3],
        ['four', 4],
        ['five', 5],
        ['six', 6],
        ['seven', 7],
        ['eight', 8],
        ['nine', 9]
    ];

    while (isNaN(+s)) {
        words.forEach((word) => {
            if (s.includes(word[0])) {
                s = s.replace(word[0], String(word[1]));
            }
        });
    }

    return +s;
}

// 예제 사용법
console.log(solution("one4seveneight"));  // 결과: 1478
