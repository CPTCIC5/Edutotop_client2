var likes=document.querySelector(".likes");
var span=document.querySelector(".likes span");
var dislikes=document.querySelector(".dislikes");
var commfeatures=document.querySelectorAll(".comment-feature");


likes.addEventListener("click",()=>{
    dislikes.classList.remove("liked");
    likes.classList.toggle("liked");
})

dislikes.addEventListener("click",()=>{
    dislikes.classList.toggle("liked");
    likes.classList.remove("liked");
})
commfeatures.forEach(commfeature =>{
    var commentlikes=commfeature.querySelector(".commentlikes") ;
var commentdislikes=commfeature.querySelector(".commentdislikes");
var heart=commfeature.querySelector(".heart");
    commentlikes.addEventListener("click",()=>{
        commentlikes.classList.toggle("liked");
        commentdislikes.classList.remove("liked");

    })
    commentdislikes.addEventListener("click",()=>{
        commentdislikes.classList.toggle("liked");
        commentlikes.classList.remove("liked");
    })
    heart.addEventListener("click",()=>{
        heart.classList.toggle("heart-liked");
    })
})


