let currentArticleId = null;

function reviewerById(id) {
    return document.getElementById(id);
}

async function loadArticles() {
    try {
        const response = await fetch('/api/articles');
        const articles = await response.json();
        if (!response.ok) throw new Error(articles.error || 'Unable to load articles.');
        const tbody = document.querySelector('#articles-table tbody');
        tbody.replaceChildren();
        if (!articles.length) {
            const row = document.createElement('tr');
            const cell = document.createElement('td');
            cell.colSpan = 6;
            cell.className = 'empty-state';
            cell.textContent = 'No articles have reached the desk yet.';
            row.appendChild(cell);
            tbody.appendChild(row);
            return;
        }
        articles.forEach(article => {
            const row = document.createElement('tr');
            [article.id, article.title, article.author, article.submission_date].forEach(value => {
                const cell = document.createElement('td');
                cell.textContent = value ?? '';
                row.appendChild(cell);
            });
            const statusCell = document.createElement('td');
            const status = document.createElement('span');
            status.className = `status-tag ${statusClass(article.status)}`;
            status.textContent = `${statusLabel(article.status)} (${article.status})`;
            statusCell.appendChild(status);
            row.appendChild(statusCell);

            const actionCell = document.createElement('td');
            const view = document.createElement('button');
            view.className = 'table-button btn-view';
            view.type = 'button';
            view.textContent = 'View / Review';
            view.addEventListener('click', () => viewArticle(article.id));
            actionCell.appendChild(view);
            row.appendChild(actionCell);
            tbody.appendChild(row);
        });
    } catch (error) {
        showReviewerMessage('error', `Failed to load articles: ${error.message}`);
    }
}

function statusLabel(status) {
    return { SUBMITTED: 'On the wire', APPROVED: 'Cleared', REJECTED: 'Spiked' }[status] || status;
}

function statusClass(status) {
    return { SUBMITTED: 'status-submitted', APPROVED: 'status-approved', REJECTED: 'status-rejected' }[status] || '';
}

async function viewArticle(id) {
    try {
        const response = await fetch(`/api/articles/${id}`);
        const article = await response.json();
        if (!response.ok) throw new Error(article.error || 'Article not found.');
        currentArticleId = article.id;
        reviewerById('modal-title').textContent = article.title;
        reviewerById('modal-author').textContent = article.author;
        reviewerById('modal-date').textContent = article.submission_date;
        reviewerById('modal-status').textContent = `${statusLabel(article.status)} (${article.status})`;
        reviewerById('modal-content').textContent = article.content;
        reviewerById('reject-comment').value = article.comment || '';
        reviewerById('article-modal').style.display = 'block';
        reviewerById('modal-actions').style.display = article.status === 'SUBMITTED' ? 'block' : 'none';
    } catch (error) {
        showReviewerMessage('error', `Failed to load article: ${error.message}`);
    }
}

async function approveArticle() {
    if (!currentArticleId) return;
    try {
        const response = await fetch(`/api/articles/${currentArticleId}/approve`, { method: 'PUT' });
        const data = await response.json();
        if (!response.ok) throw new Error(data.error || 'Approval failed.');
        showReviewerMessage('success', 'Article approved successfully.');
        closeArticleModal();
        loadArticles();
    } catch (error) {
        showReviewerMessage('error', error.message);
    }
}

async function rejectArticle() {
    if (!currentArticleId) return;
    const comment = reviewerById('reject-comment').value.trim();
    if (!comment) {
        showReviewerMessage('error', 'A rejection comment is mandatory.');
        return;
    }
    try {
        const response = await fetch(`/api/articles/${currentArticleId}/reject`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ comment })
        });
        const data = await response.json();
        if (!response.ok) throw new Error(data.error || 'Rejection failed.');
        showReviewerMessage('success', 'Article rejected successfully.');
        closeArticleModal();
        loadArticles();
    } catch (error) {
        showReviewerMessage('error', error.message);
    }
}

function closeArticleModal() {
    reviewerById('article-modal').style.display = 'none';
    currentArticleId = null;
}

function showReviewerMessage(type, text) {
    const message = reviewerById('message');
    message.className = type;
    message.textContent = text;
    message.style.display = 'block';
    window.clearTimeout(showReviewerMessage.timeout);
    showReviewerMessage.timeout = window.setTimeout(() => {
        message.style.display = 'none';
    }, 5000);
}

function updateReviewerClock() {
    const clock = reviewerById('current-time');
    if (clock) {
        clock.textContent = new Intl.DateTimeFormat('en', {
            weekday: 'short', month: 'short', day: 'numeric', hour: 'numeric', minute: '2-digit'
        }).format(new Date());
    }
}

document.addEventListener('DOMContentLoaded', () => {
    reviewerById('close-modal').addEventListener('click', closeArticleModal);
    reviewerById('article-modal').addEventListener('click', event => {
        if (event.target === event.currentTarget) closeArticleModal();
    });
    updateReviewerClock();
    window.setInterval(updateReviewerClock, 30000);
    loadArticles();
});
