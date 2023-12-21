function solution(s, skip, index) {
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
               't','u','v','w','x','y','z']
    word = s.split("")
    skip = skip.split("")
    result = ''
    word.forEach((w) => {
        let idx = 0; // 실제 옮길 인덱스
        let cnt = alphabet.indexOf(w) // 현재 인덱스
        while (idx < index ) {
            cnt ++;
            
            if (skip.includes(alphabet[cnt % 26])) {
                continue
            } else if (!skip.includes(alphabet[cnt % 26])) {
                idx ++
                // console.log(idx)
                // console.log(alphabet[cnt % 26]);
            }
            // console.log(cnt,idx,alphabet[cnt % 26])
        }
    result += alphabet[cnt % 26]
    })
    return result
}