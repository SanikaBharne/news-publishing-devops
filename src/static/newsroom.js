const statusLabels = {
    SUBMITTED: 'On the wire',
    APPROVED: 'Cleared',
    REJECTED: 'Spiked'
};

const statusClasses = {
    SUBMITTED: 'status-submitted',
    APPROVED: 'status-approved',
    REJECTED: 'status-rejected'
};

let articles = [];
let rejectionArticleId = null;

function byId(id) {
    return document.getElementById(id);
}

function escapeText(value) {
    return String(value ?? '');
}

function statusTag(status) {
    const tag = document.createElement('span');
    tag.className = `status-tag ${statusClasses[status] || ''}`;
    tag.textContent = statusLabels[status] || status;
    return tag;
}

function articleMeta(article) {
    const meta = document.createElement('div');
    meta.className = 'article-meta';
    const author = document.createElement('strong');
    author.textContent = `By ${escapeText(article.author)}`;
    meta.append(author, statusTag(article.status));
    return meta;
}

function makeArticleCard(article, withActions) {
    const card = document.createElement('article');
    card.className = 'article-card';
    card.dataset.articleId = article.id;

    const meta = articleMeta(article);
    const heading = document.createElement('h3');
    heading.textContent = escapeText(article.title);
    const content = document.createElement('p');
    content.className = 'article-content';
    content.textContent = escapeText(article.content);
    card.append(meta, heading, content);

    if (withActions) {
        const actions = document.createElement('div');
        actions.className = 'card-actions';
        const approve = document.createElement('button');
        approve.className = 'primary-button';
        approve.type = 'button';
        approve.textContent = 'Clear for publishing';
        approve.addEventListener('click', () => updateArticle(article.id, 'approve'));
        const reject = document.createElement('button');
        reject.className = 'danger-button';
        reject.type = 'button';
        reject.textContent = 'Spike';
        reject.addEventListener('click', () => openRejectionModal(article.id));
        actions.append(approve, reject);
        card.appendChild(actions);
    }
    return card;
}

function renderQueue() {
    const list = byId('queue-list');
    list.replaceChildren();
    const submitted = articles.filter(article => article.status === 'SUBMITTED');
    byId('queue-count').textContent = `${submitted.length} ${submitted.length === 1 ? 'story' : 'stories'}`;
    if (!submitted.length) {
        const empty = document.createElement('p');
        empty.className = 'empty-state';
        empty.textContent = 'The wire is clear. New submissions will appear here.';
        list.appendChild(empty);
        return;
    }
    submitted.forEach(article => list.appendChild(makeArticleCard(article, true)));
}

function renderBoardColumn(containerId, status) {
    const container = byId(containerId);
    container.replaceChildren();
    const matching = articles.filter(article => article.status === status);
    byId(`${status.toLowerCase()}-count`).textContent = matching.length;
    if (!matching.length) {
        const empty = document.createElement('p');
        empty.className = 'empty-state';
        empty.textContent = 'No stories yet.';
        container.appendChild(empty);
        return;
    }
    matching.forEach(article => {
        const item = document.createElement('article');
        item.className = 'board-item';
        const title = document.createElement('h3');
        title.textContent = escapeText(article.title);
        const author = document.createElement('p');
        author.className = 'article-meta';
        author.textContent = `By ${escapeText(article.author)}`;
        item.append(title, author);
        container.appendChild(item);
    });
}

function renderBoard() {
    renderBoardColumn('submitted-items', 'SUBMITTED');
    renderBoardColumn('approved-items', 'APPROVED');
    renderBoardColumn('rejected-items', 'REJECTED');
}

function renderLive() {
    const cleared = articles.filter(article => article.status === 'APPROVED');
    byId('live-count').textContent = cleared.length;
    const list = byId('live-list');
    list.replaceChildren();
    if (!cleared.length) {
        const empty = document.createElement('p');
        empty.className = 'empty-state';
        empty.textContent = 'No stories have been cleared for publishing yet.';
        list.appendChild(empty);
        return;
    }
    cleared.forEach(article => list.appendChild(makeArticleCard(article, false)));
}

