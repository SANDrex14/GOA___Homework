function fakeApiRequest(successRate = 0.8) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (Math.random() < successRate) {
                resolve();
            } else {
                reject("Network error");
            }
        }, 2000);
    });
}

document.addEventListener("DOMContentLoaded", () => {
    const taskInput = document.getElementById("taskInput");
    const addTaskButton = document.getElementById("addTaskButton");
    const taskList = document.getElementById("taskList");
    const message = document.getElementById("message");

    function displayMessage(text, isError = false) {
        message.textContent = text;
        message.style.color = isError ? "red" : "black";
    }

    function fetchTasks() {
        displayMessage("Fetching tasks...");
        fakeApiRequest()
            .then(() => {
                displayMessage("");
                taskList.innerHTML = "<li>Sample Task 1</li><li>Sample Task 2</li>";
            })
            .catch(() => displayMessage("Failed to fetch tasks", true));
    }

    addTaskButton.addEventListener("click", () => {
        const taskText = taskInput.value.trim();
        if (!taskText) return;

        displayMessage("Adding task...");
        fakeApiRequest()
            .then(() => {
                displayMessage("");
                const listItem = document.createElement("li");
                listItem.textContent = taskText;
                taskList.appendChild(listItem);
                taskInput.value = "";
            })
            .catch(() => displayMessage("Failed to add task", true));
    });

    fetchTasks();
});
