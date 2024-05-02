// Obtener una referencia al elemento canvas del DOM
const $grafica = document.querySelector("#grafica");

// Configurar el tamaño del canvas según el tamaño especificado en el HTML

// Las etiquetas son las que van en el eje X. 
const etiquetas = ["SUPERIOR", "ALTO", "MEDIO", "BAJO"]
// Podemos tener varios conjuntos de datos. Comencemos con uno
const datosVentas2020 = {
    label: "Porcentaje de resultados en las Pruebas Saber 11 del año 2022 - Pasto",
    data: [15.46, 23.71, 49.48, 11.34], // La data es un arreglo que debe tener la misma cantidad de valores que la cantidad de etiquetas
    backgroundColor: 'white', // Nuevo color de fondo más verde
    borderColor: 'black', // Nuevo color del borde más verde
    borderWidth: 1,// Ancho del borde
};

new Chart($grafica, {
    type: 'bar',// Tipo de gráfica
    data: {
        labels: etiquetas,
        datasets: [
            datosVentas2020,
            // Aquí más datos...
        ]
    },
    options: {
        plugins: {
            legend: {
                
                labels: {
                    font: {
                        size: 21, // Tamaño del texto de la leyenda aumentado a 21px
                    }
                }
            }
        },
        scales: {
            y: {
                ticks: {
                    beginAtZero: true,
                    font: {
                        size: 25, // Tamaño del texto del eje Y aumentado a 25px
                    },
                    color: 'black' // Color del texto del eje Y negro puro
                }
            },
            x: { // Añadir configuración para el eje X (etiquetas)
                ticks: {
                    font: {
                        size: 20, // Tamaño del texto del eje X aumentado a 20px
                    },
                    color: 'black' // Color del texto del eje X negro puro
                }
            }
        },
    }
});
