// let submit = document.getElementById("submit");
// submit.onclick(() => {
//     const spinner = document.getElementById("spinner");
//     setTimeout(function() {
//       spinner.style.display = 'none';
//     }, 5000); // Set delay to 5 seconds (5000 milliseconds)
// }) 


document.getElementById('myForm').addEventListener('submit' ,(event) => {
    event.preventDefault();

    var card = document.getElementsById('card');
    card.classList.remove('hide'); // Show spinner
});
