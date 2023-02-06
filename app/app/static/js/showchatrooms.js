const txtArea = document.getElementById('text-area-1');

const btnGET = document.getElementById('btn-get');
const btnPOST = document.getElementById('btn-post');

const urlGET = 'http://127.0.0.1:8000/chatrooms/?format=json';
const urlPOST = 'http://127.0.0.1:8000/chatrooms/';

btnGET.addEventListener("click", () => {
    fetch(urlGET)
        .then(response => response.json())
        .then(json => {
            console.log(json);
            // const data = JSON.parse(json);
            txtArea.value = json;
        });

});

// btnPOST.addEventListener('click', () => {
//     // Настраиваем наш запрос
//     const options = {
//         // Будем использовать метод POST
//         method: 'POST',
//         // Добавим тело запроса
//         body: JSON.stringify({
//             title: 'foo',
//             body: 'bar',
//             userId: 1
//         }),
//         // Дополнительный заголовое с описанием типа данных,
//         // которые мы отправляем серверу. В данном случае
//         // сервер jsonplaceholder будет знать, как ему
//         // обрабатывать запрос
//         headers: {
//             "Content-type": "application/json; charset=UTF-8"
//         }
//     }
//     // Делаем запрос за данными
//     fetch('https://jsonplaceholder.typicode.com/posts', options)
//         .then(response => response.json())
//         .then(json => console.log(json))
// });


//
//
//
//
// // Создаем экзепляр класса XMLHttpRequest
// let xhr = new XMLHttpRequest();
// // Инициализируем запрос
// xhr.open('GET', 'http://127.0.0.1:8000/members/?format=json');
//
// // Добавляем обрабочик ответа сервера
// xhr.onload = function() {
//   if (xhr.status != 200) { // HTTP ошибка?
//     // Если статус не 200 (указывает, что запрос выполнен успешно),
//     // то обрабатываем отдельно
//     chatRooms.innerHTML += ('Статус ответа: ', xhr.status);
//     // console.log('Статус ответа: ', xhr.status);
//   } else {
//     // Ответ мы получаем в формате JSON, поэтому его надо распарсить
//     // console.log('Ответ сервера JSON', xhr.response);
//     let answer = JSON.parse(xhr.response);
//     // Парсим и выводим ответ сервера
//     chatRooms.innerHTML += ('Результат ответа: ', JSON.parse(xhr.response));
//     chatRooms.innerHTML += '\n';
//     for (item in answer) {
//       chatRooms.innerHTML += `<div> ${item.user} ${item.online} </div>`
//
//     };
//     console.log('Результат: ', JSON.parse(xhr.response));
//   }
// };
//
// // Добавляем обрабочик процесса загрузки
// xhr.onprogress = function(event) {
//   // Выведем прогресс загрузки
//  chatRooms.innerHTML += `Загружено ${event.loaded} из ${event.total}\n`
// };
//
// // Добавляем обрабочик ошибки
// xhr.onerror = function() {
//   // обработаем ошибку, не связанную с HTTP (например, нет соединения)
//   chatRooms.innerHTML += ('Статус ответа: ', xhr.status);
//   // console.log('Ошибка! Статус ответа: ', xhr.status);
// };
//
// // Отправляем запрос
// xhr.send();