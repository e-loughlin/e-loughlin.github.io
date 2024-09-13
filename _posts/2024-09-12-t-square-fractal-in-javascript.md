---
title: "T-Square Fractal in Javascript"
tags:
  - Engineering
header:
  teaser: /assets/images/2024-09-12-t-square-fractal-in-javascript/img01.png
  og_image: /assets/images/2024-09-12-t-square-fractal-in-javascript/img01.png
toc: true
toc_sticky: true
---

Just a fun visual demonstration of a [T-Square Fractal](https://en.wikipedia.org/wiki/T-square_(fractal)). You can update the range of RGB values through which the squares will be generated.

{% raw %}
<head>
    <title>T-Square Fractal</title>
    <style>

        canvas {
            background-color: white;
            margin-top: 20px;
            border: 1px solid black;
        }

        .controls {
            text-align: center;
            margin-bottom: 20px;
        }

        .color-slider {
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 10px 0;
        }

        .slider-container {
            width: 300px;
            position: relative;
        }

        .slider {
            width: 100%;
        }

        .slider-label {
            width: 60px;
        }

        .range-label {
            margin-left: 10px;
            width: 100px;
        }
    </style>
</head>
<body>
    <div class="controls">
        <!-- Sliders for Red -->
        <div class="color-slider">
            <label class="slider-label">R:</label>
            <div class="slider-container">
                <input type="range" id="minR" class="slider" value="10" min="0" max="255">
                <input type="range" id="maxR" class="slider" value="20" min="0" max="255">
            </div>
            <span class="range-label" id="rangeR">10 - 20</span>
        </div>

        <!-- Sliders for Green -->
        <div class="color-slider">
            <label class="slider-label">G:</label>
            <div class="slider-container">
                <input type="range" id="minG" class="slider" value="30" min="0" max="255">
                <input type="range" id="maxG" class="slider" value="30" min="0" max="255">
            </div>
            <span class="range-label" id="rangeG">30 - 30</span>
        </div>

        <!-- Sliders for Blue -->
        <div class="color-slider">
            <label class="slider-label">B:</label>
            <div class="slider-container">
                <input type="range" id="minB" class="slider" value="50" min="0" max="255">
                <input type="range" id="maxB" class="slider" value="190" min="0" max="255">
            </div>
            <span class="range-label" id="rangeB">50 - 190</span>
        </div>

        <button id="updateColors">Update Colour Range</button>
    </div>

    <canvas id="fractalCanvas" width="640" height="640" style="display: block; margin: 0 auto;"></canvas>

    <script>
        const canvas = document.getElementById('fractalCanvas');
        const ctx = canvas.getContext('2d');
        const width = canvas.width;
        const height = canvas.height;
        const minSquareSize = 4;
        let squaresToDraw = [];
        let running = true;

        // Get slider elements and range labels
        const minR = document.getElementById('minR');
        const maxR = document.getElementById('maxR');
        const minG = document.getElementById('minG');
        const maxG = document.getElementById('maxG');
        const minB = document.getElementById('minB');
        const maxB = document.getElementById('maxB');

        const rangeR = document.getElementById('rangeR');
        const rangeG = document.getElementById('rangeG');
        const rangeB = document.getElementById('rangeB');

        // Ensure min slider can't exceed max and vice versa
        function updateSliderLimits(minSlider, maxSlider, rangeLabel) {
            if (parseInt(minSlider.value) > parseInt(maxSlider.value)) {
                maxSlider.value = minSlider.value;
            }
            if (parseInt(maxSlider.value) < parseInt(minSlider.value)) {
                minSlider.value = maxSlider.value;
            }
            rangeLabel.textContent = `${minSlider.value} - ${maxSlider.value}`;
        }

        // Add event listeners to handle slider changes
        minR.addEventListener('input', () => updateSliderLimits(minR, maxR, rangeR));
        maxR.addEventListener('input', () => updateSliderLimits(minR, maxR, rangeR));

        minG.addEventListener('input', () => updateSliderLimits(minG, maxG, rangeG));
        maxG.addEventListener('input', () => updateSliderLimits(minG, maxG, rangeG));

        minB.addEventListener('input', () => updateSliderLimits(minB, maxB, rangeB));
        maxB.addEventListener('input', () => updateSliderLimits(minB, maxB, rangeB));

        // Get the user input for RGB ranges
        function getRGBRange() {
            return {
                minR: parseInt(minR.value),
                maxR: parseInt(maxR.value),
                minG: parseInt(minG.value),
                maxG: parseInt(maxG.value),
                minB: parseInt(minB.value),
                maxB: parseInt(maxB.value),
            };
        }

        // Generate a random color within the specified range
        function getRandomColor(rgbRange) {
            const R = Math.floor(Math.random() * (rgbRange.maxR - rgbRange.minR + 1)) + rgbRange.minR;
            const G = Math.floor(Math.random() * (rgbRange.maxG - rgbRange.minG + 1)) + rgbRange.minG;
            const B = Math.floor(Math.random() * (rgbRange.maxB - rgbRange.minB + 1)) + rgbRange.minB;
            return `rgb(${R}, ${G}, ${B})`;
        }

        // Progressive draw queue
        function queueSquare(x, y, size) {
            if (size >= minSquareSize && running) {
                squaresToDraw.push({ x, y, size });

                const newSize = size / 2;
                queueSquare(x - newSize / 2, y - newSize / 2, newSize);
                queueSquare(x + size - newSize / 2, y - newSize / 2, newSize);
                queueSquare(x - newSize / 2, y + size - newSize / 2, newSize);
                queueSquare(x + size - newSize / 2, y + size - newSize / 2, newSize);
            }
        }

        // Draw each square progressively from the queue
        function drawNextSquare(rgbRange) {
            if (squaresToDraw.length > 0 && running) {
                const { x, y, size } = squaresToDraw.shift();
                ctx.fillStyle = getRandomColor(rgbRange);
                ctx.fillRect(x, y, size, size);

                requestAnimationFrame(() => drawNextSquare(rgbRange));
            } else if (running) {
                queueSquare(width / 2 - 100, height / 2 - 100, 200);  // Reset the fractal when finished
            }
        }

        // Start or reset the fractal drawing
        function startFractal() {
            ctx.clearRect(0, 0, width, height);

            const rgbRange = getRGBRange();
            squaresToDraw = [];
            queueSquare(width / 2 - 100, height / 2 - 100, 200);

            drawNextSquare(rgbRange);
        }

        // Handle the update button to reset with new colors
        document.getElementById('updateColors').addEventListener('click', () => {
            startFractal();  // Restart the fractal with updated color ranges
        });

        // Start the fractal initially
        startFractal();
    </script>
</body>
{% endraw %}

