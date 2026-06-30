const searchbar = document.getElementById("search_bar");
const form = document.getElementById("search_form");

searchbar.addEventListener("change", (e)=>{
    console.log("Changing!");
    form.submit();
})