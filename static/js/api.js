let plate;

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

// License plate recognition
async function PostPlate() {
    console.log("PostPlateData Ready!");
    let secret_key = "sk_6db061527dc1e4d30b42cd2d";
    let c = document.createElement("canvas");
    let img = document.getElementById("image_plate"); //Add image
    c.height = img.naturalHeight;
    c.width = img.naturalWidth;
    let ctx = c.getContext("2d");
    ctx.drawImage(img, 0, 0, c.width, c.height);
    let base64String = c.toDataURL();
    let base64 = base64String.split(",")[1];

    await fetch(
        "https://api.openalpr.com/v3/recognize_bytes?recognize_vehicle=1&country=th&secret_key=" +
        secret_key,
        {
            method: "POST",
            headers: {
                "Content-Type": 'application/json; charset="utf-8"',
            },
            body: base64,
        }
    )
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            const {results} = data;
            var data_res = document.getElementById("response");
            data_res.innerHTML = `<p>Plate: ${results[0].plate}<br>Province ID: ${
                results[0].region.split("-")[1]
            }</p>`;
            plate = results[0].plate;
        });
}

// Face recognition
function PostCheckin() {
    let c = document.createElement("canvas");
    let img = document.getElementById("image"); //Add image
    c.height = img.naturalHeight;
    c.width = img.naturalWidth;
    let ctx = c.getContext("2d");
    ctx.drawImage(img, 0, 0, c.width, c.height);
    let base64String = c.toDataURL();
    let base64 = base64String.split(",")[1];
    let plate_number = "1ขฆคถ"
    const URL = 'http://localhost:8000/api/checkin/'

    fetch(URL, {
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'face_login': base64, 'plate': plate_number}) //JavaScript object of data to POST
    })
        .then(response => {
            return response.json() //Convert response to JSON
        })
        .then(data => {
            console.log(data)
        })
}

function PostCheckout() {
    let c = document.createElement("canvas");
    let img = document.getElementById("image"); //Add image
    c.height = img.naturalHeight;
    c.width = img.naturalWidth;
    let ctx = c.getContext("2d");
    ctx.drawImage(img, 0, 0, c.width, c.height);
    let base64String = c.toDataURL();
    let base64 = base64String.split(",")[1];
    let plate_number = "1ขฆคถ"
    const URL = 'http://localhost:8000/api/checkout/'

    fetch(URL, {
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'face_logout': base64, 'plate': plate_number}) //JavaScript object of data to POST
    })
        .then(response => {
            return response.json() //Convert response to JSON
        })
        .then(data => {
            console.log(data)
        })
}

let plateButton = document.querySelector("#plate");
plateButton.addEventListener("click", PostPlate);

let checkInButton = document.querySelector("#checkin");
checkInButton.addEventListener("click", PostCheckin);

let checkOutButton = document.querySelector("#checkout");
checkOutButton.addEventListener("click", PostCheckout);
