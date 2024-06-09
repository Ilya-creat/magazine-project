document.addEventListener('DOMContentLoaded', function() {
    const counters = document.querySelectorAll('.pm_counter');
    
    counters.forEach(function(counter) {
        const minusButton = counter.parentElement.querySelector('.minus');
        const plusButton = counter.parentElement.querySelector('.plus');

        minusButton.addEventListener('click', function() {
            let currentValue = parseInt(counter.textContent);
            if (currentValue > 1) {
                counter.textContent = currentValue - 1;
            }
        });

        plusButton.addEventListener('click', function() {
            let currentValue = parseInt(counter.textContent);
            counter.textContent = currentValue + 1;
        });
    });
});
