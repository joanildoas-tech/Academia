// ====== Timer geral persistente ======
let savedTime = parseInt(localStorage.getItem('tempoTreino')) || 0;
function atualizarTimerGeral() {
    const min = String(Math.floor(savedTime/60)).padStart(2,'0');
    const sec = String(savedTime % 60).padStart(2,'0');
    const el = document.getElementById('timerGeral');
    if(el) el.textContent = `${min}:${sec}`;
}
atualizarTimerGeral();
setInterval(()=>{
    savedTime++;
    localStorage.setItem('tempoTreino', savedTime);
    atualizarTimerGeral();
}, 1000);

// Botão reset timer (para index)
const resetBtn = document.getElementById('resetTimerBtn');
if(resetBtn){
    resetBtn.addEventListener('click', () => {
        savedTime = 0;
        localStorage.setItem('tempoTreino', savedTime);
        atualizarTimerGeral();
    });
}

