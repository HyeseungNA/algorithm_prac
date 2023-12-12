function solution(numbers) {
    let result = [];
    for (let i = 0; i < numbers.length; i++) {
        for(let j = 0; j < numbers.length; j++) {
            if (i !== j && !result.includes(numbers[i] + numbers[j])) {
                result.push(numbers[i] + numbers[j])
            }
        }
    }
    result.sort((a,b) => a - b)
    return result
}