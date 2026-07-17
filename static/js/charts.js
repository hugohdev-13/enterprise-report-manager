/**
 * Dashboard chart initialization.
 */
document.addEventListener("DOMContentLoaded", () => {
    initializeReportCharts();
});

/**
 * Initializes every report chart rendered by dashboard templates.
 */
function initializeReportCharts() {
    if (typeof Chart === "undefined") return;

    document
        .querySelectorAll("#reportsChart, #reportsByFormatChart")
        .forEach((canvas) => renderReportChart(canvas));
}

/**
 * Renders a bar chart with values provided through data attributes.
 *
 * @param {HTMLCanvasElement} canvas - Chart canvas element.
 */
function renderReportChart(canvas) {
    const labels = JSON.parse(canvas.dataset.chartLabels || "[]");
    const values = JSON.parse(canvas.dataset.chartValues || "[]");

    new Chart(canvas, {
        type: "bar",
        data: {
            labels,
            datasets: [{
                label: "Reportes",
                data: values,
                backgroundColor: [
                    "#16a34a",
                    "#dc2626",
                    "#2563eb"
                ],
                borderRadius: 10,
                borderSkipped: false
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        precision: 0
                    }
                },
                x: {
                    grid: {
                        display: false
                    }
                }
            }
        }
    });
}