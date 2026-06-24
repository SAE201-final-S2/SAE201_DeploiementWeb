document.getElementById("region").addEventListener("change", async (e) => {
  const regionId = e.target.value;
  const selectDept = document.getElementById("departement");
  
  selectDept.innerHTML = '<option value="">-- Choisir --</option>';
  
  if (!regionId) return;
  
  const response = await fetch(`${BASE_URL}/api/departements/${regionId}`);
  const depts = await response.json();
  
  for (const dept of depts) {
    const opt = document.createElement("option");
    opt.value = dept.code;
    opt.textContent = `${dept.code} – ${dept.libelle}`;
    selectDept.appendChild(opt);
  }
});

// ── Graphique évolution (page effectifs uniquement) ──────
const canvas = document.getElementById("chartEvolution");
if (canvas) {
  new Chart(canvas, {
    type: 'bar',
    data: {
      labels: window.CHART_LABELS,
      datasets: [{
        label: 'Effectif',
        data: window.CHART_DATA,
        backgroundColor: '#2E74B5',
        borderRadius: 6,
        borderSkipped: false
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { display: false }
      },
      scales: {
        y: {
          beginAtZero: false,
          grid: { color: 'rgba(0,0,0,.05)' },
          ticks: { font: { size: 11 } }
        },
        x: {
          grid: { display: false },
          ticks: { font: { size: 11 } }
        }
      }
    }
  });
  // ── Graphique top professions (page data) ────────────────
const canvasTop = document.getElementById("chartTop");
if (canvasTop) {
    new Chart(canvasTop, {
        type: 'bar',
        data: {
            labels: window.TOP_LABELS,
            datasets: [{
                label: 'Effectif',
                data: window.TOP_DATA,
                backgroundColor: '#2E74B5',
                borderRadius: 6,
                borderSkipped: false
            }]
        },
        options: {
            responsive: true,
            plugins: { legend: { display: false } },
            scales: {
                y: { beginAtZero: false, grid: { color: 'rgba(0,0,0,.05)' } },
                x: { grid: { display: false } }
            }
        }
    });
}

// ── Graphique pie répartition (page data) ────────────────
const canvasPie = document.getElementById("chartPie");
if (canvasPie) {
    new Chart(canvasPie, {
        type: 'doughnut',
        data: {
            labels: window.PIE_LABELS,
            datasets: [{
                data: window.PIE_DATA,
                backgroundColor: [
                    '#2E74B5', '#1f9e75', '#e05c2a',
                    '#8b5cf6', '#f59e0b'
                ],
                borderWidth: 2,
                borderColor: '#fff'
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: { font: { size: 11 }, padding: 16 }
                }
            }
        }
    });
}

}
