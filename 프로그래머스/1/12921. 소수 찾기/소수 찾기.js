function is_prime(number) {
    if (number < 2) {
        return false;
    }
    if (number <= 3) {
        return true;
    }
    if (number % 2 === 0 || number % 3 === 0) {
        return false;
    }

    for (let i = 5; i * i <= number; i += 6) {
        if (number % i === 0 || number % (i + 2) === 0) {
            return false;
        }
    }

    return true;
}

let answer = 0;

function solution(n) {
    if (n < 2) {
        return 0;
    }

    answer = n >= 2 ? 1 : 0; // 2는 소수이므로 미리 카운트

    for (let i = 3; i <= n; i += 2) {
        if (is_prime(i)) {
            answer += 1;
        }
    }

    return answer;
}

// 테스트
console.log(solution(10)); // 예상 결과: 4
