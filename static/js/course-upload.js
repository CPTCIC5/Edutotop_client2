ul=document.querySelector("ul");
input = document.getElementById('tag-input');
file=document.getElementById("file");
customfile=document.getElementsByClassName('file');
file_div=document.getElementsByClassName('file-box');
tags = [];

createTag();



function createTag(){
    ul.querySelectorAll("li").forEach(li => li.remove());
    tags.slice().reverse().forEach(tag =>{
        let liTag = `<li>${tag} <i class="uit uit-multiply" onclick="remove(this, '${tag}')"></i></li>`;
        ul.insertAdjacentHTML("afterbegin", liTag);
    });
}

function remove(element, tag){
    let index  = tags.indexOf(tag);
    tags = [...tags.slice(0, index), ...tags.slice(index + 1)];
    element.parentElement.remove();
    countTags();
}

function file_upload(){
    file.click();
    
}
function condition(){
    if(file.value){
        document.getElementById("file-id").innerHTML=file.value;
        // span_file=document.createElement('h4');
        // span_file.setAttribute('class','file_span');
    }
}

function addTag(e){
    if(e.key == "Enter"){
        let tag = e.target.value.replace(/\s+/g, ' ');
        if(tag.length > 1 && !tags.includes(tag)){
            if(tags.length < 10){
                tag.split(',').forEach(tag => {
                    tags.push(tag);
                    createTag();
                });
            }
        }
        e.target.value = "";
    }
}

input.addEventListener("keyup", addTag);