function renderAll() {
    renderQueue();
    renderBoard();
    renderLive();
}

async function loadArticles() {
    try {
        const response = await fetch('/api/articles');
        const data = await response.json();
        if (!response.ok) throw new Error(data.error || 'Unable to load articles.');
        articles = data;
        renderAll();
    } catch (error) {
        showMessage('error', `Could not load newsroom data: ${error.message}`);
    }
}

async function updateArticle(id, action, comment) {
    const options = { method: 'PUT' };
    if (action === 'reject') {
        options.headers = { 'Content-Type': 'application/json' };
        options.body = JSON.stringify({ comment });
    }
    try {
        const response = await fetch(`/api/articles/${id}/${action}`, options);
        const data = await response.json();
        if (!response.ok) throw new Error(data.error || 'The article could not be updated.');
        showMessage('success', action === 'approve' ? 'Article cleared for publishing.' : 'Article spiked with the desk note.');
        closeRejectionModal();
        await loadArticles();
    } catch (error) {
        showMessage('error', error.message);
    }
}

function openRejectionModal(id) {
    rejectionArticleId = id;
    byId('reject-reason').value = '';
    byId('reject-modal').classList.add('open');
    byId('reject-reason').focus();
}

function closeRejectionModal() {
    rejectionArticleId = null;
    byId('reject-modal').classList.remove('open');
}

function showMessage(type, text) {
    const message = byId('message');
    message.className = type;
    message.textContent = text;
    message.style.display = 'block';
    window.clearTimeout(showMessage.timeout);
    showMessage.timeout = window.setTimeout(() => {
        message.style.display = 'none';
    }, 5000);
}

function activateSection(sectionId) {
    const target = sectionId || 'newsroom';
    document.querySelectorAll('[data-section]').forEach(section => {
        section.hidden = section.id !== target;
    });
    document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.toggle('active', link.dataset.target === target);
    });
}

function updateClock() {
    const clock = byId('current-time');
    if (clock) {
        clock.textContent = new Intl.DateTimeFormat('en', {
            weekday: 'short', month: 'short', day: 'numeric', hour: 'numeric', minute: '2-digit'
        }).format(new Date());
    }
}

document.addEventListener('DOMContentLoaded', () => {
    byId('submission-form').addEventListener('submit', async event => {
        event.preventDefault();
        const form = event.currentTarget;
        const payload = {
            title: byId('title').value,
            author: byId('author').value,
            content: byId('content').value
        };
        try {
            const response = await fetch('/api/articles', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });
            const data = await response.json();
            if (!response.ok) throw new Error(data.error || 'The story could not be sent.');
            showMessage('success', `Story sent to the desk. Article ID: ${data.id}, Status: ${data.status}`);
            form.reset();
            await loadArticles();
        } catch (error) {
            showMessage('error', `Submission error: ${error.message}`);
        }
    });

    byId('reject-form').addEventListener('submit', event => {
        event.preventDefault();
        const reason = byId('reject-reason').value.trim();
        if (!reason) {
            showMessage('error', 'A reason is required before an article can be spiked.');
            return;
        }
        updateArticle(rejectionArticleId, 'reject', reason);
    });
    byId('cancel-reject').addEventListener('click', closeRejectionModal);
    byId('close-reject').addEventListener('click', closeRejectionModal);
    byId('reject-modal').addEventListener('click', event => {
        if (event.target === event.currentTarget) closeRejectionModal();
    });

    document.querySelectorAll('[data-target]').forEach(link => {
        link.addEventListener('click', event => {
            event.preventDefault();
            const target = link.dataset.target;
            activateSection(target);
            window.history.replaceState(null, '', `#${target}`);
        });
    });

    activateSection(window.location.hash.slice(1));
    updateClock();
    window.setInterval(updateClock, 30000);
    loadArticles();
});
