const videos=document.querySelector("#videos");
const notes=document.querySelector("#notes");
const video=document.querySelector('.video');
const note=document.querySelector('.note');

video.addEventListener("click",()=>{
    videos.classList.remove("hide");
    notes.classList.add("hide");
    video.classList.add("active");
    note.classList.remove("active");
});
note.addEventListener("click",()=>{
    videos.classList.add("hide");
    notes.classList.remove("hide");
    video.classList.remove("active");
    note.classList.add("active");
})

