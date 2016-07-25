window.onload = socket()
function socket()
{
    var web_socket = new WebSocket('ws://localhost:3398');
    web_socket.onopen() = function(evt)
    {
        onOpen(evt);
    }
    web_socket.onclose()
    {
        ;
    }
    web_socket.onmessage()
    {
        ;
    }
    web_socket.onerror()
    {
        ;
    }
    function onOpen(evt)
    {
        user_id = document.cookie.split(' ')[1];
        alert(user_id);
        web_socket.send("user_id:" + user_id);
    }
}
