function solution(N, stages) {
    let answer = [];
    let i = 1;  
    let ing = stages.length;
    let suc = 0;
    for (let i = 1; i <=N; i++) {
        suc = stages.filter((stage) => stage === i).length
        answer.push([i,suc/ing])
        ing = ing - suc;
        
    }
    answer.sort((a,b) => b[1] - a[1])
    return answer.map((v) => v[0])
    
    
}