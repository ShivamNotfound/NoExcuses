
const goals = document.getElementsByClassName("goal_items");
const sortform = document.querySelector("#sort_form");
sortform.addEventListener("change",(e)=>
    {
        sortform.submit();
        console.log("Ding");
    })
console.log("connected!");
