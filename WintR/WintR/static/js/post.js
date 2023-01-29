// Get input-tag input field
let input_tag = document.querySelector('#input-tag');
// Location Online/InPerson checkbox
let input_online = document.querySelector('#img-location');
let location_online = true;
// Location input field
let input_location = document.querySelector('#input-location');
input_location.value="Online";
let _location = "";

// prevent non-alphabetic tags
input_tag.onkeydown = function(event) {
    let c = event.charCode ? event.charCode : event.which;
    // Check for disallowed characters otherwise allow typing
    if(!((65 <= c && c <= 90) || (37 <= c && c <= 40) || c == 16 || c == 20 || c == 17 || c == 9 || c == 8)) event.preventDefault();
}

input_online.onclick = function(event) {
    location_online = !location_online;
    if(location_online)
    {
        input_online.src = "/static/img/internet-access-icon.svg";
        _location = input_location.value;
        input_location.value="Online";
        input_location.setAttribute('readonly', "");
    } else {
        input_online.src = "/static/img/maps-pin-black-icon.svg";
        input_location.value=_location;
        input_location.removeAttribute('readonly');
    }
}