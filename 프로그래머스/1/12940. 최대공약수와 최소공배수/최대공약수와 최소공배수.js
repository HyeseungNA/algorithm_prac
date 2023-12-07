function solution(n, m) {
    var answer = [];
    let gcd = 1;
    let lcm = 1;
    for (let i = 0; i <= Math.min(n,m); i ++) {
        if (n % i === 0 && m % i === 0) {
            gcd = i
        }
    }
    console.log(gcd)
    lcm = gcd * (n / gcd) * (m/gcd)
    answer.push(gcd,lcm)
    return answer;
}