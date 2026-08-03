/*🌟CARD CREADA AL CREAR UN NUEVO SERVICIO */
const div_listadoServicios = document.querySelector(".Servicios");
const Servicios_Catalogo = document.querySelector(".servicios");

console.log("Si funciona card-preview de components");

export default function create_Card(titulo, descripcion, img, hora_inicio, hora_final, tiempo_limite){

    try{

        if(titulo,descripcion,img,hora_inicio,hora_final,tiempo_limite){     

    /*🌟Card General */
    const card = document.createElement("div");
    card.classList.add("card-muestra bg-[#FAFBF5] w-100 h-110 w-max-100 h-max-110 w-min-50 h-min-50 rounded-md ");

    /*🌟Titulo de la Card */
    const div_titulo = document.createElement("div");
    div_titulo.classList.add("titulo-card text-center mt-6 text-[Roboto] text-2xl font-semibold text-[#A19C9C] mb-8")
    const titulo_card = document.createElement("h1");
    titulo_card.classList.add("Titulo-servicio");
    titulo_card.innerHTML = `${titulo}`;
    div_titulo.appendChild(titulo_card);

    /*🌟Descripcion */
    const div_descripcion_card = document.createElement("div");
    div_descripcion_card.classList.add("descripcion-card ml-7 text-[#A19C9C]");
    const descripcion_card = document.createElement("p");
    descripcion_card.classList.add("card-descripcion");
    descripcion_card.innerHTML = `${descripcion}`;
    div_descripcion_card.appendChild(descripcion_card);

    /*🌟Imagen de Fondo */
    const div_img = document.createElement("div");
    div_img.classList.add("contenedor-imagen flex flex-row justify-center mt-2");
    const imagen_fondo = document.createElement("div");
    imagen_fondo.classList.add("imagen-card w-90 bg-[#A19C9C] h-40 rounded-sm");
    imagen_fondo.innerHTML=`${img}`;
    div_img.appendChild(imagen_fondo);

    /*🌟Informacion explicita */
    const div_informacion = document.createElement("div");
    div_informacion.classList.add("informacion-explicita ml-7 mt-2 text-[Roboto] font-bold text-[#A19C9C] ");
    const horario_inicio = document.createElement("p");
    horario_inicio.classList.add("horaInicio-card");
    horario_inicio.innerHTML=`Horario: ${hora_inicio} - ${hora_final}`;
    div_informacion.appendChild(horario_inicio);

    const tiempo_limite_p = document.createElement("p");
    tiempo_limite_p.classList.add("tiempoLimite-card");
    tiempo_limite_p.innerHTML=`${tiempo_limite}`;
    div_informacion.appendChild(tiempo_limite_p);

    /*🌟 Boton de 'Solicitar Cita'*/

    const div_btn = document.createElement("div");
    div_btn.classList.add("btn flex flex-row justify-center mt-6");
    const btn_solicitarCita = document.createElement("input");
    btn_solicitarCita.classList.add("p-3 w-50 text-white rounded-md bg-[#88bda4] hover:bg-[#659287] cursor-pointer hover:text-white transition");
    btn_solicitarCita.type = "submit";
    btn_solicitarCita.value = "Solicitar Cita";
    div_btn.appendChild(btn_solicitarCita);

    /*🌟Union de todo */
    card.appendChild(div_titulo);
    card.appendChild(div_descripcion_card);
    card.appendChild(div_img);
    card.appendChild(div_informacion);
    card.appendChild(div_btn);

    div_listadoServicios.appendChild(card);
    Servicios_Catalogo.appendChild(card);

    console.log("Se creo exitosamento la card en otros lugares");
    } else{

         console.error("No se puedo crear la card");
    }
}catch(e){

    console.error(`Hubo un error al crear la card: ${e}`);
}
}