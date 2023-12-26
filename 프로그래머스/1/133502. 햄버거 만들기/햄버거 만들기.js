function solution(ingredient) {
    var answer = 0;
    let cnt = 0;
    let tmp= []
    for (let i = 0; i < ingredient.length; i ++) {
        tmp.push(ingredient[i])
        
        if (tmp.slice(-4).join("") === '1231') {
            tmp.splice(-4)
            cnt ++;
        }
    }
    
    return cnt;
}
