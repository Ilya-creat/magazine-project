let busketObject = {
    //name: [количество, цена, id]

}
//myObject['key'] = 'value';
//Object.keys(obj)





document.addEventListener('DOMContentLoaded', function() {
    const addButtons = document.querySelectorAll('.addBusket');
    
    addButtons.forEach(function(button) {
        button.addEventListener('click', function(event) {
            const card = this.closest('.card');
            const value = card.querySelector('.underBlock h1').textContent;
            const name = card.querySelector('.nameProduct').textContent;
            const id = card.querySelector('.nameProduct').id
            console.log("Value:", value);
            console.log("Name:", name);
            console.log("Id:", id);

            if (Object.keys(busketObject).includes(name)) {
                //прибавление к значению в корзине 1
                busketObject[name][0] += 1
                console.log('fe')
            } else{
                //создание нового
                busketObject[name] = [1, value, id];
                console.log('ue')
            }            
            console.log(busketObject)
            event.preventDefault();
        });
    });
});
