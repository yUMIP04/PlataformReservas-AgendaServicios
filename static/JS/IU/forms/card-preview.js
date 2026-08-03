/*Card-preview.js */
import create_Card from "../components/card-preview.js";

console.log("Aqui card-preview");

const Form_Crear = document.querySelector(".CrearServicio");
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

function Llenar_Card(nombre, descripcion, hora_inicio, hora_fin, tiempo_limite, imagen){

    try{

            /*🌟Imagen */

    imagen.addEventListener("change", (e) =>{
        e.preventDefault();
        console.log("🔥 Evento change detectado en la imagen!");

        if(imagen.files.length > 0){

            console.log(imagen.files);

            const imagen_traducida = URL.createObjectURL(imagen.files[0]);

            console.log(imagen_traducida);
            imagen_card.innerHTML =`<div class="imagen-card w-90 bg-[url(${imagen_traducida})] bg-top bg-cover bg-no-repeat h-40 rounded-sm "></div>`;
        
        }
    })

        /*🌟input nombre */
        nombre.addEventListener("input", (e) =>{
        e.preventDefault();

      const valor_nameservice = nombre.value;

    if (nombre){

        name_service_card.innerHTML= valor_nameservice;
    } else{
        name_service_card.innerHTML = 'Titulo Card';
    }
})

      /*🌟input descripcion */

          descripcion.addEventListener("input", (e) =>{
        e.preventDefault();

      const valor_descripcionservice = descripcion.value;

    if (descripcion){

        descripcion_service_card.innerHTML= valor_descripcionservice;
    } else{
        descripcion_service_card.innerHTML = 'Descripcion...';
    }
})

  /*🌟input horaInicio */
  
          hora_inicio && hora_fin.addEventListener("input", (e) =>{
        e.preventDefault();

      const valor_hora_inicionservice = hora_inicio.value;
      const valor_hora_finservice = hora_fin.value;

    if (hora_inicio && hora_fin){

        Horario_card.innerHTML= `Horario: ${valor_hora_inicionservice} -${valor_hora_finservice}`;
    } else{
        Horario_card.innerHTML = 'Horario:';
    }
    })

    /*🌟TiempoLimite */
    
          tiempo_limite.addEventListener("input", (e) =>{
        e.preventDefault();

      const valor_tiemposervice = tiempo_limite.value;

    if (tiempo_limite){

        TiempoLimite_card.innerHTML= `Tiempo limite de cita: ${valor_tiemposervice}`;
    } else{
        TiempoLimite_card.innerHTML = 'Tiempo limite de cita';
    }
})



    }catch(e){
        console.log(`Hubo un error: ${e}`);
    }

}

Llenar_Card(name_service,descript_service, hora_inicioService, hora_FinService, tiempoLimite_Service, imagen_Service);

/*🌟Funcion crear card */

function Crear_Card(){

    try{

    Form_Crear.addEventListener("submit", (e) =>{
        e.preventDefault();

         const data = new FormData(Form_Crear);
         console.log(data);

         const name_service = data.get('name_service');
         const descript_service = data.get('descrip_service');
         const subir_imagen = data.get('subir-imagen');
         const HoraInicio_service = data.get('HoraInicio_service');
         const HoraFin_service = data.get('HoraFin_service');
         const tiempoLimite_service = data.get('tiempoLimite_service');

         if (name_service && descript_service && subir_imagen && HoraInicio_service && HoraFin_service && tiempoLimite_Service){

            create_Card(name_service, descript_service, subir_imagen, HoraInicio_service, HoraFin_service, tiempoLimite_Service);
            console.log("Se creo una card en diferentes lados");
            window.location.href='/templates/services/lista_servicios.html';
         }
    })

    }catch(e){
        
        console.error(`❌Hubo un error al crear la card en distintos lugares: ${e}`);
    }
}

Crear_Card();