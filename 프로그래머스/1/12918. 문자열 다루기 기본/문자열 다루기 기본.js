function solution(s) {
    flag = 1
    numbers = [0,1,2,3,4,5,6,7,8,9]
    
    for (let i = 0; i < s.length; i ++) {
        if (!numbers.includes(Number(s[i]))) {
            flag = 0
            break
        }
    }
    return (s.length === 4 || s.length === 6 ) && flag === 1 ? true : false
    
}