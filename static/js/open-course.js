var lech=document.querySelector(".lech");
var arrow_lect=document.querySelector(".arrow-lect");

arrow_lect.addEventListener("click",()=>{
    lech.classList.toggle("hide")
    if(lech.classList.contains("hide")){
        arrow_lect.classList.replace("bxs-down-arrow", "bxs-up-arrow");
      }
      else{
        arrow_lect.classList.replace("bxs-up-arrow", "bxs-down-arrow");
       
      }
})

