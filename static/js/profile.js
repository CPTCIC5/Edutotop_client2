var videos = document.querySelector("#profile_tab_videos_btn");
var notes = document.querySelector("#profile_tab_notes_btn");
var video=document.querySelector(".card-videos");
var note=document.querySelector(".card-notes");



videos.addEventListener("click",()=>{
  
    video.classList.remove("hide");
    note.classList.add("hide");
    videos.classList.add("tab_active");
    notes.classList.remove("tab_active");
});
notes.addEventListener("click",()=>{
    video.classList.add("hide");
    note.classList.remove("hide");
    videos.classList.remove("tab_active");
    notes.classList.add("tab_active");
})

