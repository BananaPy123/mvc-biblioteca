document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('magicParticles');
    const types = ['firefly', 'leaf', 'petal'];
    const symbols = {
        firefly: '•',
        leaf: '🍃',
        petal: '🌸'
    };

    // Cria 30 partículas
    for (let i = 0; i < 30; i++) {
        setTimeout(() => {
            const particle = document.createElement('div');
            const type = types[Math.floor(Math.random() * types.length)];

            // Configurações aleatórias
            const startX = Math.random() * 100;
            const startY = Math.random() * 100;
            const moveX = (Math.random() - 0.5) * 200; // -100 a 100
            const moveY = (Math.random() - 0.5) * 200;
            const rotate = Math.random() * 360;
            const duration = 15 + Math.random() * 20; // 15s a 35s
            const delay = Math.random() * 10;

            particle.className = `particle ${type}`;
            particle.textContent = symbols[type];
            particle.style.cssText = `
          left: ${startX}vw;
          top: ${startY}vh;
          --move-x: ${moveX};
          --move-y: ${moveY};
          --rotate: ${rotate}deg;
          animation: 
            float ${duration}s linear ${delay}s infinite,
            fadeInOut ${5 + Math.random() * 10}s ease-in-out ${delay}s infinite;
        `;

            container.appendChild(particle);
        }, i * 300); // Delay entre partículas
    }
});