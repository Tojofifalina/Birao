function openNav() {

    document.querySelector('[nav]').classList.remove("close_nav");

    /*document.querySelector('[contener]').classList.replace("max_contener", "min_contener");*/

}

function closeNav() {


    document.querySelector('[nav]').classList.add("close_nav");
    /*document.querySelector('[contener]').classList.replace("min_contener", "max_contener");*/

}
function Anim(){
    document.querySelector('[main]').classList.replace("main","main_pe")
    
    const t = setInterval(() =>{
        document.querySelector('[main]').classList.replace("main_pe","main")
            clearInterval(t)
        
    },900)
    
    /*setTimeout(() =>{
        document.querySelector('[main]').classList.replace("main_pe","main")
           
        
    },900)*/
   
    
    
}
let popup = document.getElementById("popup")
function Openpopup() {
    popup.classList.add("open-popup")
}
function Closepopup() {
    popup.classList.remove("open-popup")
    document.getElementById("about").classList.remove("active")
}
if (window.innerWidth <= 360) {
    console.log(window.innerWidth + "ddddfdfdf")
    function openNav() {
        document.querySelector('[pe_nav]').classList.add("open-pe_nav");

    }
}


const callback = function (win, observer) {
    console.log(win)

}
const spies = document.querySelector('[spy]')
console.log("ddddd= " + spies.classList)

const observere = new IntersectionObserver(callback, {})
observere.observe(spies)
console.log((window.innerWidth - 200) * window.innerHeight)