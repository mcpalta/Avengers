// movies/static/movies/js/script.js

// Efecto de scroll suave para los enlaces de navegación
document.querySelectorAll('a.nav-link').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        if(this.hash !== "") {
            e.preventDefault();
            const hash = this.hash;
            document.querySelector(hash).scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});

// Aquí puedes agregar más scripts si luego quieres animaciones o efectos
