function solution(nums) {
    len = Math.floor(nums.length / 2)
    const mons = {};
    nums.forEach((el) => {
        if (!mons[el]) {
            mons[el] = 1
        } else {
            mons[el]  += 1
        }
    })
    mons_len = Object.keys(mons).length
    
    if (mons_len >= len) {
        return len
    }else {
        return mons_len
    }
    
}