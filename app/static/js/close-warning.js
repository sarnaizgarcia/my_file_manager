(function mainCloseWarning() {
  function closeWindow() {
    const modalWindow = document.querySelector(".messages");
    modalWindow.classList.add("close");
  }
  const closeButton = document.querySelector(".close.material-icons");
  if (closeButton) {
    closeButton.addEventListener("click", closeWindow);
  }
})();
