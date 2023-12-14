function solution(answers) {
    let answer = [];
    const s1 = [1,2,3,4,5]
    const s2 = [2,1,2,3,2,4,2,5]
    const s3 = [3,3,1,1,2,2,4,4,5,5]
    
    const s1c = answers.filter((a,i) => a === s1[i%s1.length]).length
    const s2c = answers.filter((a,i) => a === s2[i%s2.length]).length
    const s3c = answers.filter((a,i) => a === s3[i%s3.length]).length
    
    const Max = Math.max(s1c,s2c,s3c)
    
    if (Max === s1c) {
        answer.push(1)
    } if (Max === s2c) {
        answer.push(2)
    } if (Max === s3c) {
        answer.push(3)
    }
    return answer
}