const form = document.querySelector(".form-todo");
const text = document.querySelector(".form-todo input[type='text']");
const todoList = document.querySelector(".todo-list");


form.addEventListener("submit",(e)=>{
    e.preventDefault(); // stayed in same page
    const newText = text.value; 
    const newLi = document.createElement("li");
    const newList = `
    <span class="text">${newText}</span>
    <div class="todo-buttons">
      <button class="todo-btn done">Done</button>
      <button class="todo-btn remove">Remove</button>
    </div>`;
    newLi.innerHTML = newList;
    todoList.append(newLi);
    
    text.value = ""; // used for delete the existing txt
});

todoList.addEventListener("click",(e)=>{
    // to check if user  clicked on a button or not
    if(e.target.classList.contains("done")){
        const list = e.target.parentNode.previousElementSibling;
        list.style.textDecoration = "line-through";
    }
    if(e.target.classList.contains("remove")){
        const targeted = e.target.parentNode.parentNode;
        targeted.remove();
    }

});