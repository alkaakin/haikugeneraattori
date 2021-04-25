var wordInput = document.getElementById("value");
var form_el = document.getElementById("value");

form_el.addEventListener("submit", function(evt) {
    evt.preventDefault();
    fillArray();
});

function fillArray() {
    console.log("do something with "+ wordInput.value);
    var out = document.getElementById("out");
    out.innerHTML = "you've entered: " + wordInput.value;
}
