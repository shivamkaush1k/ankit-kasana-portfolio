const hamburger = document.getElementById("hamburger");
const navLinks = document.getElementById("navLinks");
const menuBackdrop = document.getElementById("menuBackdrop");

// If you want a mobile sliding menu instead of inline nav-links
function toggleMobileMenu() {
    menuBackdrop.classList.toggle("active");
    navLinks.classList.toggle("active");
}

if (hamburger) {
    hamburger.addEventListener("click", toggleMobileMenu);
}

if (menuBackdrop) {
    menuBackdrop.addEventListener("click", toggleMobileMenu);
}

// Add smooth scroll behavior and active nav on scroll
const nav = document.getElementById("nav");
const sections = document.querySelectorAll(".section");
const navLinksAll = document.querySelectorAll(".nav-link");

function setActiveNav() {
    let current = "";

    sections.forEach(section => {
        const rect = section.getBoundingClientRect();
        if (rect.top <= window.innerHeight * 0.35 && rect.bottom >= window.innerHeight * 0.35) {
            current = section.id;
        }
    });

    navLinksAll.forEach(link => {
        link.classList.remove("active");
        if (link.getAttribute("href") === "#" + current) {
            link.classList.add("active");
        }
    });
}

window.addEventListener("scroll", setActiveNav);
window.addEventListener("load", setActiveNav);
