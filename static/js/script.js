const menuBar = document.getElementById('menu-bar');
const navItems = document.getElementById('nav-items');

menuBar.addEventListener('click', () => {
    navItems.style.display = navItems.style.display === 'flex' ? 'none' : 'flex';
});
