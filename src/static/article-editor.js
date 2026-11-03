document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("submission-form");
    const message = document.getElementById("message");
    if (!form || !message) return;

    form.addEventListener("submit", async event => {
        if (event.submitter?.value !== "submit") return;
        event.preventDefault();
        const fields = new FormData(form);
        const payload = Object.fromEntries(
            ["title", "author", "content", "summary", "category", "cover_image"]
                .map(name => [name, fields.get(name) || ""])
        );
        try {
            const response = await fetch("/api/articles", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRF-Token": document.querySelector('meta[name="csrf-token"]').content
                },
                body: JSON.stringify(payload)
            });
            const data = await response.json();
            if (!response.ok) throw new Error(data.error || "The story could not be submitted.");
            form.reset();
            message.className = "message success";
            message.textContent = `Story sent to the desk. Article ID: ${data.id}, Status: ${data.status}`;
            message.style.display = "block";
        } catch (error) {
            message.className = "message error";
            message.textContent = error.message;
            message.style.display = "block";
        }
    });
});
