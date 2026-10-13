let currentArticleId = null;

function reviewerById(id) {
    return document.getElementById(id);
}

function csrfHeaders(json = false) {
    const headers = { "X-CSRF-Token": document.querySelector('meta[name="csrf-token"]').content };
    if (json) headers["Content-Type"] = "application/json";
    return headers;
}

function statusLabel(status) {
    return { SUBMITTED: "On the wire", APPROVED: "Cleared", REJECTED: "Spiked", DRAFT: "Draft" }[status] || status;
}

async function loadArticles() {
    try {
        const response = await fetch("/api/articles");
        const articles = await response.json();
        if (!response.ok) throw new Error(articles.error || "Unable to load articles.");
        const tbody = document.querySelector("#articles-table tbody");
        tbody.replaceChildren();
        if (!articles.length) {
            const row = document.createElement("tr");
            const cell = document.createElement("td");
            cell.colSpan = 6;
            cell.className = "empty-state";
            cell.textContent = "No stories have reached the desk yet.";
            row.append(cell);
            tbody.append(row);
            return;
        }
        articles.forEach(article => {
            const row = document.createElement("tr");
            [article.id, article.title, article.author, article.submission_date].forEach(value => {
                const cell = document.createElement("td");
                cell.textContent = value ?? "";
                row.append(cell);
            });
            const statusCell = document.createElement("td");
            const status = document.createElement("span");
            status.className = `status-tag status-${String(article.status).toLowerCase()}`;
            status.textContent = `${statusLabel(article.status)} (${article.status})`;
            statusCell.append(status);
            row.append(statusCell);
            const actionCell = document.createElement("td");
            const view = document.createElement("button");
            view.className = "table-button btn-view";
            view.type = "button";
            view.textContent = "View / Review";
            view.addEventListener("click", () => viewArticle(article.id));
            actionCell.append(view);
            row.append(actionCell);
            tbody.append(row);
        });
    } catch (error) {
        showReviewerMessage("error", `Failed to load articles: ${error.message}`);
    }
}

async function viewArticle(id) {
    try {
        const response = await fetch(`/api/articles/${id}`);
        const article = await response.json();
        if (!response.ok) throw new Error(article.error || "Article not found.");
        currentArticleId = article.id;
        reviewerById("modal-title").textContent = article.title;
        reviewerById("modal-author").textContent = article.author;
        reviewerById("modal-date").textContent = article.submission_date;
        reviewerById("modal-status").textContent = `${statusLabel(article.status)} (${article.status})`;
        reviewerById("modal-content").textContent = article.content;
        reviewerById("reject-comment").value = article.comment || "";
        reviewerById("modal-comment").textContent = article.comment ? `Desk note: ${article.comment}` : "";
        reviewerById("modal-comment").hidden = !article.comment;
        reviewerById("article-modal").classList.add("open");
        reviewerById("modal-actions").hidden = article.status !== "SUBMITTED";
    } catch (error) {
        showReviewerMessage("error", `Failed to load article: ${error.message}`);
    }
}

async function reviewArticle(action, comment) {
    if (!currentArticleId) return;
    try {
        const options = { method: "PUT", headers: csrfHeaders(action === "reject") };
        if (action === "reject") options.body = JSON.stringify({ comment });
        const response = await fetch(`/api/articles/${currentArticleId}/${action}`, options);
        const data = await response.json();
        if (!response.ok) throw new Error(data.error || "Editorial decision failed.");
        showReviewerMessage(
            "success",
            action === "approve"
                ? "Article approved successfully. It is cleared for publishing."
                : "Article rejected successfully. It was spiked with the desk note."
        );
        closeArticleModal();
        await loadArticles();
    } catch (error) {
        showReviewerMessage("error", error.message);
    }
}

function approveArticle() {
    return reviewArticle("approve");
}

function rejectArticle() {
    const comment = reviewerById("reject-comment").value.trim();
    if (!comment) {
        showReviewerMessage("error", "A rejection comment is mandatory.");
        reviewerById("reject-comment").focus();
        return;
    }
    return reviewArticle("reject", comment);
}

function closeArticleModal() {
    reviewerById("article-modal").classList.remove("open");
    currentArticleId = null;
}

function showReviewerMessage(type, text) {
    const message = reviewerById("message");
    message.className = `message ${type}`;
    message.textContent = text;
    message.style.display = "block";
    window.clearTimeout(showReviewerMessage.timeout);
    showReviewerMessage.timeout = window.setTimeout(() => { message.style.display = "none"; }, 5000);
}

document.addEventListener("DOMContentLoaded", () => {
    reviewerById("close-modal").addEventListener("click", closeArticleModal);
    reviewerById("article-modal").addEventListener("click", event => {
        if (event.target === event.currentTarget) closeArticleModal();
    });
    loadArticles();
});
