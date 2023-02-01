const roomName = JSON.parse(document.getElementById('room-name').textContent);
const username = JSON.parse(document.getElementById('current-user').textContent);


const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/'
    + roomName
    + '/'
);


function btnSendClicked() {
    if (inputMessage.value) {
        chatSocket.send(JSON.stringify({'username': username, 'message': inputMessage.value}));
        inputMessage.value = '';
    }
    ;
};


document.querySelector('#inputMessage').focus();
document.querySelector('#inputMessage').onkeyup = function (e) {
    if (e.keyCode === 13) {  // enter, return
        btnSendClicked();
    }
};

btnSend.addEventListener('click', btnSendClicked);

chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    if (data.message) {
        const user = data.username;
        const codeText = '<div class="message"><div><p class="name">' + user + '</p><p class="text">' + data.message + '</p></div></div>';
        let chat = document.getElementById('divForMessages');
        chat.innerHTML += codeText;
    }
    ;
};

chatSocket.onclose = function (e) {
    console.error('Chat socket closed unexpectedly');
};

