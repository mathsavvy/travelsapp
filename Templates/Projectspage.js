// For any minor bug fixes and other problems use the below line

'use strict';

// The following code is for creating a new component set up when the plus button is clicked 

var compCount = 1;
var comps = [];

// The following code is to create a component group object on clicking the plus button

function compCreate() {
    
    // Assigning component's primary key value in this page
    var newComp = {}
    newComp.id = compCount;
    newComp.name = '';
    newComp.quantity = 0;

    // Incrementing the primary key for the next component
    compCount++;

    // For pushing the newly created component group into the components array
    comps.push(newComp);

    // Adding the component group in the page
    compAdd(newComp);
}

// The following code is to create a div tag in which the component group will be displayed

function compAdd(comp){

    // Create some DOM objects
    var newCompGroup = document.createElement('div');

    // For the component name text box

    var newCompTextGroup = document.createElement('div');
    var newCompText = document.createElement('input');
    newCompText.setAttribute('placeholder','Component name')
    

    // For the quantity number box

    var newCompQuanGroup = document.createElement('div');
    var newCompQuanRow = document.createElement('div');
    var newCompQuanCol = document.createElement('div');
    var newCompQuanInpGroup = document.createElement('div');
    var newCompQuan = document.createElement('input');
    newCompQuan.setAttribute("type","number");
    newCompQuan.setAttribute("min","0");
    newCompQuan.style.textAlign = "center";
    newCompQuan.id = 'compQuan-' + comp.id;
    newCompQuan.setAttribute("value",comp.quantity);
    // For the remove button 
    
    var newCompRemCol = document.createElement('div');
    var newCompRemInpGroup = document.createElement('div');

    // Assign the default values to the input boxes

    newCompText.innerHTML = comp.name;
    

    // Assign class names to the declared divs

    newCompGroup.className = 'component-group';
    newCompGroup.id = 'comp-' + comp.id;
    
    newCompTextGroup.className = 'form-group';
    newCompText.className = 'form-control';

    newCompQuanGroup.className = 'form-group';
    newCompQuanRow.className = 'row';
    newCompQuanCol.className = 'col-xs-5 col-lg-2';
    newCompQuanInpGroup.className = 'input-group';
    newCompQuan.className = 'form-control';

    newCompRemCol.className = 'col-xs-3';
    newCompRemInpGroup.className = 'input-group';
    
    // The following code is to align the divs

    newCompTextGroup.innerHTML += '<br><label>Component:</label>';
    newCompTextGroup.appendChild(newCompText);
    newCompGroup.appendChild(newCompTextGroup);

    newCompQuanInpGroup.innerHTML += '<span class="input-group-btn"><button type="button" class="btn btn-primary" id="inc-' + comp.id + '" onclick="decrement(event);"><strong>-</strong></button></span>';
    newCompQuanInpGroup.appendChild(newCompQuan);
    newCompQuanInpGroup.innerHTML += '<span class="input-group-btn"><button type="button" class="btn btn-primary" id="dec-' + comp.id + '" onclick="increment(event);"><strong>+</strong></button></span>';
    newCompQuanCol.appendChild(newCompQuanInpGroup);
    newCompQuanRow.appendChild(newCompQuanCol);

    newCompRemInpGroup.innerHTML += '<button class="btn btn-primary" id="remove" onclick="removeComp(event);">Remove</button>';
    newCompRemCol.appendChild(newCompRemInpGroup);

    newCompQuanRow.appendChild(newCompRemCol);
    newCompQuanGroup.innerHTML += '<label>Quantity:</label>';
    newCompQuanGroup.appendChild(newCompQuanRow);
    newCompGroup.appendChild(newCompQuanGroup);

    // Finally to append all these divs to the parent div

    document.getElementById("component-container").appendChild(newCompGroup);
}

// The following code is to remove a component group

function removeComp(event) {

    // Get the n-th div parent node to be deleted in this scenario
    
    var compToDelete = event.target.parentNode.parentNode.parentNode.parentNode.parentNode
    compToDelete.remove();

    // Since we have to change the primary key as a element is deleted
    
    var elementCountId = Number(compToDelete.id.split('-')[1]);
    for (var i = comps.length - 1; i >= 0; --i) {
        if(comps[i].id === elementCountId) {
            notes.splice(i, 1);
            break;
        }
    }
}

// The following code is for incrementing a quantity box in a particular div using the given buttons

function increment(event){
    
    var x = Number(event.target.id.split('-')[1]);

    var y = "compQuan-" + String(x);
    y = String(y);
    var z = document.getElementById(y).value;
    comps[x-1].quantity++;
    z++;
    document.getElementById(y).value = z;
}

// The following code is for decrementing a quatity box in a particular div using the given buttons

function decrement(event){
    
    var x = Number(event.target.id.split('-')[1]);
    var y = "compQuan-" + String(x);
    y = String(y);
    var z = document.getElementById(y).value;
    if(z>0){
        z--;
        comps[x-1].quantity--;
    }
    document.getElementById(y).value = z;
}