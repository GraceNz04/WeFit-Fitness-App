let timer;
let seconds = 0;

function startExercise() {
    document.getElementById('startBtn').disabled = true;
    document.getElementById('stopBtn').disabled = false;
    timer = setInterval(() => {
        seconds++;
        document.getElementById('timer').innerText = seconds + 's';
    }, 1000);
}

function stopExercise() {
    document.getElementById('startBtn').disabled = false;
    document.getElementById('stopBtn').disabled = true;
    clearInterval(timer);
}