const setCurrentNavBarColor = (navName) => {
    el = document.getElementById(navName)
    el.style.backgroundColor = "#0069d9";
    el.childNodes[0].style.color = "#fff";
    console.log("changement de culeur")
}

console.log("js ok")