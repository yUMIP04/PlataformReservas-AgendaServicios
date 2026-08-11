const btn_CerrarModal = document.querySelector(".btn-cerrar");
const btn_Cita = document.querySelector(".btn-cita");
const div_modal = document.querySelector(".Modal");


function Abrir_Cerrar_Modal(){

    if (btn_CerrarModal){

        try{

            btn_CerrarModal.addEventListener("click", (e) =>{

                div_modal.classList.remove("absolute");
                div_modal.classList.add("hidden");

            })

        }catch(e){

            console.error(`Hubo un error al cerrar el modal: ${e}`);
        }
    }

    if (btn_Cita){

        try{

        
            btn_Cita.addEventListener("click", (e) =>{

                div_modal.classList.remove("hidden");
                div_modal.classList.add("absolute");

            })

            }catch(e){
                console.error(`Hubo un error al abrir el modal: ${e}`);
            }
        
    }

}

Abrir_Cerrar_Modal();