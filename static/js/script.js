function getHello() {
    const url = 'https://api.covid19api.com/total/dayone/country/kr'
    fetch(url)
    .then(response => response.json())  
    .then(json => {
        console.log(json);
        document.getElementById("demo").innerHTML = JSON.stringify(json)
    })
}
