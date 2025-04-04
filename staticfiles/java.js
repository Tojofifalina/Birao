const percentage = document.querySelectorAll('.percentage p')
percentage.forEach((e,i) =>{
    let val = parseInt(e.textContent);
    console.log(val);
    let circle = document.getElementById(`cercle${i + 1}`);
    let r = circle.getAttribute('r');
    let circ = Math.PI * 2* r ;
    let counteur = 0;
    let filvalue = (circ * (100 - val))/100;
    console.log(filvalue)
    setInterval(() =>{
        if (counteur == val){
            clearInterval()
        }else{
            counteur +=1;
            e.innerText = counteur +'%';
            circle.style.strokeDashoffset = filvalue;
        }
    },100/val)
})