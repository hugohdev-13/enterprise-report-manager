/**
 * Report list interactions.
 */
document.addEventListener("DOMContentLoaded", () => {
    initializeReportFilters();
    initializeDeleteReportModal();
});

/**
 * Initializes search, filtering and sorting controls.
 */
function initializeReportFilters() {
    const filterForm = document.getElementById("reportFilters");
    const searchInput = document.getElementById("search");

    if (!filterForm || !searchInput) return;

    let searchTimer;

    searchInput.addEventListener("input", () => {
        window.clearTimeout(searchTimer);
        searchTimer = window.setTimeout(() => filterForm.submit(), 450);
    });

    ["formatFilter", "sortBy", "direction"].forEach((id) => {
        const control = document.getElementById(id);

        if (!control) return;

        control.addEventListener("change", () => filterForm.submit());
    });
}

/**
 * Initializes the Bootstrap delete confirmation modal.
 */
function initializeDeleteReportModal() {
    const reportName = document.getElementById("deleteReportName");
    const deleteForm = document.getElementById("deleteReportForm");

    if (!reportName || !deleteForm) return;

    document.querySelectorAll(".delete-report-button").forEach((button) => {
        button.addEventListener("click", () => {
            reportName.textContent = button.dataset.reportName || "";
            deleteForm.action = button.dataset.deleteUrl || "";
        });
    });
}