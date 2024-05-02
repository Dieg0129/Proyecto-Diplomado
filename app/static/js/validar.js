// Selecciona todos los campos de entrada
var inputs = document.querySelectorAll('.input');

// Agrega un event listener a cada campo de entrada
inputs.forEach(function(input) {
    input.addEventListener('input', function() {
        // Valida que el valor del campo sea un número con un máximo de 2 caracteres
        var regex = /^\d{0,3}$/;
        
        // Si es el campo de "Puntaje Global", permite hasta 3 números enteros
        if (input.id === "formulario6") {
            regex = /^\d{0,3}$/;
        }
        
        if (!regex.test(input.value)) {
            // Si el valor no cumple con el formato, restablece el valor del campo
            input.value = input.value.slice(0, input.value.length - 1);
        }
    });
});

// Agrega un event listener para detectar las teclas presionadas y habilitar el tabulador
inputs.forEach(function(input, index, array) {
    input.addEventListener('keydown', function(event) {
        // Obtiene el código de la tecla presionada
        var key = event.keyCode || event.charCode;

        // Si se presiona el tabulador
        if (key === 9) {
            // Evita el comportamiento predeterminado del navegador
            event.preventDefault();

            // Enfoca el siguiente campo de entrada, si existe
            if (index < array.length - 1) {
                array[index + 1].focus();
            } else {
                // Si es el último campo, enfoca el primer campo
                array[0].focus();
            }
        }
    });
});
