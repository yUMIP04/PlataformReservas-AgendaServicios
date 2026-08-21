document.addEventListener('DOMContentLoaded', () =>{

    const contenedor = document.getElementById('contenedor-notificaciones');

    if(!contenedor) return;

    const protocol = window.location.protocol === 'https:' ? 'wss//:' : 'wss//:';
    const socketUrl = `${protocol}${window.location.host}/ws/notificaciones/${idProfesional}/`;

    const socket = new WebSocket();
})