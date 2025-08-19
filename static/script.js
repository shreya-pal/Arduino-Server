// This function fetches the data from the API
async function updateSensorValue() {
    try {
        // This calls your existing GET / endpoint!
        const response = await fetch('/');
        // Parse the JSON response from FastAPI
        const data = await response.json();

        // Find the HTML element with id="carVal" and update its content
        document.getElementById('carVal').textContent = data.carVal;
    } catch (error) {
        // Handle any errors (e.g., server down)
        console.error('Failed to fetch data:', error);
        document.getElementById('carVal').textContent = 'Error!';
    }
}

// Call the function immediately when the page loads
updateSensorValue();

// Then set up a timer to call it every 2 seconds to keep the value updated
setInterval(updateSensorValue, 200); // 2000 milliseconds = 2 seconds