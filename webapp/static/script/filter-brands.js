var brandList = [
  "Panasonic",
  "LG",
  "Samsung",
  "Mitsubishi",
  "SHARP",
  "Others",
  "Daikin",
  "Electrolux",
  "Philips",
];
var appliance = document.getElementById("appliance");
var brand = document.getElementById("brand");

while (brand.options.length > 0) {
    brand.remove(brand.options.length - 1);
  }

appliance.addEventListener("change", () => {
  while (brand.options.length > 0) {
    brand.remove(brand.options.length - 1);
  }
  switch (appliance.value) {
    case "Air-Conditioner":
      for (let v of [
        "Daikin",
        "Panasonic",
        "Electrolux",
        "Mitsubishi",
        "Samsung",
        "Others",
      ]) {
        let option = document.createElement("option");
        option.text = v;
        option.value = v;
        brand.add(option, null);
      }
      break;
    case "Fridge":
      for (let v of ["Panasonic", "LG", "Hitachi", "Samsung", "Others"]) {
        let option = document.createElement("option");
        option.text = v;
        option.value = v;
        brand.add(option, null);
      }
      break;
    case "Television":
      for (let v of ["Panasonic", "LG", "Philips", "Samsung", "Others"]) {
        let option = document.createElement("option");
        option.text = v;
        option.value = v;
        brand.add(option, null);
      }
      break;
    case "Washing Machine":
      for (let v of ["Panasonic", "LG", "SHARP", "Samsung", "Others"]) {
        let option = document.createElement("option");
        option.text = v;
        option.value = v;
        brand.add(option, null);
      }
      break;
    default:
      option = document.createElement("option");
      option.text = "Please choose appliance first!";
      option.value = "invalid";
      brand.add(option, null);
  }
});
