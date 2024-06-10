const dialog = document.querySelector("dialog");
const showButton = document.querySelectorAll(".busketButton");
const closeButton = document.querySelector(".close");

// "Show the dialog" button opens the dialog modally
showButton.forEach(button => {
    button.addEventListener("click", () => {
        dialog.showModal();
    })
});
closeButton.addEventListener("click", () => {
  dialog.close();
});
