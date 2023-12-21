function solution(participant, completion) {
    var answer = '';
    com = {}
    completion.forEach((c) => {
        if (!com[c]) {
            com[c] = 1
        }else {
            com[c] +=1
        }
    })
    
    participant.forEach((p) => {
        if (com[p]) {
            com[p] -=1
        }else{
            answer = p
        }
    })
    
    return answer;
}