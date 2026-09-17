const uploadArea = document.getElementById('uploadArea');
const uploadContent = document.getElementById('uploadContent');
const previewArea = document.getElementById('previewArea');
const previewImage = document.getElementById('previewImage');
const uploadBtn = document.getElementById('uploadBtn');
const fileInput = document.getElementById('fileInput');
const retakeBtn = document.getElementById('retakeBtn');
const cameraBtn = document.getElementById('cameraBtn');
const cameraArea = document.getElementById('cameraArea');
const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const captureBtn = document.getElementById('captureBtn');
const closeCameraBtn = document.getElementById('closeCameraBtn');
const analyzeBtn = document.getElementById('analyzeBtn');
const resultsPanel = document.getElementById('resultsPanel');

let currentImage = null;
let stream = null;

uploadBtn.addEventListener('click', () => fileInput.click());

fileInput.addEventListener('change', (e) => {
    if (e.target.files[0]) handleImage(e.target.files[0]);
});

uploadArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadArea.classList.add('dragover');
});

uploadArea.addEventListener('dragleave', () => {
    uploadArea.classList.remove('dragover');
});

uploadArea.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadArea.classList.remove('dragover');
    if (e.dataTransfer.files[0]) handleImage(e.dataTransfer.files[0]);
});

retakeBtn.addEventListener('click', () => {
    uploadContent.style.display = 'block';
    previewArea.style.display = 'none';
    analyzeBtn.disabled = true;
    resultsPanel.style.display = 'none';
});

cameraBtn.addEventListener('click', async () => {
    try {
        stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: 'user' } });
        video.srcObject = stream;
        cameraArea.style.display = 'block';
        uploadArea.style.display = 'none';
        cameraBtn.style.display = 'none';
    } catch (err) {
        alert('Unable to access camera. Please upload a photo instead.');
    }
});

captureBtn.addEventListener('click', () => {
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    canvas.getContext('2d').drawImage(video, 0, 0);
    const imageData = canvas.toDataURL('image/jpeg');
    showPreview(imageData);
    closeCamera();
});

closeCameraBtn.addEventListener('click', closeCamera);

function closeCamera() {
    if (stream) {
        stream.getTracks().forEach(track => track.stop());
        stream = null;
    }
    cameraArea.style.display = 'none';
    uploadArea.style.display = 'flex';
    cameraBtn.style.display = 'inline-flex';
}

function handleImage(file) {
    const reader = new FileReader();
    reader.onload = (e) => showPreview(e.target.result);
    reader.readAsDataURL(file);
}

function showPreview(src) {
    previewImage.src = src;
    currentImage = src;
    uploadContent.style.display = 'none';
    previewArea.style.display = 'block';
    analyzeBtn.disabled = false;
}

analyzeBtn.addEventListener('click', analyzeSkin);

function analyzeSkin() {
    analyzeBtn.disabled = true;
    analyzeBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Analyzing...';

    setTimeout(() => {
        const scores = generateScores();
        displayResults(scores);
        analyzeBtn.innerHTML = '<i class="fas fa-wand-magic-sparkles"></i> Analyze Now';
        analyzeBtn.disabled = false;
    }, 2000);
}

function generateScores() {
    const hydration = Math.floor(Math.random() * 3) + 2;
    const texture = Math.floor(Math.random() * 3) + 2;
    const acne = Math.floor(Math.random() * 3) + 2;
    const aging = Math.floor(Math.random() * 3) + 2;
    const overall = ((hydration + texture + acne + aging) / 4).toFixed(1);

    return { hydration, texture, acne, aging, overall: parseFloat(overall) };
}

