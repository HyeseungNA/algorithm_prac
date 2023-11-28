function solution(s1, s2) {
    var answer = 0;
    const inter = s1.filter((el) => s2.includes(el))
    return inter.length;
}