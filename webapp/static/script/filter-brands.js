const brandList = ["Panasonic", "LG", "Samsung", "Mitsubishi", "SHARP", "Others", "Daikin", "Electrolux", "Philips"];
const appliance = document.getElementById("appliance");
const brand = document.getElementById("brand");

document.addEventListener('click', () => {

    while (appliance.options.length > 0) {
        appliance.remove(appliance.options.length - 1)
    }
    switch(appliance.value) {
        case "Air-Conditioner":
            for (let v of ["Daikin", "Panasonic", "Electrolux", "Mitsubishi", "Samsung", "Others"]) {
            let option = document.createElement('option')
            option.text = v
            option.value = v
            appliance.add(option, null)
            }
            break;
        case "Fridge":
            for (let v of ["Panasonic", "LG", "Hitachi", "Samsung", "Others"]) {
            let option = document.createElement('option')
            option.text = v
            option.value = v
            appliance.add(option, null)
            }
            break;
        case "Television":
            for (let v of ["Panasonic", "LG", "Philips", "Samsung", "Others"]) {
            let option = document.createElement('option')
            option.text = v
            option.value = v
            appliance.add(option, null)
            }
            break;
        case "Washing Machine":
            for (let v of ["Panasonic", "LG", "SHARP", "Samsung", "Others"]) {
            let option = document.createElement('option')
            option.text = v
            option.value = v
            appliance.add(option, null)
            }
            break;
        default:
            // code block
        }
});