timerInput1 = document.getElementById("time1");
buttonRun1 = document.getElementById("rest");
timerShow1 = document.getElementById("timer1");
var timer1, timer2;

function restTimer() {
    let time = parseInt(timerInput1.value)
    if (timerInput1.value == ""){
        alert('Ничего не введено');
        return;
    }
    else if (!Number.isInteger(time) || time <= 0) {
        alert('Некорректный ввод')
        return;
    } 

    let timeMinut = time * 60
    clearInterval(timer1);

    timer1 = setInterval(function () {
        let seconds = timeMinut%60 // Получаем секунды
        let minutes = timeMinut/60%60 // Получаем минуты
        let hour = timeMinut/60/60%60 // Получаем часы
        // Условие если время закончилось то...
        if (timeMinut <= 0) {
            // Таймер удаляется
            clearInterval(timer1);
            // Выводит сообщение что время закончилось
            timerShow1.innerHTML = "";
            soundStart();
            document.title = 'Бот'
        } else { // Иначе
            // Создаём строку с выводом времени
            let strTimer = `${Math.trunc(hour)}:${Math.trunc(minutes)}:${seconds}`;
            // Выводим строку в блок для показа таймера
            timerShow1.innerHTML = strTimer;
            document.title = strTimer
        }
        --timeMinut; // Уменьшаем таймер
    }, 1000)
}

timerInput2 = document.getElementById("time2");
buttonRun2 = document.getElementById("work");
timerShow2 = document.getElementById("timer2");

function workTimer() {
    let time = parseInt(timerInput2.value)
    if (timerInput2.value == ""){
        alert('Ничего не введено');
        return;
    }
    else if (!Number.isInteger(time) || time <= 0) {
        alert('Некорректный ввод')
        return;
    } 

    let timeMinut = time * 60
    clearInterval(timer2);

    timer2 = setInterval(function () {
        let seconds = timeMinut%60 // Получаем секунды
        let minutes = timeMinut/60%60 // Получаем минуты
        let hour = timeMinut/60/60%60 // Получаем часы
        // Условие если время закончилось то...
        if (timeMinut <= 0) {
            // Таймер удаляется
            clearInterval(timer2);
            // Выводит сообщение что время закончилось
            timerShow2.innerHTML = "";
            soundStart();
            document.title = 'Бот'
        } else { // Иначе
            // Создаём строку с выводом времени
            let strTimer = `${Math.trunc(hour)}:${Math.trunc(minutes)}:${seconds}`;
            // Выводим строку в блок для показа таймера
            timerShow2.innerHTML = strTimer;
            document.title = strTimer
        }
        --timeMinut; // Уменьшаем таймер
    }, 1000)
}

function soundStart() {
    let selector = document.getElementById('notices_selector');
    let notices = selector.getElementsByTagName('option');
    let selected_audio = "";
    for (let i = 0; i < notices.length; i++){
        if (notices[i].selected){
            selected_audio = notices[i].innerHTML;
            break;
        }
    }

    audio = document.getElementById('audio_info'); // Создаём новый элемент Audio
    audio.src = "static/notice_sounds/" + selected_audio;
    audio.play();// Автоматически запускаем
}

