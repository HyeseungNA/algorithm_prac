function solution(s) {
    let stack = [];
    let same = [];
    let notSame = [];
    let count = 0;
    let i = 0;
    for (let i = 0; i <s.length; i++) {
        stack.push(s[i])
        
        same = stack.filter((el) => el === stack[0]);
        notSame = stack.filter((el) => el !== stack[0]);
        
        if (same.length === notSame.length) {
            stack = [];
            same = [];
            notSame = [];
            count ++;
        }
        
    }
    if (stack.length !==0) {
        count ++
    }
    return count
}