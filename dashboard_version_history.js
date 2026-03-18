(function () {
  const VERSION_FILE = './dashboard.versions.json';
  const currentVersion = document.body.dataset.dashboardVersion || 'unknown';
  const footer = document.querySelector('footer');
  if (!footer) return;

  injectStyles();
  injectFooterControls();

  const modal = document.createElement('div');
  modal.className = 'dashboard-version-modal';
  modal.id = 'dashboardVersionModal';
  modal.setAttribute('aria-hidden', 'true');
  modal.innerHTML = `
    <div class="dashboard-version-dialog" role="dialog" aria-modal="true" aria-labelledby="dashboardVersionTitle">
      <div class="dashboard-version-header">
        <strong id="dashboardVersionTitle">Dashboard version history</strong>
        <button type="button" class="dashboard-version-close" aria-label="Close version history">Close</button>
      </div>
      <div class="dashboard-version-status" id="dashboardVersionStatus">Loading version history…</div>
      <div class="dashboard-version-list" id="dashboardVersionList"></div>
    </div>
  `;
  document.body.appendChild(modal);

  const openBtn = document.getElementById('dashboardVersionBtn');
  const closeBtn = modal.querySelector('.dashboard-version-close');
  const listEl = modal.querySelector('#dashboardVersionList');
  const statusEl = modal.querySelector('#dashboardVersionStatus');

  openBtn.addEventListener('click', async () => {
    modal.classList.add('show');
    modal.setAttribute('aria-hidden', 'false');
    statusEl.textContent = 'Loading version history…';
    listEl.innerHTML = '';
    try {
      const response = await fetch(VERSION_FILE, { cache: 'no-store' });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const data = await response.json();
      renderVersions(Array.isArray(data.versions) ? data.versions : []);
      statusEl.textContent = `Current version: ${currentVersion}`;
    } catch (err) {
      statusEl.textContent = `Unable to load dashboard version history: ${err.message}`;
    }
  });

  closeBtn.addEventListener('click', closeModal);
  modal.addEventListener('click', (event) => {
    if (event.target === modal) closeModal();
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && modal.classList.contains('show')) closeModal();
  });

  function renderVersions(versions) {
    if (!versions.length) {
      listEl.innerHTML = '<div class="dashboard-version-empty">No dashboard versions found.</div>';
      return;
    }
    listEl.innerHTML = versions.map((entry) => {
      const active = entry.version === currentVersion;
      const notes = (entry.notes || []).map((note) => `<li>${escapeHtml(note)}</li>`).join('');
      return `
        <section class="dashboard-version-item${active ? ' active' : ''}">
          <div class="dashboard-version-item-head">
            <div>
              <h3>${escapeHtml(entry.version)} — ${escapeHtml(entry.label || '')}</h3>
              <div class="dashboard-version-item-meta">${active ? 'Currently viewing this version.' : 'Archived dashboard snapshot.'}</div>
            </div>
            <button type="button" data-app-file="${escapeHtml(entry.appFile)}">Open</button>
          </div>
          <ul>${notes}</ul>
        </section>
      `;
    }).join('');

    listEl.querySelectorAll('button[data-app-file]').forEach((button) => {
      button.addEventListener('click', () => {
        const file = button.getAttribute('data-app-file');
        if (file) window.location.href = new URL(file, document.baseURI).href;
      });
    });
  }

  function closeModal() {
    modal.classList.remove('show');
    modal.setAttribute('aria-hidden', 'true');
  }

  function injectFooterControls() {
    const wrap = document.createElement('div');
    wrap.className = 'dashboard-version-footer';
    wrap.innerHTML = `
      <span>Dashboard version:</span>
      <button type="button" id="dashboardVersionBtn">${escapeHtml(currentVersion)}</button>
    `;
    footer.appendChild(wrap);
  }

  function injectStyles() {
    if (document.getElementById('dashboardVersionStyles')) return;
    const style = document.createElement('style');
    style.id = 'dashboardVersionStyles';
    style.textContent = `
      .dashboard-version-footer { margin-top: 12px; display:flex; gap:8px; align-items:center; justify-content:center; flex-wrap:wrap; }
      .dashboard-version-footer button { border:1px solid rgba(120,166,255,0.24); background:rgba(120,166,255,0.12); color:#78a6ff; border-radius:999px; padding:8px 12px; font-weight:700; cursor:pointer; }
      .dashboard-version-modal { position:fixed; inset:0; background:rgba(6,17,32,0.72); display:none; place-items:center; padding:20px; z-index:1000; }
      .dashboard-version-modal.show { display:grid; }
      .dashboard-version-dialog { width:min(760px, 100%); max-height:min(82vh, 900px); overflow:auto; border-radius:24px; background:#101b30; color:#edf4ff; border:1px solid rgba(255,255,255,0.12); box-shadow:0 28px 70px rgba(0,0,0,0.34); padding:20px; }
      .dashboard-version-header { display:flex; justify-content:space-between; gap:12px; align-items:center; margin-bottom:10px; }
      .dashboard-version-close { border:1px solid rgba(255,255,255,0.12); background:rgba(255,255,255,0.04); color:#edf4ff; border-radius:999px; padding:8px 12px; cursor:pointer; }
      .dashboard-version-status { color:#aab8d0; margin-bottom:12px; }
      .dashboard-version-list { display:grid; gap:12px; }
      .dashboard-version-item { border:1px solid rgba(255,255,255,0.1); border-radius:18px; padding:16px; background:rgba(255,255,255,0.03); }
      .dashboard-version-item.active { border-color:rgba(120,166,255,0.35); box-shadow:0 0 0 1px rgba(120,166,255,0.18) inset; }
      .dashboard-version-item-head { display:flex; justify-content:space-between; gap:12px; align-items:flex-start; }
      .dashboard-version-item-head h3 { margin:0 0 4px; font-size:1rem; }
      .dashboard-version-item-head button { border:1px solid rgba(120,166,255,0.24); background:rgba(120,166,255,0.12); color:#78a6ff; border-radius:999px; padding:8px 12px; font-weight:700; cursor:pointer; }
      .dashboard-version-item-meta { color:#aab8d0; font-size:0.92rem; }
      .dashboard-version-item ul { margin:10px 0 0 18px; color:#edf4ff; }
      .dashboard-version-empty { color:#aab8d0; }
    `;
    document.head.appendChild(style);
  }

  function escapeHtml(value) {
    return String(value)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }
})();
