// Contents of static/js/app.js

let currentView = 0;

function switchPreview() {
  const mobilePreview = document.getElementById('mobile-preview');
  const desktopPreview = document.getElementById('desktop-preview');
  const largeDesktopPreview = document.getElementById('large-desktop-preview');
  const previewButton = document.getElementById('toggle-preview');

  if (currentView === 0) {
    mobilePreview.classList.add('hidden');
    desktopPreview.classList.remove('hidden');
    currentView = 1;
    previewButton.innerText = 'Switch to large desktop view';
  } else if (currentView === 1) {
    desktopPreview.classList.add('hidden');
    largeDesktopPreview.classList.remove('hidden');
    currentView = 2;
    previewButton.innerText = 'Switch to mobile view';
  } else {
    largeDesktopPreview.classList.add('hidden');
    mobilePreview.classList.remove('hidden');
    currentView = 0;
    previewButton.innerText = 'Switch to desktop view';
  }
}