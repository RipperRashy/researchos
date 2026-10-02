const fileInput = document.getElementById('fileInput');
const analyzeBtn = document.getElementById('analyzeBtn');
const fileNameDisplay = document.getElementById('fileName');

fileInput.addEventListener('change', () => {
  const file = fileInput.files[0];
  if (file) {
    fileNameDisplay.textContent = 'Selected: ' + file.name;
    analyzeBtn.disabled = false;
  }
});

async function analyzePaper() {
  const file = fileInput.files[0];
  if (!file) return;

  document.getElementById('loader').style.display = 'block';
  document.getElementById('results').style.display = 'none';
  document.getElementById('error').style.display = 'none';
  document.querySelector('.upload-section').style.display = 'none';

  const formData = new FormData();
  formData.append('file', file);

  try {
    const response = await fetch('/analyze', {
      method: 'POST',
      body: formData
    });

    const data = await response.json();

    if (data.error) {
      showError(data.error);
      return;
    }

    document.getElementById('filenameTag').textContent = data.filename;
    document.getElementById('summary').textContent = data.summary || 'Not available.';
    document.getElementById('research_question').textContent = data.analysis.research_question || 'Not available.';
    document.getElementById('methodology').textContent = data.analysis.methodology || 'Not available.';
    document.getElementById('dataset').textContent = data.analysis.dataset || 'Not available.';
    document.getElementById('findings').textContent = data.analysis.findings || 'Not available.';
    document.getElementById('limitations').textContent = data.analysis.limitations || 'Not available.';
    document.getElementById('conclusion').textContent = data.analysis.conclusion || 'Not available.';

    document.getElementById('loader').style.display = 'none';
    document.getElementById('results').style.display = 'block';

  } catch (err) {
    showError('Something went wrong. Make sure the server is running.');
  }
}

function showError(msg) {
  document.getElementById('loader').style.display = 'none';
  document.getElementById('error').style.display = 'block';
  document.getElementById('errorMsg').textContent = msg;
  document.querySelector('.upload-section').style.display = 'block';
}

function resetPage() {
  document.getElementById('results').style.display = 'none';
  document.getElementById('error').style.display = 'none';
  document.querySelector('.upload-section').style.display = 'block';
  fileInput.value = '';
  fileNameDisplay.textContent = '';
  analyzeBtn.disabled = true;
}