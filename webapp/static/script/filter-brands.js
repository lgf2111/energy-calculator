var brand_list = ["Panasonic", "LG", "Samsung", "Mitsubishi", "SHARP", "Others", "Daikin", "Electrolux", "Philips"];
const appliance = document.getElementById("Appliance");
const brands = document.getElementById("Brand");

function filterFunction() {
    if (appliance == "Air-Conditioner") {
        brands.innerText = brand_list.filter(airCon);
    } else if (appliance == "Fridge") {
        brands.innerText = brand_list.filter(fridge);
    } else if (appliance == "Television") {
        brands.innerText = brand_list.filter(tv);
    } else {
        brands.innerText = brand_list.filter(washingMachine);
    }
}
    
function airCon() {
    return brand_list = ["Daikin", "Panasonic", "Electrolux", "Mitsubishi", "Samsung", "Others"];
}

function fridge() {
    return brand_list = ["Panasonic", "LG", "Hitachi", "Samsung", "Others"];
}

function tv() {
    return brand_list = ["Panasonic", "LG", "Philips", "Samsung", "Others"];
}

function washingMachine() {
    return brand_list = ["Panasonic", "LG", "SHARP", "Samsung", "Others"];
}

document.addEventListener('click', filterFunction);