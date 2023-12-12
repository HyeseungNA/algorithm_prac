function solution(food) {
   let order = ''
   for (let i = 1; i < food.length; i ++) {
       order += String(i).repeat(Math.floor(food[i]/2))
       
   }
    const reversed = order.split('').reverse().join('')
    order += "0"
    order += reversed
    return order
   
  
}