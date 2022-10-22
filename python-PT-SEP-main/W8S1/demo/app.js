// alert('Hello');

let container = document.querySelector('.container');
fetch('https://digimon-api.vercel.app/api/digimon')
  .then(res => res.json())
  .then(digimons => {
    digimons.forEach(digimon => {
      appendDigimon(container, digimon);
    });
  })
  .catch();

function appendDigimon(container, digi) {
  let div = document.createElement('div');
  div.classList.add('card');
  let name = document.createElement('p');
  let img = document.createElement('img');
  let level = document.createElement('p');
  img.src = digi.img;
  level.textContent = digi.level;
  name.textContent = digi.name;
  div.appendChild(name);
  div.appendChild(img);
  div.appendChild(level);
  container.append(div);
}
