// const form = document.querySelector('#gh-form'); 
const container = document.querySelector('.container');

// form.addEventListener('submit', getGit());


async function handleSubmit() { 
    const response = await fetch('https://api.github.com/users/spavlov03')
    const coderData =  await response.json();
    // console.log("coder data",coderData);
    return coderData 
}

async function getGit() { 
    // console.log(handleSubmit());
    // console.log(container);
    // container.append(document.createElement('p'));
    // console.log(createElement(await handleSubmit()));
    container.append(createElement(await handleSubmit()));
}

function createElement(user) { 
    // console.log("TESTTTTTT-----",user);
    let div = document.createElement('div'); 
    let name = document.createElement('p'); 
    let img = document.createElement('img');
    let followers = document.createElement('p')
    img.src = user.avatar_url; 
    img.width = 300;
    img.style.borderRadius = "50px";
    name.textContent = `User login is ${user.login}`;
    followers.textContent = `${user.name} has ${user.followers} followers.`;
    div.appendChild(name); 
    div.appendChild(followers);
    div.appendChild(img); 
    div.style.marginLeft = '50px';
    return div
}