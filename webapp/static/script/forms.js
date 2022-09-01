var i = 0
const forms = document.getElementById("forms")


function addForm() {
    i += 1
    var form = document.createElement("div")
    form.className = "form"
    form.id = `form-${i}`
    forms.appendChild(form)
    form.innerHTML += `
    <div class="bg-white border rounded py-3 px-3 my-3">
    <div class="form-group my-2">
        <label for="appliance-${i}" class="form-control-label">Appliance</label>
        <select name="appliance-${i}" id="appliance-${i}" class="form-control appliance" required>
            <option value="Air-Conditioner">Air-Conditioner</option>
            <option value="Fridge">Fridge</option>
            <option value="Television">Television</option>
            <option value="Washing Machine">Washing Machine</option>
        </select>
    </div>
    
    <div class="form-group my-2">
        <label for="brand-${i}" class="form-control-label">Brand</label>
        <select name="brand-${i}" id="brand-${i}" class="form-control brand" required>
            <option value="Panasonic">Panasonic</option>
            <option value="Electrolux">Electrolux</option>
            <option value="Mitsubishi">Mitsubishi</option>
            <option value="Samsung">Samsung</option>
            <option value="Others">Others</option>
        </select>
    </div>
            
    <div class="form-group my-2">
        <label for="usage-${i}" class="form-control-label">Hours Used (Per Day)</label>
        <input type="number" class="form-control" id="usage-${i}" name="usage-${i}" max="24" min="0" required>
    </div>
    
    <div class="form-group radio my-2">
        <label for="ticks-${i}" class="form-control-label">Efficiency Level</label>
        ${(()=>{
            let output = ""
            for (let j=1; j<6; j++) {
                output += '<div class="form-check">'
                output += '<input class="form-check-input" id="ticks-'+i.toString()+'-'+j.toString()+'" name="ticks-'+i.toString()+'" required="" type="radio" value="'+j.toString()+'">'
                output += '<label class="form-check-label text-success bg-warning rounded ticks" for="ticks-'+i.toString()+'-'+j.toString()+'">'
                output += '✓'.repeat(j)
                output += '</label>'
                output += '</div>'
            }
            return output
        })()}
    </div>
    <div class="remove text-right">
        <button type="button" class="btn btn-danger" onclick= "deleteForm(${i})"><i class="bi bi-file-earmark-minus"></i> Remove</button>
    </div>
    `
    document.getElementById("index").value = i
    window.scrollTo(0, document.body.scrollHeight)
}

function deleteForm(idx){
    forms.removeChild(document.getElementById(`form-${idx}`))
}

function clearForm(){
    window.location.replace(window.location.href);
}

addForm() //addForm() initalise the first form




