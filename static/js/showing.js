document.addEventListener('DOMContentLoaded', function(event) {
    let showElement = document.querySelector('.showElement');
    let showBlok = document.querySelector('.showBlok');

    function hideShowBlok() {
        showBlok.classList.add('hidden');
    }

    // Показываем showBlok при клике на showElement
    showElement.addEventListener('click', function() {
        showBlok.classList.toggle('hidden');
    });

    // Скрываем showBlok при клике за его пределами
    document.addEventListener('click', function(event) {
        if (!event.target.closest('.showElement')) {
            hideShowBlok();
        }
    });

    // Скрываем showBlok при загрузке страницы
    hideShowBlok();
});
