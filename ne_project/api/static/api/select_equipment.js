const searchbar = document.getElementById("search_bar");
let equipments = document.querySelectorAll(".equipment_cards");
let name;
const mus_percent = document.getElementById("muscle_percent");
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

equipments.forEach(ele => {
    ele.addEventListener('change', (e) =>
    {
        if(ele.checked){
        console.log("Here?");
        let sub_length = Number(ele.getAttribute('key'));
        mus_percent.textContent = `${sub_length/36}% of muscles`;}
    })
})