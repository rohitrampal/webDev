const btn = document.querySelector("button");
const body = document.querySelector("body");
const span = document.querySelector(".span");

function randomColor(){
    let red = Math.floor(Math.random()*256);
    let green = Math.floor(Math.random()*256);
    let blue = Math.floor(Math.random()*256);
    let random = `rgb(${red},${green},${blue})`;
    return random;
};

btn.addEventListener("click",()=>{
    let color = randomColor();
    body.style.backgroundColor  = color;
    span.textContent = color;
    console.log(color);

});