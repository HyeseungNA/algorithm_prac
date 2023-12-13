function solution(nums) {
    len = Math.floor(nums.length / 2)
    mons = new Set([...nums])
    size = mons.size
    
    return size >= len ?len : size
     
}