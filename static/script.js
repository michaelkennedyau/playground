const map = L.map('map').setView([0, 0], 2);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19,
  attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

async function fetchData() {
  const res = await fetch('/api/adsb');
  const data = await res.json();
  // expecting data.states from OpenSky API
  if (data.states) {
    data.states.forEach(state => {
      const lat = state[6];
      const lon = state[5];
      if (lat && lon) {
        L.marker([lat, lon]).addTo(map)
          .bindPopup(state[1] || 'aircraft');
      }
    });
  }
}

fetchData();
