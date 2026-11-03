(() => {
    const feed = document.getElementById("article-feed");
    if (!feed) return;

    const search = document.getElementById("story-search");
    const category = document.getElementById("category-filter");
    const dateSort = document.getElementById("date-sort");
    const count = document.getElementById("story-count");
    const featured = document.getElementById("featured-story");
    const empty = document.getElementById("empty-feed");
    let searchTimer;

    function articleCard(article, isFeatured = false) {
        const card = document.createElement("article");
        card.className = isFeatured ? "featured-card" : "public-card";
        if (article.cover_image) {
            const image = document.createElement("img");
            image.className = "story-thumbnail";
            image.src = article.cover_image;
            image.alt = article.title;
            image.loading = "lazy";
            card.append(image);
        } else {
            const placeholder = document.createElement("div");
            placeholder.className = "story-thumbnail-placeholder";
            placeholder.textContent = article.category || "NewsFlow";
            card.append(placeholder);
        }
        const label = document.createElement("span");
        label.className = "category-label";
        label.textContent = article.category || "General";
        const title = document.createElement("h3");
        const link = document.createElement("a");
        link.href = `/article/${encodeURIComponent(article.id)}`;
        link.textContent = article.title;
        title.append(link);
        const standfirst = document.createElement("p");
        standfirst.textContent = article.summary || article.content.slice(0, 220);
        const meta = document.createElement("div");
        meta.className = "article-meta";
        meta.textContent = `By ${article.author} · ${article.submission_date}`;
        card.append(label, title, standfirst, meta);
        return card;
    }

    async function loadStories() {
        const params = new URLSearchParams();
        if (search.value.trim()) params.set("q", search.value.trim());
        if (category.value) params.set("category", category.value);
        params.set("sort", dateSort.value);
        count.textContent = "Loading stories…";
        try {
            const response = await fetch(`/api/public/articles?${params.toString()}`);
            const articles = await response.json();
            if (!response.ok) throw new Error(articles.error || "Stories could not be loaded.");

            feed.replaceChildren();
            featured.replaceChildren();
            const [lead, ...rest] = articles;
            if (lead && !search.value.trim() && !category.value) {
                featured.append(articleCard(lead, true));
                rest.forEach(article => feed.append(articleCard(article)));
            } else {
                articles.forEach(article => feed.append(articleCard(article)));
            }
            empty.hidden = articles.length !== 0;
            count.textContent = `${articles.length} ${articles.length === 1 ? "story" : "stories"}`;
        } catch (error) {
            count.textContent = "Stories unavailable";
            empty.hidden = false;
            empty.textContent = error.message;
        }
    }

    search.addEventListener("input", () => {
        window.clearTimeout(searchTimer);
        searchTimer = window.setTimeout(loadStories, 250);
    });
    category.addEventListener("change", loadStories);
    dateSort.addEventListener("change", loadStories);
    fetch("/api/public/categories")
        .then(response => {
            if (!response.ok) throw new Error("Sections could not be loaded.");
            return response.json();
        })
        .then(categories => categories.forEach(item => category.add(new Option(item, item))))
        .catch(error => {
            const message = document.getElementById("message");
            message.className = "message error";
            message.textContent = error.message;
            message.style.display = "block";
        });

    const clock = document.getElementById("current-time");
    const updateClock = () => {
        if (clock) clock.textContent = new Intl.DateTimeFormat("en", {
            weekday: "short", month: "short", day: "numeric", hour: "numeric", minute: "2-digit"
        }).format(new Date());
    };
    updateClock();
    window.setInterval(updateClock, 30000);
    loadStories();
})();
