var input=document.querySelector("#thumbnail");
var input2=document.querySelector("#file");
var error=document.getElementById("error");
var submit=document.querySelector("#submit");

function clike(){
    input.click();
}

function clicke(){
    input2.click();
}
input2.addEventListener("change",()=>{
    if(!input2.value){
        error.innerHTML="No file has been uploaded";
    }
  
    
})

submit.addEventListener("click",()=>{
    if(!input2.value){
        error.innerHTML="No file has been uploaded";
    }
})