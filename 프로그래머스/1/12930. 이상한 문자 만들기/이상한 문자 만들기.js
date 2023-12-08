function solution(s) {
    var words = s.split(' ');
    var answer = '';

    for (let i = 0; i < words.length; i++) {
        for (let j = 0; j < words[i].length; j++) {
            if (j % 2 === 0) {
                answer += words[i][j].toUpperCase();
            } else {
                answer += words[i][j].toLowerCase();
            }
        }
        if (i < words.length - 1) {
            answer += ' '; // 단어 사이에 공백 추가
        }
    }

    return answer;
}
