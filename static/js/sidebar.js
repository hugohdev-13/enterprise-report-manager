/**
 * Sidebar collapse behavior.
 */
document.addEventListener("DOMContentLoaded", () => {
    const toggle = document.getElementById("sidebarToggle");
    const sidebar = document.querySelector(".enterprise-sidebar");

    if (!toggle || !sidebar) return;

    const storageKey = "enterpriseSidebarCollapsed";
    const isCollapsed = window.localStorage.getItem(storageKey) === "true";

    document.body.classList.toggle("sidebar-collapsed", isCollapsed);
    toggle.setAttribute("aria-expanded", String(!isCollapsed));

    toggle.addEventListener("click", () => {
        const collapsed = document.body.classList.toggle("sidebar-collapsed");

        window.localStorage.setItem(storageKey, String(collapsed));
        toggle.setAttribute("aria-expanded", String(!collapsed));
    });
});