// Get the modal
var modal = document.getElementById("loginModal");

// Get the anchor tag (Login button)
var btn = document.getElementById("loginBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the anchor tag (Login button), open the modal
btn.onclick = function(event) {
    event.preventDefault(); // Prevent the default anchor link behavior
    modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
