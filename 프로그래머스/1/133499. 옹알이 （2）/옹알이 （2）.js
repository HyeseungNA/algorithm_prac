function solution(babbling) {
    words = ["aya","ye","woo","ma"]
    
    let answer = 0;
    
    for (let i = 0; i < babbling.length; i ++) {
        let bab = babbling[i];
        for (j = 0; j < words.length; j++) {
            if (bab.includes(words[j].repeat(2))) {
                break
            }
            bab = bab.split(words[j]).join(" ")
        }
        if (bab.split(" ").join("").length === 0) {
            answer += 1
        }
        }
        return answer
    }