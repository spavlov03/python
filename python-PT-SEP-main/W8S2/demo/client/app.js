const form = document.querySelector('#gh-form');
const container = document.querySelector('.container');

form.addEventListener('submit', handleSubmit);

async function handleSubmit(e) {
  e.preventDefault();
  const username = e.target.username.value;
  const res = await fetch(
    'http://localhost:8000/api/followers?' + new URLSearchParams({ username: username }),
  );
  const data = await res.json();
  console.log('FLASK RESPONSE', data);
  container.innerHTML = '';
  data.forEach(user => {
    addFollowers(user);
  });
}

function addFollowers(user) {
  const div = document.createElement('div');
  const img = document.createElement('img');
  img.src = user.avatar_url;
  img.width = 100;
  img.style.borderRadius = '50px';
  div.appendChild(img);
  const a = document.createElement('a');
  a.textContent = user.login;
  a.href = `https://github.com/${user.login}?tab=repositories`;
  a.setAttribute('target', '_blank');
  div.appendChild(a);
  container.appendChild(div);
}
