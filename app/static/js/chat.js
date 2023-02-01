// // const roomName = JSON.parse(document.getElementById('room-name').textContent);
// //
// // const chatSocket = new WebSocket(
// //     'ws://'
// //     + window.location.host
// //     + '/ws/chat/'
// //     + roomName
// //     + '/'
// // );
// //
// // chatSocket.onmessage = function (e) {
// //     const data = JSON.parse(e.data);
// //     document.querySelector('#chat-log').value += (data.message + '\n');
// // };
// //
// // chatSocket.onclose = function (e) {
// //     console.error('Chat socket closed unexpectedly');
// // };
// //
// // document.querySelector('#chat-message-input').focus();
// // document.querySelector('#chat-message-input').onkeyup = function (e) {
// //     if (e.keyCode === 13) {  // enter, return
// //         document.querySelector('#chat-message-submit').click();
// //     }
// // };
// //
// // document.querySelector('#chat-message-submit').onclick = function (e) {
// //     const messageInputDom = document.querySelector('#chat-message-input');
// //     const message = messageInputDom.value;
// //     chatSocket.send(JSON.stringify({
// //         'message': message
// //     }));
// //     messageInputDom.value = '';
// // };
//
//
// code
// from
// room.js
//
// document.querySelector('#inputMessage').focus();
// document.querySelector('#inputMessage').onkeyup = function (e) {
//     if (e.keyCode === 13) {  // enter, return
//         btnSendClicked();
//     }
// };
//
//
// const chatSocket = new WebSocket('ws://' + window.location.host + '/ws/chat/' + roomName + '/');
//
// function btnSendClicked() {
//     if (inputMessage.value) {
//         let username = document.getElementById('curUser');
//         chatSocket.send(JSON.stringify({'username': username.value, 'message': inputMessage.value}));
//         inputMessage.value = '';
//     }
//     ;
// };
//
//
// //
// // const roomName = JSON.parse(document.getElementById('room-name').value);
// //
// //
//
// //
// //
// // btnSend.addEventListener('click', btnSendClicked);
// //
//
// //
// // chatSocket.onmessage = function (e) {
// //     const data = JSON.parse(e.data);
// //     if (data.message) {
// //         let username = document.getElementById('curUser');
// //         let codeText = '<div class="message"><div><p class="name">' + username.value + '</p><p class="text">' + data.message + '</p></div></div>';
// //         let chat = document.getElementById('divForMessages');
// //         chat.innerHTML += codeText;
// //     }
// //     ;
// //
// // };
// //
// // chatSocket.onclose = function (e) {
// //     console.error('Chat socket closed unexpectedly');
// // };
// //
// //
// // document.querySelector('#chat-message-submit').onclick = function (e) {
// //     const messageInputDom = document.querySelector('#chat-message-input');
// //     const message = messageInputDom.value;
// //     chatSocket.send(JSON.stringify({
// //         'message': message
// //     }));
// //     messageInputDom.value = '';
// // };
// //
