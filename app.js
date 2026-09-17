/**
 * REC·ONE — Ultra-Minimal Phone Recommendation Engine
 * Vanilla JavaScript Engine with Interactive Mouse Spotlight Tracking
 */

document.addEventListener('DOMContentLoaded', () => {
  // ==========================================================================
  // 1. TACTILE SPOTLIGHT TRACKER (requestAnimationFrame)
  // ==========================================================================
  let mouseX = window.innerWidth / 2;
  let mouseY = window.innerHeight / 3;
  let isTicking = false;

  const updateSpotlight = () => {
    document.documentElement.style.setProperty('--mouse-x', `${mouseX}px`);
    document.documentElement.style.setProperty('--mouse-y', `${mouseY}px`);
    isTicking = false;
  };

  window.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;

    if (!isTicking) {
      window.requestAnimationFrame(updateSpotlight);
      isTicking = true;
    }
  }, { passive: true });

  // Initial call to set center spotlight
  updateSpotlight();

  // ==========================================================================
  // 2. CURATED SMARTPHONE DATASET (Loaded from data/phones.json)
  // ==========================================================================
  let PHONES = [];

  // ==========================================================================
  // 3. APPLICATION STATE & DOM REFERENCES
  // ==========================================================================
  const state = {
    selectedCategory: 'all',
    activeFilterTags: new Set(),
    searchQuery: '',
    sortBy: 'score-desc',
    comparisonList: [],
    quizAnswers: {
      useCase: null,
      dealbreaker: null,
      budget: null
    },
    currentQuizStep: 1
  };

  const phonesGrid = document.getElementById('phones-grid');
  const searchInput = document.getElementById('phone-search-input');
  const sortSelect = document.getElementById('phone-sort-select');
  const resultCount = document.getElementById('filter-result-count');
  const resetFiltersBtn = document.getElementById('reset-filters-btn');
  const filterChips = document.querySelectorAll('.chip-btn');
  const categoryCards = document.querySelectorAll('.category-card');

  const compareDrawer = document.getElementById('compare-drawer');
  const compareSelectedList = document.getElementById('compare-selected-list');
  const compareCountBadges = document.querySelectorAll('.compare-count-badge');
  const openCompareModalBtn = document.getElementById('open-compare-modal-btn');
  const clearCompareBtn = document.getElementById('clear-compare-btn');
  const compareModal = document.getElementById('compare-modal');
  const specDetailModal = document.getElementById('spec-detail-modal');

  const quizStepIndicators = document.querySelectorAll('.step-indicator');
  const quizSteps = document.querySelectorAll('.quiz-step-content');
  const quizOptionCards = document.querySelectorAll('.quiz-option-card');
  const quizNextBtn = document.getElementById('quiz-next-btn');
  const quizPrevBtn = document.getElementById('quiz-prev-btn');
  const quizResultsView = document.getElementById('quiz-results-view');
  const restartQuizBtn = document.getElementById('restart-quiz-btn');

  // Hero Matchup & Quick Deck References
  const heroMatchupStage = document.getElementById('hero-matchup-stage');
  const matchupPillBtns = document.querySelectorAll('.matchup-pill-btn');
  const heroLaunchMatrixBtn = document.getElementById('hero-launch-matrix-btn');
  const deckPhone1 = document.getElementById('deck-phone-1');
  const deckPhone2 = document.getElementById('deck-phone-2');
  const deckPhone3 = document.getElementById('deck-phone-3');
  const deckCompareSubmitBtn = document.getElementById('deck-compare-submit-btn');
  const deckPresetTags = document.querySelectorAll('.deck-preset-tag');

  let currentHeroMatchup = ['samsung-galaxy-s24-ultra', 'iphone-15-pro-max'];

  const MATCHUP_PRESETS = {
    's24u-vs-15pm': ['samsung-galaxy-s24-ultra', 'iphone-15-pro-max'],
    'op12-vs-iqoo12': ['oneplus-12', 'iqoo-12'],
    'poco-vs-nord': ['poco-f6', 'oneplus-nord-4']
  };

  function renderHeroMatchup(idA, idB) {
    if (!heroMatchupStage || PHONES.length === 0) return;
    const phoneA = PHONES.find(p => p.id === idA) || PHONES[0];
    const phoneB = PHONES.find(p => p.id === idB) || PHONES[1];
    if (!phoneA || !phoneB) return;

    currentHeroMatchup = [phoneA.id, phoneB.id];

    // Check winners for key specs
    const antutuWinA = phoneA.antutu >= phoneB.antutu;
    const batteryWinA = (phoneA.battery.capacityNum || 0) >= (phoneB.battery.capacityNum || 0);

    heroMatchupStage.innerHTML = `
      <div class="matchup-dual-header">
        <div class="matchup-phone-col">
          <span class="matchup-phone-brand">${phoneA.brand}</span>
          <h3 class="matchup-phone-title">${phoneA.name}</h3>
          <span class="matchup-phone-price">${phoneA.priceFormatted || ('₹' + Number(phoneA.price).toLocaleString('en-IN'))}</span>
        </div>
        <div class="matchup-vs-badge">VS</div>
        <div class="matchup-phone-col" style="text-align: right;">
          <span class="matchup-phone-brand">${phoneB.brand}</span>
          <h3 class="matchup-phone-title">${phoneB.name}</h3>
          <span class="matchup-phone-price">${phoneB.priceFormatted || ('₹' + Number(phoneB.price).toLocaleString('en-IN'))}</span>
        </div>
      </div>

      <table class="matchup-metrics-table">
        <tbody>
          <tr>
            <td class="matchup-metric-label">Compute Silicon</td>
            <td class="matchup-val-cell">${phoneA.processor.split('(')[0]}</td>
            <td class="matchup-val-cell" style="text-align: right;">${phoneB.processor.split('(')[0]}</td>
          </tr>
          <tr>
            <td class="matchup-metric-label">AnTuTu Score</td>
            <td class="matchup-val-cell ${antutuWinA ? 'winner' : ''}">${phoneA.antutuFormatted} ${antutuWinA ? '★' : ''}</td>
            <td class="matchup-val-cell ${!antutuWinA ? 'winner' : ''}" style="text-align: right;">${!antutuWinA ? '★ ' : ''}${phoneB.antutuFormatted}</td>
          </tr>
          <tr>
            <td class="matchup-metric-label">Display & Hz</td>
            <td class="matchup-val-cell">${phoneA.display.size} ${phoneA.display.refresh}</td>
            <td class="matchup-val-cell" style="text-align: right;">${phoneB.display.size} ${phoneB.display.refresh}</td>
          </tr>
          <tr>
            <td class="matchup-metric-label">Battery Cell</td>
            <td class="matchup-val-cell ${batteryWinA ? 'winner' : ''}">${phoneA.battery.capacity}</td>
            <td class="matchup-val-cell ${!batteryWinA ? 'winner' : ''}" style="text-align: right;">${phoneB.battery.capacity}</td>
          </tr>
          <tr>
            <td class="matchup-metric-label">Primary Camera</td>
            <td class="matchup-val-cell">${phoneA.camera.main}</td>
            <td class="matchup-val-cell" style="text-align: right;">${phoneB.camera.main}</td>
          </tr>
          <tr>
            <td class="matchup-metric-label">OS / Software</td>
            <td class="matchup-val-cell">${phoneA.os.name}</td>
            <td class="matchup-val-cell" style="text-align: right;">${phoneB.os.name}</td>
          </tr>
        </tbody>
      </table>
    `;
  }

  function initHeroMatchupListeners() {
    matchupPillBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const key = btn.dataset.matchup;
        matchupPillBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        if (MATCHUP_PRESETS[key]) {
          const [idA, idB] = MATCHUP_PRESETS[key];
          renderHeroMatchup(idA, idB);

          if (deckPhone1) deckPhone1.value = idA;
          if (deckPhone2) deckPhone2.value = idB;
          if (deckPhone3) deckPhone3.value = '';
        }
      });
    });

    if (heroLaunchMatrixBtn) {
      heroLaunchMatrixBtn.addEventListener('click', () => {
        const pA = PHONES.find(p => p.id === currentHeroMatchup[0]);
        const pB = PHONES.find(p => p.id === currentHeroMatchup[1]);
        if (pA && pB) {
          state.comparisonList = [pA, pB];
          updateCompareDrawerUI();
          renderPhoneCards();
          openFullCompareModal();
        }
      });
    }
  }

  function populateDeckSelects() {
    if (!deckPhone1 || !deckPhone2 || !deckPhone3 || PHONES.length === 0) return;

    const createOptions = (defaultId, isOptional = false) => {
      let html = isOptional ? `<option value="">+ 3rd Phone (Optional)</option>` : `<option value="">Select Phone...</option>`;
      
      const brands = [...new Set(PHONES.map(p => p.brand))].sort();
      brands.forEach(brand => {
        html += `<optgroup label="${brand}">`;
        PHONES.filter(p => p.brand === brand).forEach(phone => {
          const selected = phone.id === defaultId ? 'selected' : '';
          const price = phone.priceFormatted || ('₹' + Number(phone.price).toLocaleString('en-IN'));
          html += `<option value="${phone.id}" ${selected}>${phone.name} (${price})</option>`;
        });
        html += `</optgroup>`;
      });
      return html;
    };

    deckPhone1.innerHTML = createOptions('samsung-galaxy-s24-ultra');
    deckPhone2.innerHTML = createOptions('iphone-15-pro-max');
    deckPhone3.innerHTML = createOptions('', true);

    const onDeckChange = () => {
      const idA = deckPhone1.value;
      const idB = deckPhone2.value;
      if (idA && idB && idA !== idB) {
        renderHeroMatchup(idA, idB);
      }
    };

    deckPhone1.addEventListener('change', onDeckChange);
    deckPhone2.addEventListener('change', onDeckChange);
  }

  function initDeckEventListeners() {
    if (deckCompareSubmitBtn) {
      deckCompareSubmitBtn.addEventListener('click', () => {
        const id1 = deckPhone1 ? deckPhone1.value : '';
        const id2 = deckPhone2 ? deckPhone2.value : '';
        const id3 = deckPhone3 ? deckPhone3.value : '';

        if (!id1 || !id2) {
          alert('Please select at least two distinct smartphones to compare.');
          return;
        }

        if (id1 === id2 || (id3 && (id3 === id1 || id3 === id2))) {
          alert('Please select different smartphones for each slot.');
          return;
        }

        const selectedIds = [id1, id2];
        if (id3) selectedIds.push(id3);

        state.comparisonList = selectedIds.map(id => PHONES.find(p => p.id === id)).filter(Boolean);
        updateCompareDrawerUI();
        renderPhoneCards();
        openFullCompareModal();
      });
    }

    deckPresetTags.forEach(tag => {
      tag.addEventListener('click', () => {
        const p1 = tag.dataset.p1;
        const p2 = tag.dataset.p2;

        if (deckPhone1) deckPhone1.value = p1;
        if (deckPhone2) deckPhone2.value = p2;
        if (deckPhone3) deckPhone3.value = '';

        renderHeroMatchup(p1, p2);

        const phoneA = PHONES.find(p => p.id === p1);
        const phoneB = PHONES.find(p => p.id === p2);
        if (phoneA && phoneB) {
          state.comparisonList = [phoneA, phoneB];
          updateCompareDrawerUI();
          renderPhoneCards();
          openFullCompareModal();
        }
      });
    });
  }

  // Load phone data from data/phones.json
  async function loadPhonesData() {
    try {
      const response = await fetch('data/phones.json');
      if (!response.ok) throw new Error(`HTTP error: ${response.status}`);
      PHONES = await response.json();
      renderPhoneCards();
      updateCompareDrawerUI();
      populateDeckSelects();
      renderHeroMatchup('samsung-galaxy-s24-ultra', 'iphone-15-pro-max');
      initHeroMatchupListeners();
      initDeckEventListeners();
    } catch (err) {
      console.error('Error loading phones data:', err);
      if (phonesGrid) {
        phonesGrid.innerHTML = `
          <div style="grid-column: 1 / -1; padding: 3rem; text-align: center; border: 1px solid var(--border-light); background-color: var(--bg-card);">
            <h3 style="font-family: var(--font-serif); font-size: 1.5rem; color: var(--text-primary); margin-bottom: 0.5rem;">Failed to load smartphone database</h3>
            <p style="font-size: 0.875rem; color: var(--text-secondary);">Please ensure the web server is running and data/phones.json is accessible.</p>
          </div>
        `;
      }
    }
  }

  loadPhonesData();

  // ==========================================================================
  // 4. FILTERING & SEARCH EVENT LISTENERS
  // ==========================================================================
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      state.searchQuery = e.target.value.toLowerCase().trim();
      renderPhoneCards();
    });
  }

  if (sortSelect) {
    sortSelect.addEventListener('change', (e) => {
      state.sortBy = e.target.value;
      renderPhoneCards();
    });
  }

  if (resetFiltersBtn) {
    resetFiltersBtn.addEventListener('click', () => {
      state.searchQuery = '';
      if (searchInput) searchInput.value = '';
      state.selectedCategory = 'all';
      state.activeFilterTags.clear();
      state.sortBy = 'score-desc';
      if (sortSelect) sortSelect.value = 'score-desc';

      filterChips.forEach(chip => {
        if (chip.dataset.filter === 'all' && chip.dataset.type === 'category') {
          chip.classList.add('active');
        } else {
          chip.classList.remove('active');
        }
      });

      renderPhoneCards();
    });
  }

  filterChips.forEach(chip => {
    chip.addEventListener('click', () => {
      const filterType = chip.dataset.type;
      const filterVal = chip.dataset.filter;

      if (filterType === 'category') {
        document.querySelectorAll('.chip-btn[data-type="category"]').forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        state.selectedCategory = filterVal;
      } else if (filterType === 'spec') {
        if (state.activeFilterTags.has(filterVal)) {
          state.activeFilterTags.delete(filterVal);
          chip.classList.remove('active');
        } else {
          state.activeFilterTags.add(filterVal);
          chip.classList.add('active');
        }
      }

      renderPhoneCards();
    });
  });

  categoryCards.forEach(card => {
    card.addEventListener('click', () => {
      const cat = card.dataset.category;
      state.selectedCategory = cat;

      document.querySelectorAll('.chip-btn[data-type="category"]').forEach(c => {
        if (c.dataset.filter === cat) {
          c.classList.add('active');
        } else {
          c.classList.remove('active');
        }
      });

      renderPhoneCards();

      const explorerSection = document.getElementById('spec-matrix-explorer');
      if (explorerSection) {
        explorerSection.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });

  // ==========================================================================
  // 5. CORE FILTER & RENDER ENGINE
  // ==========================================================================
  function getFilteredPhones() {
    return PHONES.filter(phone => {
      if (state.selectedCategory !== 'all' && phone.category !== state.selectedCategory) {
        return false;
      }

      if (state.searchQuery) {
        const q = state.searchQuery;
        const matchName = phone.name.toLowerCase().includes(q);
        const matchBrand = phone.brand.toLowerCase().includes(q);
        const matchProcessor = phone.processor.toLowerCase().includes(q);
        const matchCategory = phone.categoryName.toLowerCase().includes(q);
        if (!matchName && !matchBrand && !matchProcessor && !matchCategory) {
          return false;
        }
      }

      for (let tag of state.activeFilterTags) {
        if (tag === 'flat-display' && !phone.isFlat) return false;
        if (tag === 'ois' && !phone.hasOIS) return false;
        if (tag === 'headphone-jack' && !phone.hasJack) return false;
        if (tag === 'battery-5000' && phone.battery.capacityNum < 5000) return false;
        if (tag === 'antutu-650k' && phone.antutu < 650000) return false;
        if (tag === 'clean-os' && !phone.isCleanOS) return false;
        if (tag === 'compact' && !phone.isCompact) return false;
      }

      return true;
    }).sort((a, b) => {
      if (state.sortBy === 'score-desc') return b.antutu - a.antutu;
      if (state.sortBy === 'score-asc') return a.antutu - b.antutu;
      if (state.sortBy === 'price-asc') return a.price - b.price;
      if (state.sortBy === 'price-desc') return b.price - a.price;
      if (state.sortBy === 'battery-desc') return b.battery.capacityNum - a.battery.capacityNum;
      return 0;
    });
  }

  function renderPhoneCards() {
    if (!phonesGrid) return;
    const filtered = getFilteredPhones();

    if (resultCount) {
      resultCount.textContent = `Showing ${filtered.length} of ${PHONES.length} curated devices`;
    }

    if (filtered.length === 0) {
      phonesGrid.innerHTML = `
        <div style="grid-column: 1 / -1; padding: 4rem 2rem; text-align: center; border: 1px solid var(--border-light); background-color: var(--bg-card); position: relative; z-index: 2;">
          <div style="font-family: var(--font-mono); font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--text-muted); margin-bottom: 0.5rem;">0 MATCHES FOUND</div>
          <h3 style="font-family: var(--font-serif); font-size: 1.75rem; color: var(--text-primary); margin-bottom: 1rem;">No device satisfies all selected constraints.</h3>
          <p style="font-size: 0.9375rem; color: var(--text-secondary); max-width: 480px; margin: 0 auto 1.5rem auto;">Try removing one of the strict hardware filters (e.g. 3.5mm jack or compact dimensions) to expand results.</p>
          <button class="btn btn-primary btn-sm" id="empty-state-reset-btn">Reset All Filters</button>
        </div>
      `;
      const btn = document.getElementById('empty-state-reset-btn');
      if (btn) {
        btn.addEventListener('click', () => {
          if (resetFiltersBtn) resetFiltersBtn.click();
        });
      }
      return;
    }

    phonesGrid.innerHTML = filtered.map(phone => {
      const isCompared = state.comparisonList.some(item => item.id === phone.id);

      return `
        <article class="phone-card" data-id="${phone.id}">
          <div class="phone-card-top">
            <div>
              <div class="phone-brand-series">${phone.brand} · ${phone.series}</div>
              <h3 class="phone-title">${phone.name}</h3>
            </div>
            <div class="antutu-pill" title="Verified AnTuTu V10 Score">
              ★ ${phone.antutuFormatted}
            </div>
          </div>

          <div class="phone-specs-grid">
            <div class="spec-cell">
              <span class="spec-cell-label">SoC</span>
              <span class="spec-cell-val">${phone.processor.split('(')[0]}</span>
            </div>
            <div class="spec-cell">
              <span class="spec-cell-label">Display</span>
              <span class="spec-cell-val">${phone.display.size} Flat ${phone.display.refresh}</span>
            </div>
            <div class="spec-cell">
              <span class="spec-cell-label">Battery</span>
              <span class="spec-cell-val">${phone.battery.capacity} (${phone.battery.charging.split('(')[0].trim()})</span>
            </div>
            <div class="spec-cell">
              <span class="spec-cell-label">Main Camera</span>
              <span class="spec-cell-val">${phone.camera.main} ${phone.camera.ois ? '(OIS)' : ''}</span>
            </div>
          </div>

          <div class="phone-badges-row">
            ${phone.isFlat ? '<span class="spec-badge highlight">Flat AMOLED</span>' : ''}
            ${phone.hasOIS ? '<span class="spec-badge highlight">Hardware OIS</span>' : ''}
            ${phone.hasJack ? '<span class="spec-badge highlight">3.5mm Jack</span>' : ''}
            ${phone.isCleanOS ? '<span class="spec-badge highlight">Clean OS</span>' : ''}
            ${phone.ipRating ? `<span class="spec-badge">${phone.ipRating}</span>` : ''}
          </div>

          <div class="phone-card-footer">
            <div class="phone-price-tag">
              <span class="tier">${phone.categoryName}</span>
              <span class="amount">${phone.priceFormatted || ('₹' + Number(phone.price).toLocaleString('en-IN'))}</span>
            </div>

            <div class="phone-actions">
              <label class="compare-checkbox-label ${isCompared ? 'selected' : ''}" title="Add to comparison tray">
                <input type="checkbox" data-compare-id="${phone.id}" ${isCompared ? 'checked' : ''}>
                <span>${isCompared ? 'Comparing' : 'Compare'}</span>
              </label>
              <button class="btn btn-outline btn-sm view-spec-btn" data-spec-id="${phone.id}">
                Specs
              </button>
            </div>
          </div>
        </article>
      `;
    }).join('');

    attachCardEventListeners();
  }

  function attachCardEventListeners() {
    document.querySelectorAll('input[data-compare-id]').forEach(checkbox => {
      checkbox.addEventListener('change', (e) => {
        const id = e.target.dataset.compareId;
        const phone = PHONES.find(p => p.id === id);
        if (!phone) return;

        if (e.target.checked) {
          if (state.comparisonList.length >= 3) {
            alert('Comparison tray limit reached. You can compare up to 3 devices simultaneously.');
            e.target.checked = false;
            return;
          }
          if (!state.comparisonList.some(p => p.id === id)) {
            state.comparisonList.push(phone);
          }
        } else {
          state.comparisonList = state.comparisonList.filter(p => p.id !== id);
        }

        updateCompareDrawerUI();
        renderPhoneCards();
      });
    });

    document.querySelectorAll('.view-spec-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const id = btn.dataset.specId;
        const phone = PHONES.find(p => p.id === id);
        if (phone) openSpecModal(phone);
      });
    });
  }

  // ==========================================================================
  // 6. COMPARISON TRAY & DRAWER
  // ==========================================================================
  function updateCompareDrawerUI() {
    const count = state.comparisonList.length;

    compareCountBadges.forEach(badge => {
      badge.textContent = count;
    });

    if (count > 0) {
      if (compareDrawer) compareDrawer.classList.add('open');
    } else {
      if (compareDrawer) compareDrawer.classList.remove('open');
    }

    if (compareSelectedList) {
      compareSelectedList.innerHTML = state.comparisonList.map(phone => `
        <span class="compare-pill-tag">
          ${phone.name}
          <span class="compare-remove-btn" data-remove-compare="${phone.id}" title="Remove">✕</span>
        </span>
      `).join('');

      document.querySelectorAll('[data-remove-compare]').forEach(btn => {
        btn.addEventListener('click', (e) => {
          const id = e.target.dataset.removeCompare;
          state.comparisonList = state.comparisonList.filter(p => p.id !== id);
          updateCompareDrawerUI();
          renderPhoneCards();
        });
      });
    }
  }

  if (clearCompareBtn) {
    clearCompareBtn.addEventListener('click', () => {
      state.comparisonList = [];
      updateCompareDrawerUI();
      renderPhoneCards();
    });
  }

  if (openCompareModalBtn) {
    openCompareModalBtn.addEventListener('click', () => {
      if (state.comparisonList.length === 0) return;
      openFullCompareModal();
    });
  }

  const headerCompareBtn = document.getElementById('header-compare-btn');
  if (headerCompareBtn) {
    headerCompareBtn.addEventListener('click', () => {
      if (state.comparisonList.length === 0) {
        const exp = document.getElementById('spec-matrix-explorer');
        if (exp) exp.scrollIntoView({ behavior: 'smooth' });
      } else {
        openFullCompareModal();
      }
    });
  }

  // ==========================================================================
  // 7. SPEC DETAIL & SIDE-BY-SIDE MODALS
  // ==========================================================================
  function openSpecModal(phone) {
    if (!specDetailModal) return;
    const content = specDetailModal.querySelector('.modal-content-slot');
    if (!content) return;

    content.innerHTML = `
      <div class="spec-modal-header">
        <div class="eyebrow">${phone.brand} · ${phone.series}</div>
        <h2 class="spec-modal-title">${phone.name}</h2>
        <p class="spec-modal-sub">${phone.editorialVerdict}</p>
      </div>

      <div class="spec-sheet-sections">
        <div>
          <div class="spec-sheet-group-title">01 / Compute & Storage</div>
          <table class="spec-table-list">
            <tr><td>Processor (SoC)</td><td>${phone.processor}</td></tr>
            <tr><td>AnTuTu Benchmark</td><td>${phone.antutuFormatted} (~${phone.antutu.toLocaleString()} pts)</td></tr>
            <tr><td>Storage Standard</td><td>${phone.storage}</td></tr>
            <tr><td>OS / Software</td><td>${phone.os.name} (${phone.os.bloatware})</td></tr>
            <tr><td>Support Commitment</td><td>${phone.os.updates}</td></tr>
          </table>
        </div>

        <div>
          <div class="spec-sheet-group-title">02 / Display & Hardware Ergonomics</div>
          <table class="spec-table-list">
            <tr><td>Display Panel</td><td>${phone.display.size} ${phone.display.type}</td></tr>
            <tr><td>Panel Contour</td><td>${phone.isFlat ? '100% Flat Screen (Zero Distortion)' : 'Curved Edge'}</td></tr>
            <tr><td>Refresh Rate</td><td>${phone.display.refresh}</td></tr>
            <tr><td>Peak Luminance</td><td>${phone.display.brightness}</td></tr>
            <tr><td>Chassis Weight</td><td>${phone.weight}</td></tr>
            <tr><td>Ingress Protection</td><td>${phone.ipRating}</td></tr>
          </table>
        </div>

        <div>
          <div class="spec-sheet-group-title">03 / Optics & Acoustic Architecture</div>
          <table class="spec-table-list">
            <tr><td>Primary Optics</td><td>${phone.camera.main}</td></tr>
            <tr><td>Hardware OIS</td><td>${phone.hasOIS ? 'Included (Optical Image Stabilization)' : 'Not Included (EIS Only)'}</td></tr>
            <tr><td>Auxiliary Sensors</td><td>${phone.camera.secondary}</td></tr>
            <tr><td>3.5mm Headphone Jack</td><td>${phone.hasJack ? 'Dedicated 3.5mm Analog Audio Port' : 'No 3.5mm Jack (USB-C / BT Audio)'}</td></tr>
            <tr><td>Speaker Array</td><td>${phone.audio.stereo ? 'Symmetrical Dual Stereo' : 'Single Loudspeaker'}</td></tr>
          </table>
        </div>

        <div>
          <div class="spec-sheet-group-title">04 / Endurance & Power</div>
          <table class="spec-table-list">
            <tr><td>Battery Capacity</td><td>${phone.battery.capacity}</td></tr>
            <tr><td>Wired Charging Rate</td><td>${phone.battery.charging}</td></tr>
            <tr><td>Base Price</td><td>${phone.priceFormatted || ('₹' + Number(phone.price).toLocaleString('en-IN'))}</td></tr>
          </table>
        </div>
      </div>
    `;

    specDetailModal.classList.add('active');
  }

  function openFullCompareModal() {
    if (!compareModal) return;
    const slot = compareModal.querySelector('.modal-content-slot');
    if (!slot) return;

    const list = state.comparisonList;

    slot.innerHTML = `
      <div class="spec-modal-header">
        <div class="eyebrow">Direct Spec Audit</div>
        <h2 class="spec-modal-title">Side-by-Side Hardware Comparison</h2>
        <p class="spec-modal-sub">Objective technical matrix comparing ${list.length} selected daily drivers.</p>
      </div>

      <div style="overflow-x: auto;">
        <table class="compare-matrix-table">
          <thead>
            <tr>
              <th>Spec Parameter</th>
              ${list.map(p => `<th>${p.name}<br><span style="font-weight:400; color:var(--text-muted);">${p.priceFormatted || ('₹' + Number(p.price).toLocaleString('en-IN'))}</span></th>`).join('')}
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>AnTuTu Benchmark</td>
              ${list.map(p => `<td><strong>${p.antutuFormatted}</strong></td>`).join('')}
            </tr>
            <tr>
              <td>Processor</td>
              ${list.map(p => `<td>${p.processor}</td>`).join('')}
            </tr>
            <tr>
              <td>Display Type</td>
              ${list.map(p => `<td>${p.display.size} ${p.display.type} (${p.isFlat ? 'Flat' : 'Curved'})</td>`).join('')}
            </tr>
            <tr>
              <td>Refresh Rate</td>
              ${list.map(p => `<td>${p.display.refresh}</td>`).join('')}
            </tr>
            <tr>
              <td>Battery & Speed</td>
              ${list.map(p => `<td>${p.battery.capacity} <br><span style="color:var(--text-secondary); font-size:0.75rem;">${p.battery.charging}</span></td>`).join('')}
            </tr>
            <tr>
              <td>Main Camera & OIS</td>
              ${list.map(p => `<td>${p.camera.main} <br><strong>${p.hasOIS ? '✓ Hardware OIS' : '✕ EIS Only'}</strong></td>`).join('')}
            </tr>
            <tr>
              <td>3.5mm Headphone Jack</td>
              ${list.map(p => `<td><strong>${p.hasJack ? '✓ Included' : '✕ No 3.5mm Port'}</strong></td>`).join('')}
            </tr>
            <tr>
              <td>Software / OS</td>
              ${list.map(p => `<td>${p.os.name} <br><span style="color:var(--text-secondary); font-size:0.75rem;">${p.os.bloatware}</span></td>`).join('')}
            </tr>
            <tr>
              <td>Update Lifecycle</td>
              ${list.map(p => `<td>${p.os.updates}</td>`).join('')}
            </tr>
            <tr>
              <td>Ingress Protection</td>
              ${list.map(p => `<td>${p.ipRating}</td>`).join('')}
            </tr>
            <tr>
              <td>Chassis Weight</td>
              ${list.map(p => `<td>${p.weight}</td>`).join('')}
            </tr>
          </tbody>
        </table>
      </div>
    `;

    compareModal.classList.add('active');
  }

  document.querySelectorAll('.modal-close-btn, .modal-overlay').forEach(el => {
    el.addEventListener('click', (e) => {
      if (e.target === el || e.target.closest('.modal-close-btn')) {
        document.querySelectorAll('.modal-overlay').forEach(modal => modal.classList.remove('active'));
      }
    });
  });

  // ==========================================================================
  // 8. RECOMMENDATION ENGINE QUIZ
  // ==========================================================================
  quizOptionCards.forEach(card => {
    card.addEventListener('click', () => {
      const step = card.dataset.step;
      const value = card.dataset.value;

      const parentGrid = card.closest('.quiz-options-grid');
      if (parentGrid) {
        parentGrid.querySelectorAll('.quiz-option-card').forEach(c => c.classList.remove('selected'));
      }
      card.classList.add('selected');

      if (step === '1') state.quizAnswers.useCase = value;
      if (step === '2') state.quizAnswers.dealbreaker = value;
      if (step === '3') state.quizAnswers.budget = value;

      if (quizNextBtn) quizNextBtn.disabled = false;
    });
  });

  if (quizNextBtn) {
    quizNextBtn.addEventListener('click', () => {
      if (state.currentQuizStep < 3) {
        state.currentQuizStep++;
        updateQuizStepUI();
      } else {
        calculateQuizRecommendation();
      }
    });
  }

  if (quizPrevBtn) {
    quizPrevBtn.addEventListener('click', () => {
      if (state.currentQuizStep > 1) {
        state.currentQuizStep--;
        updateQuizStepUI();
      }
    });
  }

  if (restartQuizBtn) {
    restartQuizBtn.addEventListener('click', () => {
      state.currentQuizStep = 1;
      state.quizAnswers = { useCase: null, dealbreaker: null, budget: null };
      quizOptionCards.forEach(c => c.classList.remove('selected'));
      if (quizResultsView) quizResultsView.classList.remove('active');
      document.querySelector('.quiz-step-container').style.display = 'block';
      updateQuizStepUI();
    });
  }

  function updateQuizStepUI() {
    quizSteps.forEach(s => {
      if (parseInt(s.dataset.step) === state.currentQuizStep) {
        s.classList.add('active');
      } else {
        s.classList.remove('active');
      }
    });

    quizStepIndicators.forEach((ind, idx) => {
      if (idx + 1 === state.currentQuizStep) {
        ind.classList.add('current');
      } else {
        ind.classList.remove('current');
      }
    });

    if (quizPrevBtn) {
      quizPrevBtn.style.visibility = state.currentQuizStep > 1 ? 'visible' : 'hidden';
    }

    if (quizNextBtn) {
      quizNextBtn.textContent = state.currentQuizStep === 3 ? 'Match Daily Driver' : 'Next Step →';
      let hasAnswer = false;
      if (state.currentQuizStep === 1 && state.quizAnswers.useCase) hasAnswer = true;
      if (state.currentQuizStep === 2 && state.quizAnswers.dealbreaker) hasAnswer = true;
      if (state.currentQuizStep === 3 && state.quizAnswers.budget) hasAnswer = true;
      quizNextBtn.disabled = !hasAnswer;
    }
  }

  function calculateQuizRecommendation() {
    const { useCase, dealbreaker, budget } = state.quizAnswers;

    const scored = PHONES.map(phone => {
      let score = 0;
      let reasons = [];

      if (budget === 'budget' && phone.price <= 30000) { score += 30; reasons.push('Fits your sub-₹30,000 budget parameter.'); }
      if (budget === 'midrange' && phone.price > 25000 && phone.price <= 60000) { score += 30; reasons.push('Optimal price-to-performance tier (₹30K - ₹60K).'); }
      if (budget === 'flagship' && phone.price >= 60000) { score += 30; reasons.push('Uncompromised flagship construction (₹60K+).'); }

      if (dealbreaker === 'flat-screen' && phone.isFlat) { score += 25; reasons.push('Features a 100% distortion-free flat display.'); }
      if (dealbreaker === '35mm-jack' && phone.hasJack) { score += 40; reasons.push('Retains the dedicated 3.5mm analog headphone jack.'); }
      if (dealbreaker === 'clean-os' && phone.isCleanOS) { score += 30; reasons.push('Bloatware-free, ad-free operating system.'); }
      if (dealbreaker === 'ois' && phone.hasOIS) { score += 25; reasons.push('Equipped with hardware Optical Image Stabilization.'); }

      if (useCase === 'gaming' && phone.antutu >= 1200000) { score += 35; reasons.push('Raw AnTuTu > 1.2M score handles heavy sustained gaming.'); }
      if (useCase === 'camera' && (phone.hasOIS || phone.brand === 'Google' || phone.brand === 'Xiaomi' || phone.brand === 'Samsung' || phone.brand === 'Apple' || phone.brand === 'Vivo')) { score += 35; reasons.push('Class-leading optics and natural color calibration.'); }
      if (useCase === 'battery' && phone.battery.capacityNum >= 5000) { score += 35; reasons.push('5000mAh+ high-density battery cell for effortless 2-day endurance.'); }
      if (useCase === 'productivity' && (phone.isCleanOS || phone.isCompact)) { score += 30; reasons.push('Zero notification spam and ergonomic daily workflow.'); }

      return { phone, score, reasons };
    }).sort((a, b) => b.score - a.score);

    const topPick = scored[0];
    const runnerUp = scored[1];

    if (quizResultsView) {
      document.querySelector('.quiz-step-container').style.display = 'none';
      quizResultsView.classList.add('active');

      const resultSlot = document.getElementById('quiz-result-slot');
      if (resultSlot) {
        resultSlot.innerHTML = `
          <div class="result-card-inner">
            <span class="result-match-score">★ 98% Compatibility Match</span>
            <div class="eyebrow">${topPick.phone.brand} · ${topPick.phone.categoryName}</div>
            <h2 class="result-phone-name">${topPick.phone.name}</h2>
            <div class="result-reasoning">
              <strong>Why it matches your profile:</strong>
              <ul style="list-style: square; padding-left: 1.25rem; margin-top: 0.5rem; display: flex; flex-direction: column; gap: 0.25rem;">
                ${topPick.reasons.map(r => `<li>${r}</li>`).join('')}
              </ul>
            </div>

            <div class="phone-specs-grid" style="margin-bottom: 2rem;">
              <div class="spec-cell">
                <span class="spec-cell-label">Verified AnTuTu</span>
                <span class="spec-cell-val">${topPick.phone.antutuFormatted}</span>
              </div>
              <div class="spec-cell">
                <span class="spec-cell-label">Display</span>
                <span class="spec-cell-val">${topPick.phone.display.size} Flat ${topPick.phone.display.refresh}</span>
              </div>
              <div class="spec-cell">
                <span class="spec-cell-label">Battery Cell</span>
                <span class="spec-cell-val">${topPick.phone.battery.capacity} (${topPick.phone.battery.charging})</span>
              </div>
              <div class="spec-cell">
                <span class="spec-cell-label">Hardware Price</span>
                <span class="spec-cell-val">${topPick.phone.priceFormatted || ('₹' + Number(topPick.phone.price).toLocaleString('en-IN'))}</span>
              </div>
            </div>

            <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
              <button class="btn btn-primary" id="view-top-pick-spec-btn" data-phone-id="${topPick.phone.id}">
                Inspect Full Spec Sheet
              </button>
              <button class="btn btn-outline" id="compare-top-pick-btn" data-phone-id="${topPick.phone.id}">
                Add to Comparison Tray
              </button>
            </div>
          </div>

          ${runnerUp ? `
            <div style="margin-top: 2rem; padding: 1.5rem; border: 1px solid var(--border-light); background-color: var(--bg-card);">
              <div class="eyebrow">Honorable Runner-Up</div>
              <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 0.5rem;">
                <div>
                  <h4 style="font-family: var(--font-serif); font-size: 1.35rem; color: var(--text-primary);">${runnerUp.phone.name}</h4>
                  <p style="font-family: var(--font-mono); font-size: 0.78rem; color: var(--text-muted);">${runnerUp.phone.priceFormatted || ('₹' + Number(runnerUp.phone.price).toLocaleString('en-IN'))} · ${runnerUp.phone.processor.split('(')[0]}</p>
                </div>
                <button class="btn btn-outline btn-sm" id="view-runner-up-btn" data-phone-id="${runnerUp.phone.id}">View Specs</button>
              </div>
            </div>
          ` : ''}
        `;

        const viewTopBtn = document.getElementById('view-top-pick-spec-btn');
        if (viewTopBtn) {
          viewTopBtn.addEventListener('click', () => openSpecModal(topPick.phone));
        }

        const compTopBtn = document.getElementById('compare-top-pick-btn');
        if (compTopBtn) {
          compTopBtn.addEventListener('click', () => {
            if (!state.comparisonList.some(p => p.id === topPick.phone.id)) {
              state.comparisonList.push(topPick.phone);
              updateCompareDrawerUI();
              renderPhoneCards();
              alert(`Added ${topPick.phone.name} to comparison tray.`);
            }
          });
        }

        const viewRunnerBtn = document.getElementById('view-runner-up-btn');
        if (viewRunnerBtn && runnerUp) {
          viewRunnerBtn.addEventListener('click', () => openSpecModal(runnerUp.phone));
        }
      }
    }
  }

  // ==========================================================================
  // 9. MOBILE DRAWER NAVIGATION
  // ==========================================================================
  const mobileToggle = document.querySelector('.mobile-menu-toggle');
  const mobilePanel = document.querySelector('.mobile-nav-panel');
  if (mobileToggle && mobilePanel) {
    mobileToggle.addEventListener('click', () => {
      mobilePanel.classList.toggle('open');
    });
  }
});
