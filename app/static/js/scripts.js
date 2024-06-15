const mode = document.querySelector(".mode");
const nav = document.querySelector(".navbar");

let style = document.createElement("STYLE")

let modeTheme = localStorage.getItem("theme")

const changeMode = mode =>{
    localStorage.setItem("theme", mode);
    history.pushState("", "changeMode", `?mode=${mode}`)
    modeTheme = localStorage.getItem("theme")
}

const configPrederences = () => {
    modeTheme = localStorage.getItem("theme")
    if (modeTheme == "dark"){
        mode.innerHTML = 'Dark_mode'
        mode.classList.add( 'mode_dark')
        mode.classList.remove('mode_ligth')
        style.innerHTML = `
        body{
            --main-color: #481E14;
            --bg-color: #9B3922;
            --dark-color: #0C0C0C;
            --light-color: #F2613F;
            --item-navbar-color: #A67B5B;
            --light-transparent-color: #fff4;
        }
        .list__link{
            color: var(--dark-color);
        }`
        nav.appendChild(style)
        localStorage.setItem("theme", mode);
    }
}

mode.addEventListener("click", ()=>{
    if (mode.innerHTML == 'Light_mode'){
        mode.innerHTML = 'Dark_mode'
        mode.classList.add( 'mode_dark')
        mode.classList.remove('mode_ligth')
        style.innerHTML = `
        body{
            --main-color: #481E14;
            --bg-color: #9B3922;
            --dark-color: #0C0C0C;
            --light-color: #F2613F;
            --item-navbar-color: #A67B5B;
            --light-transparent-color: #fff4;
        }
        .list__link{
            color: var(--dark-color);
        }`
        nav.appendChild(style)
        changeMode("dark")
    }else{
        mode.innerHTML = 'Light_mode'
        mode.classList.add( 'mode_ligth')
        mode.classList.remove('mode_dark')
        style.innerHTML = `
        body{
            --main-color: #7AB2B2;
            --bg-color: #CDE8E5;
            --dark-color: #2D667C;
            --light-color: #EEF7FF;
            --item-navbar-color: #4D869C;
            --light-transparent-color: #fff4;
        }
        .list__link{
            color: var(--light-color);
        }   `
        nav.appendChild(style)
        changeMode("light")
    }
})


addEventListener("load", configPrederences)