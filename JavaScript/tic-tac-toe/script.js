let currPlayer = "X";
let arr =Array(9).fill(null);

function Click(e){
    const id = Number(e.id);

    if(arr[id]!==null) return; // if the cell is not empty, do nothing and exit the function
    
    arr[id] = currPlayer;
    e.innerText = currPlayer;
    showWinner();
    currPlayer = currPlayer === "X" ? "O" : "X";    
    console.log(arr);
}

function showWinner(){
    if(
        (arr[0] !== null &&  arr[0] == arr[1] && arr[1] == arr[2]) ||
        (arr[3] !== null &&  arr[3] == arr[4] && arr[4] == arr[5]) ||
        (arr[6] !== null &&  arr[6] == arr[7] && arr[7] == arr[8]) ||

        (arr[0] !== null &&  arr[0] == arr[3] && arr[3] == arr[6]) ||
       (arr[1]!== null &&  arr[1] == arr[4] && arr[4] == arr[7]) ||
       (arr[2]!== null &&  arr[2] == arr[5] && arr[5] == arr[8]) ||

       (arr[0]!== null &&  arr[0] == arr[4] && arr[4] == arr[8]) ||
        (arr[2] !== null &&  arr[2] == arr[4] && arr[4] == arr[6]) 
         
    ){
        alert(`Game over !!
            Player ${currPlayer} Won!!`);
        document.write(`${currPlayer} is the winner`);
        return;
    }
    if(!arr.some(e=>e===null)){
        alert("Draw!!");
        document.write(`Match draw !!`);
        return;
    }
}