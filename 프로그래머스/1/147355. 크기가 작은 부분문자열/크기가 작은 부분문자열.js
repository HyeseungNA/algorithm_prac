function solution(t, p) {
    cnt = 0
    for (let i = 0; i <= t.length - p.length; i ++) {
        num = ''
        for (let j = 0; j < p.length; j ++) {
            num += t[i+j]
        }
        
        if (Number(num) <= Number(p)) {
            cnt += 1
        }

    }

    return cnt;
}