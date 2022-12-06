
let counter = 0;

function count() {
    counter++;
    document.querySelector('h1').innerHTML = counter;
    
    if (counter % 10 === 0) {
        alert(`The count is now ${counter}.`);
    }
}

document.addEventListener('DOMContentLoaded',function() {
    // update the button text in the DOM - no need to call function
    // onclick is a property of the button
    document.querySelector('button').onclick = count; 
})
