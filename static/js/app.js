document.getElementById('generateBtn').addEventListener('click', generateLyrics);

function generateLyrics() {
    const language = document.getElementById('language').value;
    const genre = document.getElementById('genre').value;  // Now using the selected dropdown value
    const description = document.getElementById('description').value;

    if (!description) {
        alert('Please provide a song description.');
        return;
    }

    const payload = {
        language: language,
        genre: genre,
        description: description
    };

    // Make POST request to Flask backend
    fetch('/generate_lyrics', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById('lyrics').textContent = data.error;
        } else {
            // Remove asterisks from the generated lyrics
            const cleanLyrics = data.lyrics.replace(/\*/g, '');  // Replace all asterisks
            document.getElementById('lyrics').textContent = cleanLyrics;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('lyrics').textContent = 'Error generating lyrics';
    });
}
