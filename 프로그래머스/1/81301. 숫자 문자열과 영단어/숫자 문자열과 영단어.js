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

    words.forEach((word) => {
        s = s.replaceAll(word[0], String(word[1]));
    });

    return Number(s);
}

// 테스트
console.log(solution("one4seveneight"));  // 결과: 1478