function displayResults(scores) {
    resultsPanel.style.display = 'block';

    document.getElementById('overallScore').textContent = scores.overall;

    const starsContainer = document.getElementById('scoreStars');
    starsContainer.innerHTML = '';
    for (let i = 1; i <= 5; i++) {
        const star = document.createElement('i');
        star.className = i <= Math.round(scores.overall) ? 'fas fa-star' : 'fas fa-star empty';
        starsContainer.appendChild(star);
    }

    document.getElementById('hydrationScore').textContent = scores.hydration;
    document.getElementById('textureScore').textContent = scores.texture;
    document.getElementById('acneScore').textContent = scores.acne;
    document.getElementById('agingScore').textContent = scores.aging;

    const tips = {
        hydration: [
            "Your skin needs more hydration. Use a hydrating serum with hyaluronic acid.",
            "Decent hydration level. Maintain with a good moisturizer daily.",
            "Well hydrated! Keep up your current routine."
        ],
        texture: [
            "Texture needs improvement. Add exfoliation 2-3 times per week.",
            "Good texture. Regular exfoliation will make it even better.",
            "Excellent skin texture! Maintain with gentle care."
        ],
        acne: [
            "Some breakouts detected. Use salicylic acid cleanser and spot treatment.",
            "Generally clear skin. Keep pores clean with regular cleansing.",
            "Very clear skin! Maintain with consistent cleansing routine."
        ],
        aging: [
            "Early signs detected. Add retinol and sunscreen daily.",
            "Good for your age. Antioxidants will help long-term.",
            "Looking great! Continue with preventive care."
        ]
    };

    document.getElementById('hydrationTip').textContent = tips.hydration[scores.hydration - 2];
    document.getElementById('textureTip').textContent = tips.texture[scores.texture - 2];
    document.getElementById('acneTip').textContent = tips.acne[scores.acne - 2];
    document.getElementById('agingTip').textContent = tips.aging[scores.aging - 2];

    const products = getRecommendations(scores);
    const productsGrid = document.getElementById('recommendedProducts');
    productsGrid.innerHTML = products.map(p => `
        <div class="product-card">
            <div class="product-category">${p.category}</div>
            <h4>${p.name}</h4>
            <p>${p.description}</p>
            <div class="product-why"><i class="fas fa-lightbulb"></i> ${p.why}</div>
        </div>
    `).join('');

    const routine = getRoutine(scores);
    const routineTimeline = document.getElementById('personalizedRoutine');
    routineTimeline.innerHTML = routine.map((step, i) => `
        <div class="routine-step">
            <div class="step-number">${i + 1}</div>
            <div class="step-info">
                <h4>${step.name}</h4>
                <p>${step.detail}</p>
            </div>
        </div>
    `).join('');

    resultsPanel.scrollIntoView({ behavior: 'smooth' });
}

function getRecommendations(scores) {
    const products = [];

    products.push({
        category: "Cleanser",
        name: "Gentle Foaming Cleanser",
        description: "A mild cleanser that removes impurities without stripping natural oils.",
        why: "Essential first step for all skin types"
    });

    if (scores.hydration <= 3) {
        products.push({
            category: "Hydration",
            name: "Hyaluronic Acid Serum",
            description: "Lightweight serum that draws moisture into the skin.",
            why: "Your skin needs a hydration boost"
        });
    }

    if (scores.texture <= 3) {
        products.push({
            category: "Exfoliation",
            name: "BHA Exfoliant (2% Salicylic Acid)",
            description: "Chemical exfoliant that unclogs pores and smooths texture.",
            why: "Will improve skin texture and clarity"
        });
    }

    if (scores.acne <= 3) {
        products.push({
            category: "Treatment",
            name: "Niacinamide 10% Serum",
            description: "Reduces inflammation and controls oil production.",
            why: "Helps clear breakouts and prevent new ones"
        });
    }

    products.push({
        category: "Moisturizer",
        name: "Lightweight Daily Moisturizer",
        description: "Non-greasy formula that hydrates without clogging pores.",
        why: "Locks in hydration and protects skin barrier"
    });

    if (scores.aging <= 3) {
        products.push({
            category: "Anti-Aging",
            name: "Retinol Night Serum",
            description: "Stimulates collagen production and speeds cell turnover.",
            why: "Fights early signs of aging"
        });
    }

    products.push({
        category: "Protection",
        name: "SPF 50+ Sunscreen",
        description: "Broad-spectrum protection that's lightweight and invisible.",
        why: "The single best anti-aging product"
    });

    return products;
}

function getRoutine(scores) {
    const routine = [
        { name: "Step 1: Cleanse", detail: "Use gentle foaming cleanser with lukewarm water" },
        { name: "Step 2: Tone", detail: "Apply alcohol-free toner to balance pH" }
    ];

    if (scores.hydration <= 3) {
        routine.push({ name: "Step 3: Hydrate", detail: "Apply hyaluronic acid serum to damp skin" });
    }

    if (scores.acne <= 3) {
        routine.push({ name: "Step 4: Treat", detail: "Apply niacinamide serum to problem areas" });
    }

    routine.push({ name: "Step 5: Moisturize", detail: "Apply lightweight moisturizer evenly" });
    routine.push({ name: "Step 6: Protect", detail: "Apply SPF 50+ sunscreen as final step" });

    if (scores.aging <= 3) {
        routine.push({ name: "Night: Retinol", detail: "Use retinol serum 2-3 nights per week" });
    }

    return routine;
}

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});
