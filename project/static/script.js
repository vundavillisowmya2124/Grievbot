function sendMessage() {
  const input = document.getElementById("user-input");
  const msg = input.value.trim();
  if (!msg) return;

  const chatBox = document.getElementById("chat-box");
  chatBox.innerHTML += `<div class="user-msg">${msg}</div>`;
  input.value = "";

  fetch("/get", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({msg: msg})
  })
  .then(response => response.json())
  .then(data => {
    chatBox.innerHTML += `<div class="bot-msg">${data.response}</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;
  });
}
