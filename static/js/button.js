var notes_btn=document.querySelector(".notes-btn");
var notes_less_btn=document.querySelector(".notes-less-btn");
var videos_btn=document.querySelector(".videos-btn");
var videos_less_btn=document.querySelector(".videos-less-btn");
var text=document.querySelector(".text");
var notes=document.querySelector("#notes");
var video=document.querySelector(".videos");
var note=document.querySelector(".notes");
var videos=document.querySelector("#videos");
var top_title=document.querySelector(".top-title");


        //notes
notes_btn.addEventListener("click",()=>{
    text.style.display="none";
    videos.style.display="none";
    video.style.display="none";
    notes_btn.classList.add("hide");
    notes_less_btn.classList.remove("hide");
    
})
notes_less_btn.addEventListener("click",()=>{
    text.style.display="flex";
    videos.style.display="flex";
    video.style.display="flex";
    notes_btn.classList.remove("hide");
    notes_less_btn.classList.add("hide");
})
        //videos
videos_btn.addEventListener("click",()=>{
    text.style.display="none";
    note.style.display="none";
    notes.style.display="none";
    
    videos_btn.classList.add("hide");
    videos_less_btn.classList.remove("hide");
})
videos_less_btn.addEventListener("click",()=>{
    text.style.display="flex";
    notes.style.display="flex";
    note.style.display="flex";
    videos_btn.classList.remove("hide");
    videos_less_btn.classList.add("hide");
})
