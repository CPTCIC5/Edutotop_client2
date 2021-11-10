let sidebar = document.querySelector(".sidebar");
let closeBtn = document.querySelector("#btn");
let searchBtn = document.querySelector(".bx-search");
let dropdown_student=document.querySelector(".dropdown-student");
let dropdown_teacher=document.querySelector(".dropdown-teacher");
let dropdown_student_list = document.querySelector(".dropdown-list");
let dropdownli=document.querySelector(".dropdownli");
let dropdownlist=document.querySelector(".dropdownlist");
let arrow=document.querySelector("#arrow");
let arrowteach=document.querySelector("#arrow-teach");

closeBtn.addEventListener("click", ()=>{
  sidebar.classList.toggle("open");
  menuBtnChange();//calling the function(optional)
});

searchBtn.addEventListener("click", ()=>{ // Sidebar open when you click on the search iocn
  sidebar.classList.toggle("open");
  menuBtnChange(); //calling the function(optional)
});

dropdown_student.addEventListener("click",()=>{

  if(dropdownlist.classList.contains("dropdown-list")){
    dropdownli.classList.toggle("dropdown-list");
    
  }
  else{
    dropdownlist.classList.toggle("dropdown-list");
    dropdownli.classList.toggle("dropdown-list");
    arrowteach.classList.replace("bxs-down-arrow", "bxs-up-arrow");

  }

  if(dropdownli.classList.contains("dropdown-list")){
    arrow.classList.replace("bxs-down-arrow", "bxs-up-arrow");
  }
  else{
    arrow.classList.replace("bxs-up-arrow", "bxs-down-arrow");
   
  }
});
dropdown_teacher.addEventListener("click",()=>{
  

  if(dropdownli.classList.contains("dropdown-list")){
    dropdownlist.classList.toggle("dropdown-list");
    
  }
  else{
    dropdownlist.classList.toggle("dropdown-list");
    dropdownli.classList.toggle("dropdown-list");
    arrow.classList.replace("bxs-down-arrow", "bxs-up-arrow");

  }


  if(dropdownlist.classList.contains("dropdown-list")){
    arrowteach.classList.replace("bxs-down-arrow", "bxs-up-arrow");
  }
  else{
    arrowteach.classList.replace("bxs-up-arrow", "bxs-down-arrow");
  }
});

// following are the code to change sidebar button(optional)
function menuBtnChange() {
 if(sidebar.classList.contains("open")){
   closeBtn.classList.replace("bx-menu", "bx-menu-alt-right");//replacing the iocns class
 }else {
   closeBtn.classList.replace("bx-menu-alt-right","bx-menu");//replacing the iocns class
 }
}


