var video=document.querySelector(".notes");
var dot=document.querySelector(".bx-dots-vertical-rounded");
var features=document.querySelector(".other-features");
dot.addEventListener("click",()=>{
    features.classList.toggle("hide");
})