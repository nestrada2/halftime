// import clickSoundAsset from "../sounds/click.wav";
// import lightSwitchSoundAsset from "/Volumes/NINO'S SSD 1/Halftime/static/sounds/light_switch";

// const lightSwitch = new Audio(lightSwitchSoundAsset);

let lightModeBtn = document.getElementById("light");
let darkModeBtn = document.getElementById("dark");

lightModeBtn.addEventListener("click", lightMode);
darkModeBtn.addEventListener("click", darkMode);

// Click On - Make Site Light Mode
function lightMode() {
  let body = document.querySelector("body");
  let nav = document.querySelector("nav");
  let footer = document.querySelector("footer");
  let navTitle = document.getElementById("nav-title");
  // let navLinks = document.getElementsByClassName("navbar-item");

  body.classList.remove("dark");
  nav.classList.remove("dark");
  footer.classList.remove("dark");
  navTitle.classList.remove("dark");
  // navLinks.classList.remove("dark");

  sound();
  // lightSwitch.play();

  body.classList.add("light");
  nav.classList.add("light");
  footer.classList.add("light");
  navTitle.classList.add("light");
  // navLinks.classList.add("light");
}

// Click Off - Make Site Dark Mode
function darkMode() {
  let body = document.querySelector("body");
  let nav = document.querySelector("nav");
  let footer = document.querySelector("footer");
  let navTitle = document.getElementById("nav-title");
  // let navLinks = document.querySelector("a");

  body.classList.remove("light");
  nav.classList.remove("light");
  footer.classList.remove("light");
  navTitle.classList.remove("light");
  // navLinks.classList.remove("light");

  body.classList.add("dark");
  nav.classList.add("dark");
  footer.classList.add("dark");
  navTitle.classList.add("dark");
  // navLinks.classList.add("dark");
}

function sound() {
  let snd = new Audio("/static/sounds/light_switch.mp3"); //wav is also supported
  snd.play(); //plays the sound
}

console.log("Hello!");
