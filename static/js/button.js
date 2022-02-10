var savednotes=document.querySelector(".saved-notes");
var savedcourses=document.querySelector(".saved-courses");
var cardcourses=document.querySelector(".card-courses");
var cardnotes=document.querySelector(".card-notes");

savednotes.addEventListener("click",()=>{
    cardcourses.classList.add("hide");
    cardnotes.classList.remove("hide");

    savednotes.classList.add("active");
    savedcourses.classList.remove("active");
})

savedcourses.addEventListener("click",()=>{
    cardcourses.classList.remove("hide");
    cardnotes.classList.add("hide");

    savednotes.classList.remove("active");
    savedcourses.classList.add("active");
})