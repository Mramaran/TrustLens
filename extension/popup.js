// Popup Logic
const fileInput = document.getElementById('fileInput');
const dropZone = document.getElementById('dropZone');
const preview = document.getElementById('preview');
const analyzeBtn = document.getElementById('analyzeBtn');
const resultBox = document.getElementById('resultBox');
const resultLabel = document.getElementById('resultLabel');
const confidence = document.getElementById('confidence');
const loading = document.getElementById('loading');
const modelSelect = document.getElementById('modelSelect');
const backBtn = document.getElementById('backBtn');

let selectedFile = null;

// Handle File Selection
fileInput.addEventListener('change', handleFileSelect);

// Handle Drop Zone
dropZone.addEventListener('click', () => fileInput.click());
dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropZone.style.background = 'rgba(37, 130, 246, 0.2)';
});
dropZone.addEventListener('dragleave', () => {
    dropZone.style.background = 'transparent';
});
dropZone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropZone.style.background = 'transparent';
    if (e.dataTransfer.files.length > 0) {
        fileInput.files = e.dataTransfer.files;
        handleFileSelect({ target: fileInput });
    }
});

function handleFileSelect(e) {
    const file = e.target.files[0];
    if (file) {
        selectedFile = file;
        const reader = new FileReader();
        reader.onload = (e) => {
            preview.src = e.target.result;
            preview.style.display = 'block';
            dropZone.style.display = 'none';
            analyzeBtn.disabled = false;
            resultBox.style.display = 'none';
        };
        reader.readAsDataURL(file);
    }
}

// Handle Analyze Click
analyzeBtn.addEventListener('click', async () => {
    if (!selectedFile) return;

    loading.style.display = 'block';
    analyzeBtn.disabled = true;
    resultBox.style.display = 'none';

    try {
        const formData = new FormData();
        formData.append('file', selectedFile);

        // Ensure the API is running locally
        const response = await fetch(`http://127.0.0.1:8000/analyze?model=${modelSelect.value}`, {
            method: 'POST',
            body: formData
        });

        if (!response.ok) throw new Error('Analysis failed');

        const data = await response.json();

        // Update UI
        resultLabel.textContent = data.label;
        const confPercent = (data.score * 100).toFixed(2);
        confidence.textContent = `Score: ${confPercent}%`; // Raw score for now

        resultBox.style.display = 'block';

        // Color coding
        if (data.label === 'AI Generated') {
            resultLabel.style.background = 'linear-gradient(135deg, #FF6B6B 0%, #EE5253 100%)';
            resultLabel.style.webkitBackgroundClip = 'text';
            resultLabel.style.webkitTextFillColor = 'transparent';
        } else {
            resultLabel.style.background = 'linear-gradient(135deg, #1DD1A1 0%, #10AC84 100%)';
            resultLabel.style.webkitBackgroundClip = 'text';
            resultLabel.style.webkitTextFillColor = 'transparent';
        }

    } catch (error) {
        console.error(error);
        alert("Error connecting to TrustLens API. Make sure the backend is running!");
    } finally {
        loading.style.display = 'none';
        analyzeBtn.disabled = false;
    }
});

// Handle Back Button
backBtn.addEventListener('click', () => {
    // Reset UI to initial state
    selectedFile = null;
    fileInput.value = '';
    preview.style.display = 'none';
    dropZone.style.display = 'block';
    analyzeBtn.disabled = true;
    resultBox.style.display = 'none';
    loading.style.display = 'none';
});

// Check for image from context menu
chrome.storage.local.get(['analyzableImage'], (result) => {
    if (result.analyzableImage) {
        fetch(result.analyzableImage)
            .then(res => res.blob())
            .then(blob => {
                const file = new File([blob], "context_image.jpg", { type: "image/jpeg" });
                const dataTransfer = new DataTransfer();
                dataTransfer.items.add(file);
                fileInput.files = dataTransfer.files;
                handleFileSelect({ target: fileInput });

                // Clear storage
                chrome.storage.local.remove('analyzableImage');
            });
    }
});
