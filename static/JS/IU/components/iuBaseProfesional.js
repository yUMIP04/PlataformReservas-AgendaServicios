const btn_abrirOpciones = document.querySelector('.btn-abrir');
const ventana_opciones = document.querySelector('.opciones');
const div_btns = document.querySelector('.btns-abrir-cerrar');


/*🌟 Abrir opciones(cerrar sesion, etc) */
function Abrir_Opciones(btn_abrir, ventana_abrir, btns){

    try{
    
        const btn_cerrar = document.createElement("button");
        btn_cerrar.innerHTML= '<i class="bx bx-caret-big-down" /></i>';
        btn_cerrar.classList.add('cursor-pointer');

        btn_abrir.addEventListener("click", (e) => {
            ventana_abrir.classList.add('absolute');
            ventana_abrir.classList.remove('hidden');
            
            btns.removeChild(btn_abrir);

            btns.appendChild(btn_cerrar);
            

        })

        btn_cerrar.addEventListener("click", (e) =>{

            ventana_abrir.classList.add('hidden');
            ventana_abrir.classList.remove('absolute');
            
            btns.removeChild(btn_cerrar);

            btns.appendChild(btn_abrir);

        })
    }catch(e){

        console.error(`Hubo un error al abrir las opciones: ${e}`);

    }
}

Abrir_Opciones(btn_abrirOpciones, ventana_opciones, div_btns);