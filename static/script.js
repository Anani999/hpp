function Predict() {
    room_size = document.getElementById('room_size').value;
    bedrooms = document.getElementById('bedrooms').value;

    fetch('/predict',{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            "room_size":room_size,
            "bedrooms":bedrooms
        })
    })
    .then(response => response.json())
    .then(data => {
        predicted_price = data.predicted_price;
        document.getElementById('show_price').innerText = predicted_price;
    })
}