function solution(keymap, targets) {
    var answer = [];
    keys = {}
    for (let i = 0; i < keymap.length; i ++) {
        tmp = keymap[i].split("");

        tmp.forEach((el) => {
            // 딕셔너리에 아직 아무것도 없다면
            if (!keys[el]) {
                keys[el] = tmp.indexOf(el) + 1
            } else {
                if (keys[el] > tmp.indexOf(el) + 1 ) {
                    keys[el] = tmp.indexOf(el) + 1
                }
            }
            
        })
    }
    
    // target 돌아다니면서 딕셔너리 value들 더해주기
    targets.forEach((ta) => {
        let flag = 1
        total  = 0
        let lst = ta.split("")
        // console.log(lst)
        lst.forEach((el) => {
            // 딕셔너리 값이 있으면 더해주기
            if (keys[el]) {
                total += keys[el]
            // target에 없으면 도는거 멈추고 answer에 -1 넣어주기
            } else {
                flag = 0
                return false
            }
            
        })
        if (flag) {
            answer.push(total)
        }else {
            answer.push(-1)
        }
        
    })
    
    
    
    return answer;
}