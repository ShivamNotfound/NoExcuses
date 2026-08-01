const searchbar = document.getElementById("search_bar");
let equipments = document.querySelectorAll(".equipment_cards");
let name;
searchbar.addEventListener("input", (e)=>{
    
    const value = searchbar.value.toLowerCase();

    equipments.forEach(element => {
        name = element.getAttribute("name").toLowerCase();
        if(name.includes(value))
        {
            element.style.display = "";
        }
        else{
            element.style.display = "none";
        }
    });

})