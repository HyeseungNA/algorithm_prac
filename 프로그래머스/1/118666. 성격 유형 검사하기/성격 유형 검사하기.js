function solution(survey, choices) {
    var answer = '';
    type = {'R':0,'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0 , 'N':0}
    scores = [0,3,2,1,0,1,2,3]
    
    for (let i = 0 ; i < survey.length; i ++) {
        su = survey[i]
        su = su.split('') // 리스트로 변환, 비동의: 첫번째, 동의 : 두번째   
        let target;
        
        if (choices[i] >= 5) { // 동의 쪽
            target = su[1]
            type[target] += scores[choices[i]]
        }else {
            target = su[0];
            type[target] += scores[choices[i]]
        }
    }   
            
    const ty = Object.keys(type)
    
    for (let i = 0; i < ty.length; i+=2) {
        if (type[ty[i]] < type[ty[i+1]]) {
            answer += ty[i+1]
        } else {
            answer += ty[i]
        }
    }

    return answer;
}
