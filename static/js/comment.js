var comment_box=document.querySelector(".comment-box");
var reply_box=document.querySelector(".reply-box");
var reply_profile=document.querySelector(".do-reply .circle");
var commentbtns=document.querySelector(".commentbtns");
var replybtns=document.querySelector(".replybtns");
var cancelbtn=document.querySelector(".comment-cancel-btn");
var commentbtn=document.querySelector(".comment-btn");
var replybtn=document.querySelector(".reply-btn");
var replycancelbtn=document.querySelector(".reply-cancel-btn");
var reply=document.querySelector(".reply");

comment_box.addEventListener("focus",()=>{
    commentbtns.classList.remove("hide");
})

cancelbtn.addEventListener("click",()=>{
    commentbtns.classList.add("hide");
})

reply.addEventListener("click",()=>{
    reply_box.classList.remove("hide");
    reply_profile.classList.remove("hide");
})

reply_box.addEventListener("focus",()=>{
    replybtns.classList.remove("hide");
})

replycancelbtn.addEventListener("click",()=>{
    reply_box.classList.add("hide");
    replybtns.classList.add("hide");
    reply_profile.classList.add("hide");
})




