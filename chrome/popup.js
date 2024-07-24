document.addEventListener('DOMContentLoaded', function() {
    var postalCodeInput = document.getElementById('postal_code');
    var findButton = document.getElementById('findButton');
    var resultElement = document.getElementById('result');
    
    function findNeighbourhood() {
      var postalCode = postalCodeInput.value;
      
      if (postalCode) {
        resultElement.textContent = 'postal code entered'
        fetch(`http://localhost:5000/neighbourhood?postal_code=${postalCode}`)
          .then(response => {
            if (!response.ok) {
              throw new Error('Network response error ' + response.statusText);
            }
            return response.json();
          })
          .then(data => {
            if (data.neighbourhood) {
              resultElement.textContent = `${data.neighbourhood}`;
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
  
    findButton.addEventListener('click', findNeighbourhood);
    
    postalCodeInput.addEventListener('keypress', function(event) {
      if (event.key === 'Enter') {
        findNeighbourhood();
      }
    });
  });
  