/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */

const form = document.querySelector('form');
const resultsDiv = document.getElementById('address-results');
const addressTypeDiv = document.getElementById('parse-type');
const table = document.querySelector('#address-results table');
const tbody = document.querySelector('#address-results tbody');

form.addEventListener('submit', async function(event) {
   event.preventDefault(); 

   const formData = new FormData(form);
   const address = formData.get('address');

   fetch('/api/parse/?address=' + address)
   .then(response => response.json())
   .then(data => {

   table.innerHTML = '';
   resultsDiv.style.display = 'block';

   if (!data.error) {
   
      const { address_components, address_type } = data;

      addressTypeDiv.textContent = address_type;

      let makeTableRow = (component) => {
         const row = document.createElement('tr');
         const addressPart = document.createElement('td');
         const partTag = document.createElement('td');
         addressPart.textContent = component[0];
         partTag.textContent = component[1];
         row.appendChild(addressPart);
         row.appendChild(partTag);
         tbody.appendChild(row);
       }

       Object.entries(address_components).map((component) => {
         makeTableRow(component)
       });

       table.appendChild(tbody);

   } else {
      table.innerHTML = '<p style="color:red;">invalid address, could not parse</p>'
   }

   })
   .catch(error => {
      console.error('Error:', error);
   });
});
