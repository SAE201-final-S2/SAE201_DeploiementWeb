document.addEventListener("DOMContentLoaded", function () {

    let map = L.map('map').setView([46.6, 2.5], 6);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap'
    }).addTo(map);

    let layer;

    function getColor(d) {
        if (!d) return "#ccc";
        if (d > 150) return "#800026";
        if (d > 100) return "#BD0026";
        if (d > 70) return "#E31A1C";
        if (d > 40) return "#FC4E2A";
        if (d > 20) return "#FD8D3C";
        return "#FEB24C";
    }

    function getCode(feature) {
        return (
            feature.properties.code ||
            feature.properties.code_departement ||
            feature.properties.dep ||
            feature.properties.CODE_DEPT
        );
    }

    async function loadGeoJSON() {
        let res = await fetch('/static/data/departements.geojson');
        return await res.json();
    }

    document.getElementById("form-carte").addEventListener("submit", async function (e) {
        e.preventDefault();

        const professionId = document.getElementById("profession").value;
        const annee = document.getElementById("annee").value;
        const statut = document.getElementById("carte-statut");

        if (!professionId) {
            statut.textContent = "Veuillez choisir une profession.";
            return;
        }

        statut.textContent = "Chargement des données… (peut prendre quelques secondes)";

        let geojson = await loadGeoJSON();
        let res = await fetch(`/api/carte?profession_id=${professionId}&annee=${annee}`);
        let data = await res.json();

        let densites = {};
        data.forEach(d => densites[d.code] = d.densite);

        if (layer) map.removeLayer(layer);

        layer = L.geoJSON(geojson, {
            style: function (feature) {
                let d = densites[getCode(feature)];
                return {
                    color: "#333",
                    weight: 1,
                    fillColor: getColor(d),
                    fillOpacity: 0.7
                };
            },
            onEachFeature: function (feature, layer) {
                let code = getCode(feature);
                let d = densites[code];
                layer.bindPopup(
                    "<strong>Département " + code + "</strong><br>" +
                    "Densité : " + (d !== undefined ? d : "Non disponible")
                );
            }
        }).addTo(map);

        statut.textContent = "Carte chargée.";
    });

    // Légende
    let legend = L.control({ position: "bottomright" });
    legend.onAdd = function () {
        let div = L.DomUtil.create("div");
        div.style.background = "white";
        div.style.padding = "8px";
        div.style.border = "1px solid black";
        div.style.fontSize = "14px";
        let grades = [0, 20, 40, 70, 100, 150];
        let colors = ["#FEB24C", "#FD8D3C", "#FC4E2A", "#E31A1C", "#BD0026", "#800026"];
        for (let i = 0; i < grades.length; i++) {
            div.innerHTML +=
                '<div style="display:flex; align-items:center;">' +
                '<div style="width:18px; height:18px; background:' + colors[i] + '; margin-right:5px;"></div>' +
                grades[i] + (grades[i + 1] ? " - " + grades[i + 1] : "+") +
                "</div>";
        }
        return div;
    };
    legend.addTo(map);
});