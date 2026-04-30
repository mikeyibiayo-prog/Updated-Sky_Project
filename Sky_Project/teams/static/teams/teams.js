document.addEventListener('DOMContentLoaded', function () {
  const teamSearch = document.querySelector('[data-team-search]');
  if (teamSearch) {
    teamSearch.addEventListener('input', function () {
      const query = teamSearch.value.toLowerCase();
      document.querySelectorAll('[data-team-row]').forEach(function (row) {
        row.style.display = row.textContent.toLowerCase().includes(query) ? 'grid' : 'none';
      });
    });
  }

  function openPanel(panelName, tabToActivate) {
    document.querySelectorAll('[data-panel]').forEach(function (panel) {
      panel.classList.remove('active');
    });

    const panel = document.querySelector('[data-panel="' + panelName + '"]');
    if (panel) {
      panel.classList.add('active');
      panel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    document.querySelectorAll('[data-tab]').forEach(function (tab) {
      tab.classList.remove('active');
    });

    if (tabToActivate) {
      const tab = document.querySelector('[data-tab="' + tabToActivate + '"]');
      if (tab) tab.classList.add('active');
    }
  }

  document.querySelectorAll('[data-tab]').forEach(function (tab) {
    tab.addEventListener('click', function (event) {
      event.preventDefault();
      openPanel(tab.dataset.tab, tab.dataset.tab);
    });
  });

  document.querySelectorAll('[data-open]').forEach(function (button) {
    button.addEventListener('click', function (event) {
      event.preventDefault();
      openPanel(button.dataset.open, null);
    });
  });

  document.querySelectorAll('[data-filter]').forEach(function (button) {
    button.addEventListener('click', function () {
      const group = button.parentElement;
      group.querySelectorAll('[data-filter]').forEach(function (item) {
        item.classList.remove('active');
      });
      button.classList.add('active');

      const value = button.dataset.filter;
      document.querySelectorAll(group.dataset.target).forEach(function (card) {
        const matches = value === 'all' || card.dataset.type === value || card.dataset.role === value;
        card.style.display = matches ? '' : 'none';
      });
    });
  });

  const MESSAGE_KEY = 'sky_frontend_team_messages';
  const MEETING_KEY = 'sky_frontend_team_meetings';

  function readSaved(key) {
    try { return JSON.parse(localStorage.getItem(key)) || []; }
    catch (e) { return []; }
  }

  function saveItems(key, items) {
    localStorage.setItem(key, JSON.stringify(items));
  }

  function escapeHtml(value) {
    return String(value).replace(/[&<>'"]/g, function (char) {
      return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#039;', '"': '&quot;' })[char];
    });
  }

  function renderMessages() {
    const list = document.getElementById('team-messages-list');
    if (!list) return;
    const messages = readSaved(MESSAGE_KEY);
    if (!messages.length) {
      list.innerHTML = '<div class="empty-state">No team messages added yet.</div>';
      return;
    }
    list.innerHTML = messages.map(function (item) {
      return '<article class="activity-item">' +
        '<div class="activity-meta">' + escapeHtml(item.createdAt) + '</div>' +
        '<h3>' + escapeHtml(item.subject) + '</h3>' +
        '<p>' + escapeHtml(item.message) + '</p>' +
      '</article>';
    }).join('');
  }

  function renderMeetings() {
    const list = document.getElementById('team-meetings-list');
    if (!list) return;
    const meetings = readSaved(MEETING_KEY);
    if (!meetings.length) {
      list.innerHTML = '<div class="empty-state">No team meetings scheduled yet.</div>';
      return;
    }
    list.innerHTML = meetings.map(function (item) {
      return '<article class="activity-item meeting-item">' +
        '<div>' +
          '<div class="activity-meta">' + escapeHtml(item.date) + ' at ' + escapeHtml(item.time) + '</div>' +
          '<h3>' + escapeHtml(item.platform) + '</h3>' +
          '<p>' + escapeHtml(item.message) + '</p>' +
        '</div>' +
        '<span class="status active-status">Scheduled</span>' +
      '</article>';
    }).join('');
  }

  const emailForm = document.getElementById('team-email-form');
  if (emailForm) {
    emailForm.addEventListener('submit', function (event) {
      event.preventDefault();
      const subject = document.getElementById('team-email-subject').value.trim();
      const message = document.getElementById('team-email-message').value.trim();
      if (!subject || !message) return;
      const items = readSaved(MESSAGE_KEY);
      items.unshift({
        subject: subject,
        message: message,
        createdAt: new Date().toLocaleString()
      });
      saveItems(MESSAGE_KEY, items);
      emailForm.reset();
      renderMessages();
      const note = document.getElementById('team-email-success');
      if (note) {
        note.hidden = false;
        setTimeout(function () { note.hidden = true; }, 2500);
      }
    });
  }

  const scheduleForm = document.getElementById('team-schedule-form');
  if (scheduleForm) {
    scheduleForm.addEventListener('submit', function (event) {
      event.preventDefault();
      const date = document.getElementById('team-meeting-date').value;
      const time = document.getElementById('team-meeting-time').value;
      const platform = document.getElementById('team-meeting-platform').value.trim();
      const message = document.getElementById('team-meeting-message').value.trim();
      if (!date || !time || !platform || !message) return;
      const items = readSaved(MEETING_KEY);
      items.unshift({ date: date, time: time, platform: platform, message: message });
      saveItems(MEETING_KEY, items);
      scheduleForm.reset();
      renderMeetings();
      const note = document.getElementById('team-schedule-success');
      if (note) {
        note.hidden = false;
        setTimeout(function () { note.hidden = true; }, 2500);
      }
    });
  }

  const clearMessages = document.querySelector('[data-clear-team-messages]');
  if (clearMessages) {
    clearMessages.addEventListener('click', function () {
      localStorage.removeItem(MESSAGE_KEY);
      renderMessages();
    });
  }

  const clearMeetings = document.querySelector('[data-clear-team-meetings]');
  if (clearMeetings) {
    clearMeetings.addEventListener('click', function () {
      localStorage.removeItem(MEETING_KEY);
      renderMeetings();
    });
  }

  renderMessages();
  renderMeetings();

  if (window.location.hash === '#email') openPanel('email', null);
  if (window.location.hash === '#schedule') openPanel('schedule', null);
});
