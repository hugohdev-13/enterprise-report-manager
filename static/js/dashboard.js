/**
 * Dashboard micro-interactions.
 */
document.addEventListener("DOMContentLoaded", () => {
    animateCounters();
    revealDashboardCards();
});

/**
 * Animates numeric KPI counters.
 */
function animateCounters() {
    document.querySelectorAll(".counter").forEach((counter) => {
        const target = Number(counter.dataset.target || 0);
        const increment = Math.max(1, Math.ceil(target / 50));
        let current = 0;

        if (target <= 0) {
            counter.textContent = "0";
            return;
        }

        function animate() {
            current += increment;

            if (current >= target) {
                counter.textContent = target.toLocaleString();
                return;
            }

            counter.textContent = current.toLocaleString();
            window.requestAnimationFrame(animate);
        }

        animate();
    });
}

/**
 * Reveals dashboard cards with a subtle production-friendly animation.
 */
function revealDashboardCards() {
    const cards = document.querySelectorAll(".reveal-card");

    if (!cards.length) return;

    if (!("IntersectionObserver" in window)) {
        cards.forEach((card) => card.classList.add("is-visible"));
        return;
    }

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (!entry.isIntersecting) return;

            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
        });
    }, { threshold: 0.15 });

    cards.forEach((card) => observer.observe(card));
}