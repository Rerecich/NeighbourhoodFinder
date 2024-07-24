document.addEventListener('DOMContentLoaded', function() {
    var postalCodeInput = document.getElementById('postalCode');
    var findButton = document.getElementById('findButton');
    var resultElement = document.getElementById('result');
  
    function findNeighborhood() {
      var postalCode = postalCodeInput.value;
      
      if (postalCode) {
        fetch(`http://localhost:5000/neighborhood?postal_code=${postalCode}`)
          .then(response => {
            if (!response.ok) {
              throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
          })
          .then(data => {
            if (data.neighborhood) {
              resultElement.textContent = `Neighborhood: ${data.neighborhood}`;
            } else {
              resultElement.textContent = 'Postal code not found.';
            }
          })
          .catch(error => {
            console.error('Fetch error:', error);
            resultElement.textContent = 'Error retrieving data. ' + error.message;
          });
      } else {
        resultElement.textContent = 'Please enter a postal code.';
      }
    }
  
    findButton.addEventListener('click', findNeighborhood);
    
    postalCodeInput.addEventListener('keypress', function(event) {
      if (event.key === 'Enter') {
        findNeighborhood();
      }
    });
  });
  