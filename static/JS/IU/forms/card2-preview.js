/* Card-preview.js */
console.log("Aqui card2-preview");

const name_service = document.querySelector(".input-name-service");
const descript_service = document.querySelector(".input-descripcion-service");
const hora_inicioService = document.querySelector(".input-hora-inicio");
const hora_FinService = document.querySelector(".input-hora-fin");
const tiempoLimite_Service = document.querySelector(".tiempoLimite-select");
const imagen_Service = document.querySelector(".subir-imagen");

const name_service_card = document.querySelector(".Titulo-servicio");
const descripcion_service_card = document.querySelector(".card-descripcion");
const Horario_card = document.querySelector(".horaInicio-card");
const TiempoLimite_card = document.querySelector(".tiempoLimite-card");
const imagen_card = document.querySelector(".imagen-card");

function Llenar_Card(nombre, descripcion, hora_inicio, hora_fin, tiempo_limite, imagen) {
    try {
        /* 🌟 Imagen */
        if (imagen) {
            imagen.addEventListener("change", () => {
                if (imagen.files.length > 0) {
                    const imagen_traducida = URL.createObjectURL(imagen.files[0]);
                    imagen_card.style.backgroundImage = `url('${imagen_traducida}')`;
                    imagen_card.style.backgroundSize = 'cover';
                    imagen_card.style.backgroundPosition = 'top';
                    imagen_card.style.backgroundRepeat = 'no-repeat';
                }
            });
        }

        /* 🌟 Input Nombre */
        if (nombre) {
            nombre.addEventListener("input", () => {
                const valor = nombre.value.trim();
                name_service_card.innerHTML = valor ? valor : 'Titulo Card';
            });
        }

        /* 🌟 Input Descripción */
        if (descripcion) {
            descripcion.addEventListener("input", () => {
                const valor = descripcion.value.trim();
                descripcion_service_card.innerHTML = valor ? valor : 'Descripcion...';
            });
        }

        /* 🌟 Horarios*/
        const actualizarHorario = () => {
            const inicio = hora_inicio ? hora_inicio.value : '';
            const fin = hora_fin ? hora_fin.value : '';

            if (inicio || fin) {
                Horario_card.innerHTML = `Horario: ${inicio} - ${fin}`;
            } else {
                Horario_card.innerHTML = 'Horario:';
            }
        };

        if (hora_inicio) hora_inicio.addEventListener("input", actualizarHorario);
        if (hora_fin) hora_fin.addEventListener("input", actualizarHorario);

        /* 🌟 Tiempo Límite */
        if (tiempo_limite) {
            tiempo_limite.addEventListener("change", () => {
                const valor = tiempo_limite.value;
                TiempoLimite_card.innerHTML = valor ? `Tiempo limite de cita: ${valor}` : 'Tiempo limite de cita';
            });
        }

    } catch (e) {
        console.log(`❌ Hubo un error en el script de vista previa: ${e}`);
    }
}

Llenar_Card(name_service, descript_service, hora_inicioService, hora_FinService, tiempoLimite_Service, imagen_Service);