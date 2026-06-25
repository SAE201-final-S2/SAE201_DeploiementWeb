document.addEventListener('DOMContentLoaded', () => {
  const types = window.typesHon || [];
  const n1 = document.getElementById('type_niv1');
  const n2 = document.getElementById('type_niv2');
  const n3 = document.getElementById('type_niv3');
  const hid = document.getElementById('type_honoraire_id');

  function addOption(sel, value, text, selected=false) {
    const o = document.createElement('option');
    o.value = value;
    o.textContent = text;
    if (selected) o.selected = true;
    sel.appendChild(o);
  }

  n1.innerHTML = '';
  addOption(n1, '', '-- Tous --');
  const niv1s = Array.from(new Set(types.map(t => t.niveau_1).filter(Boolean))).sort();
  niv1s.forEach(v => addOption(n1, v, v, false));

  const preN1 = hid.dataset.n1 || '';
  const preN2 = hid.dataset.n2 || '';
  const preN3 = hid.dataset.n3 || '';

  function clearAndDisable(sel) {
    sel.innerHTML = '';
    sel.disabled = true;
  }

  function populateN2(selectedN1, preSelectN2, preSelectN3) {
    clearAndDisable(n2);
    clearAndDisable(n3);
    if (!selectedN1) return;
    const filtered = types.filter(t => t.niveau_1 === selectedN1);
    const niv2s = Array.from(new Set(filtered.map(t => t.niveau_2).filter(Boolean))).sort();
    addOption(n2, '', '-- Tous --');
    if (niv2s.length > 0) {
      niv2s.forEach(v => addOption(n2, v, v));
      n2.disabled = false;
      if (preSelectN2) {
        n2.value = preSelectN2;
        populateN3(preSelectN2, preSelectN3);
      }
    } else {
      const match = types.find(t => t.niveau_1 === selectedN1 && (!t.niveau_2 || t.niveau_2 === null));
      if (match) hid.value = match.id;
    }
  }

  function populateN3(selectedN2, preSelectN3) {
    clearAndDisable(n3);
    const selectedN1 = n1.value;
    if (!selectedN1 || !selectedN2) return;
    const filtered = types.filter(t => t.niveau_1 === selectedN1 && t.niveau_2 === selectedN2);
    const niv3s = Array.from(new Set(filtered.map(t => t.niveau_3).filter(Boolean))).sort();
    addOption(n3, '', '-- Tous --');
    if (niv3s.length > 0) {
      niv3s.forEach(v => addOption(n3, v, v));
      n3.disabled = false;
      if (preSelectN3) {
        n3.value = preSelectN3;
        setHiddenForCurrent();
      }
    } else {
      const match = types.find(t => t.niveau_1 === selectedN1 && t.niveau_2 === selectedN2 && (!t.niveau_3 || t.niveau_3 === null));
      if (match) hid.value = match.id;
    }
  }

  function setHiddenForCurrent() {
    const selectedN1 = n1.value;
    const selectedN2 = n2.value;
    const selectedN3 = n3.value;
    if (!selectedN1) { hid.value = ''; return; }
    const match = types.find(t =>
      t.niveau_1 === selectedN1 &&
      (selectedN2 ? t.niveau_2 === selectedN2 : (!t.niveau_2 || t.niveau_2 === null)) &&
      (selectedN3 ? t.niveau_3 === selectedN3 : (!t.niveau_3 || t.niveau_3 === null))
    );
    hid.value = match ? match.id : '';
  }

  n1.addEventListener('change', (e) => {
    hid.value = '';
    populateN2(e.target.value, '', '');
  });

  n2.addEventListener('change', (e) => {
    hid.value = '';
    populateN3(e.target.value, '');
  });

  n3.addEventListener('change', () => setHiddenForCurrent());

  if (preN1) {
    n1.value = preN1;
    populateN2(preN1, preN2, preN3);
    if (!preN2 && !preN3) {
      const match = types.find(t => t.niveau_1 === preN1 && (!t.niveau_2 || t.niveau_2 === null));
      if (match) hid.value = match.id;
    }
  }
});
