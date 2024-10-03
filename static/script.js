async function analyzeSentiment() {
    const text = document.getElementById('userInput').value;
    const aspect = document.getElementById('aspectInput').value;
    
    // Basic validation
    if (!text.trim() || !aspect.trim()) {
        alert("Please enter both the text and aspect.");
        return;
    }

    // Send the input to the backend API
    const response = await fetch('/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text, aspect }),
    });

    const data = await response.json();
    console.log(data);  // Log the response data

    // Display result
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = `<p>Aspect: ${aspect}</p><p>Sentiment: ${data.sentiment}</p>`;
}
