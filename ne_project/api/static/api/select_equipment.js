const searchbar = document.getElementById("search_bar");
let equipments = document.querySelectorAll(".equipment_cards");
const equipment_inputs = document.querySelectorAll(".equipment_card_box")
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


let selected_count = 0;
equipment_inputs.forEach(ele => {
    ele.addEventListener('change', (e) =>
    {
        let id = ele.getAttribute('id')
        let equipmentPercent = document.getElementById(`${id}forPercent`);
        let sub_count = Number(equipmentPercent.getAttribute('value'));
        if(ele.checked)
        {
            selected_count += sub_count;
            mus_percent.textContent = `${Math.round(selected_count/36*100)}% of muscles`;
                
        }
        else
        {
            selected_count -= sub_count;
            mus_percent.textContent = `${Math.round(selected_count/36*100)}% of muscles`;
        }
    })
})