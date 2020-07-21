function get_json_data(){
  fetch('./data.json')
  .then(request => request.json())
  .then(data => {
    document.querySelector("#ime_prezime").innerText = "Ime i prezime: " + data.first_name + " " + data.last_name;
    document.querySelector("#mail").innerText = "E-mail: " + data["email"];
    document.querySelector("#telefon").innerText = "Broj telefona: " + data["tel"];
  });
};

document.getElementById("btn").addEventListener("click", get_json_data);