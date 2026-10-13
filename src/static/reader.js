document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("bookmark-button");
    const message = document.getElementById("bookmark-message");
    if (!button) return;
    button.addEventListener("click", async () => {
        button.disabled = true;
        try {
            const response = await fetch("/api/reader/bookmarks", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRF-Token": document.querySelector('meta[name="csrf-token"]')?.content || ""
                },
                body: JSON.stringify({ article_id: Number(button.dataset.articleId) })
            });
            const data = await response.json();
            if (!response.ok) throw new Error(data.error || "This story could not be saved.");
            message.textContent = "Saved to your reading list.";
        } catch (error) {
            message.textContent = error.message;
        } finally {
            button.disabled = false;
        }
    });
});
