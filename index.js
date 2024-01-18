

const activate = document.querySelector('#activate');
const audio = new Audio('https://www.myinstants.com/media/sounds/lightsabre.mp3');

activate.addEventListener('change', () => {
    if (activate.checked) {
        audio.play();
    }
});