var map = L.map('map').setView([-33.4489, -70.6693], 13);

L.tileLayer('https://{s}.basemaps.cartocdn.com/{style}/{z}/{x}/{y}{r}.png', {
    attribution: '&copy; <a href="https://carto.com/">Carto</a>',
    subdomains: 'abcd',
    maxZoom: 19,
    style: 'light_all'
}).addTo(map);
        
function redirectToUrl(button) {
    window.location.href = button.getAttribute('data-url');
}

document.addEventListener("DOMContentLoaded", function () {
    var apiKey = 'key'; // Reemplaza con tu clave API
    fetch('/api/recintos/')
        .then(response => response.json())
        .then(data => {
            data.forEach(recinto => {
                var address = recinto.address;
                var url = `https://geocode.maps.co/search?q=${encodeURIComponent(address)}&key=${apiKey}`;
                fetch(url)
                    .then(response => response.json())
                    .then(data => {
                        if (data.length > 0) {
                            var coordinates = data[0];
                            var marker = L.marker([coordinates.lat, coordinates.lon]).addTo(map);
                            marker.bindPopup('<b>' + recinto.name + '</b><br>' + address).openPopup();
                        }
                    });
            });
        });
});
