function solution(k, m, score) {
    score.sort((a,b) => b - a)
    let i = 0;
    let result = 0;
    while (i <= score.length) {
        let tmp = score.slice(i,i+m)
        
        if (tmp.length === m) {
            result += (Math.min(...tmp) * m)
        }
        i += m
    }
    return result;
}