function solution(lottos, win_nums) {
    scores = [6,6,5,4,3,2,1]
    var answer = [];
    const Max = lottos.filter((lotto) => win_nums.includes(lotto) || lotto === 0)
    const Min = lottos.filter((lotto) => win_nums.includes(lotto))
    
    scores.forEach((score,idx) => {
        if (Max.length === idx) {
            answer.push(scores[idx])
        }
    })
      scores.forEach((score,idx) => {
        if (Min.length === idx) {
            answer.push(scores[idx])
        }
    })
    
    return answer;
}