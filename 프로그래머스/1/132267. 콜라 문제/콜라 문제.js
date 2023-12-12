function solution(a, b, n) {
    let result = 0;
    while (n >= a) {
        let get = 0;
        let rest = 0;
        get = Math.floor(n / a) * b
        rest = Math.floor(n % a)
        n = get + rest
        result += get
        
    }
    return result

}