const chatRooms = document.getElementById('chatrooms-output');




// Создаем экзепляр класса XMLHttpRequest
let xhr = new XMLHttpRequest();
// Инициализируем запрос
xhr.open('GET', 'http://127.0.0.1:8000/members/?format=json');

// Добавляем обрабочик ответа сервера
xhr.onload = function() {
  if (xhr.status != 200) { // HTTP ошибка?
    // Если статус не 200 (указывает, что запрос выполнен успешно),
    // то обрабатываем отдельно
    chatRooms.innerHTML += ('Статус ответа: ', xhr.status);
    // console.log('Статус ответа: ', xhr.status);
  } else {
    // Ответ мы получаем в формате JSON, поэтому его надо распарсить
    // console.log('Ответ сервера JSON', xhr.response);
    let answer = JSON.parse(xhr.response);
    // Парсим и выводим ответ сервера
    chatRooms.innerHTML += ('Результат ответа: ', JSON.parse(xhr.response));
    chatRooms.innerHTML += '\n';
    for (item in answer) {
      chatRooms.innerHTML += `<div> ${item.user} ${item.online} </div>`

    };
    console.log('Результат: ', JSON.parse(xhr.response));
  }
};

// Добавляем обрабочик процесса загрузки
xhr.onprogress = function(event) {
  // Выведем прогресс загрузки
 chatRooms.innerHTML += `Загружено ${event.loaded} из ${event.total}\n`
};

// Добавляем обрабочик ошибки
xhr.onerror = function() {
  // обработаем ошибку, не связанную с HTTP (например, нет соединения)
  chatRooms.innerHTML += ('Статус ответа: ', xhr.status);
  // console.log('Ошибка! Статус ответа: ', xhr.status);
};

// Отправляем запрос
xhr.send();