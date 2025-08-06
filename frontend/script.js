
function getInputValue(){
    const input = document.getElementById('artist-input');
    const value = input.value;
    console.log("Artist entered:", value);
}

const button = document.getElementById('search-button');

button.addEventListener('click', () => {
    getInputValue();
})
