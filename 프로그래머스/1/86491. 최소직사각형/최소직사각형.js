function solution(sizes) {
    var answer = 0;
    for (let i = 0 ; i < sizes.length; i++) {
        if (sizes[i][0] < sizes[i][1]) {
            let temp = sizes[i][0];
            sizes[i][0] = sizes[i][1];
            sizes[i][1] = temp;
        }
    }
    
    Max = 0
    Min = 0
    
    for (let i = 0; i < sizes.length; i++) {
        Max = Math.max(Max, sizes[i][0])
        Min = Math.max(Min, sizes[i][1])
    }
   
    
    result = Max * Min
    
    return result;
}