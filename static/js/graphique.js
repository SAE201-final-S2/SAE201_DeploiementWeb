document.addEventListener("DOMContentLoaded", () => {
    const professionSelect = document.getElementById("profession");
    const departementSelect = document.getElementById("departement");
    const graphContainer = document.getElementById("graph-container");

    // Écouter les changements sur les menus déroulants
    [professionSelect, departementSelect].forEach(select => {
        select?.addEventListener("change", () => {
            const profLibelle = professionSelect.options[professionSelect.selectedIndex]?.dataset.libelle;
            const deptCode = departementSelect.value;
            const deptNom = departementSelect.options[departementSelect.selectedIndex]?.textContent || "";

            // On ne lance le graphique que si les deux informations sont présentes
            if (profLibelle && deptCode) {
                console.log("Tentative de chargement pour :", profLibelle, "Département :", deptCode);
                chargerGraphiqueEvolution(profLibelle, deptCode, deptNom);
            }
        });
    });

    async function chargerGraphiqueEvolution(profession, deptCode, deptNom) {
        try {
            const url = `${BASE_URL}/api/evolution?profession=${encodeURIComponent(profession)}&dept=${deptCode}`;
            const response = await fetch(url);
            const data = await response.json();

            console.log("Données reçues de l'API :", data);

            // Si aucune donnée n'est trouvée par l'API Ameli
            if (!data || data.length === 0) {
                console.warn("Aucune donnée disponible pour cette sélection.");
                if (graphContainer) {
                    graphContainer.style.display = "block"; // On l'affiche quand même pour y mettre un message
                    document.getElementById("plotly-chart").innerHTML = "<p style='color:red; padding:10px;'>Aucune donnée historique trouvée pour cette profession dans ce département.</p>";
                }
                return;
            }

            // Tri chronologique des données pour éviter les graphiques brouillons
            data.sort((a, b) => new Date(a.annee) - new Date(b.annee));

            // Extraction des axes
            const annees = data.map(d => {
                // Si l'année est une date complète (ex: "2021-01-01"), on extrait l'année numérique
                const dateObj = new Date(d.annee);
                return isNaN(dateObj.getFullYear()) ? d.annee : dateObj.getFullYear();
            });
            const effectifs = data.map(d => d.effectif);

            // Définition de la courbe Plotly
            const trace = {
                x: annees,
                y: effectifs,
                type: 'scatter', // Crée une courbe
                mode: 'lines+markers', // Points + lignes
                name: 'Effectif',
                line: { color: '#007bff', width: 3 },
                marker: { size: 8 }
            };

            const layout = {
                title: `Évolution des effectifs : ${profession} (${deptNom})`,
                xaxis: { title: 'Années', tickmode: 'linear' },
                yaxis: { title: 'Nombre de professionnels' },
                margin: { t: 50, b: 50, l: 60, r: 30 }
            };

            if (graphContainer) {
                graphContainer.style.display = "block";
                // Génération effective du graphique Plotly dans la div
                Plotly.newPlot('plotly-chart', [trace], layout);
            }

        } catch (err) {
            console.error("Erreur critique lors de la création du graphique :", err);
        }}})