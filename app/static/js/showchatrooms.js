const chatRooms = document.getElementById('chatrooms-output');

let xhr = new XMLHttpRequest();
xhr.open('GET', 'http://127.0.0.1:8000/chatrooms/?format=json');

xhr.onload = function () {
    if (xhr.status != 200) {
        chatRooms.innerHTML += ('Статус ответа: ', xhr.status);
        chatRooms.innerHTML += '\n';
    } else {
        let answer = JSON.parse(xhr.response);
        chatRooms.innerHTML += ('Результат ответа: ', JSON.parse(xhr.response));
        chatRooms.innerHTML += '\n';
        for (item in answer) {
            chatRooms.innerHTML += `<div> ${item.user} ${item.online} </div>`
        };
        console.log('Результат: ', JSON.parse(xhr.response));
    }
};


xhr.onprogress = function (event) {
    chatRooms.innerHTML += `Загружено ${event.loaded} из ${event.total}`;
    chatRooms.innerHTML += ''

};

xhr.onerror = function () {
    chatRooms.innerHTML += ('Статус ответа: ', xhr.status);
};

xhr.send();