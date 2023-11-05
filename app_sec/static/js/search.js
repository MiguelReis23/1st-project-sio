const searchInput = document.querySelector('#search-input');

searchInput.addEventListener('input', async (event) => {
    const searchTerm = event.target.value;
    const response = await fetch(`/api/products?search=${searchTerm}`);
    const products = await response.json();
    // display the matching products on the page
});
