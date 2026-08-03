const searchbar = document.getElementById("search_bar");
let equipments = document.querySelectorAll(".equipment_cards");
const equipment_inputs = document.querySelectorAll(".equipment_card_box")
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

const selected_set = new Set();
const mapping_data = document.getElementById("sub_data");
const equip_json = JSON.parse(mapping_data.textContent)
const percent = document.getElementById("percent");
equipment_inputs.forEach(ele => {
    ele.addEventListener('change', (e) =>
    {
        selected_set.clear();
        document.querySelectorAll(".equipment_card_box:checked")
        .forEach((equipment)=>{
            equip_json[equipment.id]
            .forEach((id)=>selected_set.add(id));
        })
        percent.textContent = `${Math.round(selected_set.size/36*100)}`;
    })
})