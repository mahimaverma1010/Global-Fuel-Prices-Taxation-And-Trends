/**
 * Global Fuel Analytics — Client-side JavaScript
 * Handles responsive Tableau embedding, fullscreen toggle, reload triggers,
 * and user interface enhancements.
 */

document.addEventListener('DOMContentLoaded', function () {
    console.log("Global Fuel Analytics application initialized.");

    // Initialize Tooltips if Bootstrap is available
    if (typeof bootstrap !== 'undefined' && bootstrap.Tooltip) {
        var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
        tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        });
    }

    // Fullscreen toggle for Tableau visual container
    const fullscreenBtn = document.getElementById('btn-fullscreen');
    const tableauContainer = document.getElementById('tableau-container');

    if (fullscreenBtn && tableauContainer) {
        fullscreenBtn.addEventListener('click', function () {
            if (!document.fullscreenElement) {
                if (tableauContainer.requestFullscreen) {
                    tableauContainer.requestFullscreen();
                } else if (tableauContainer.webkitRequestFullscreen) {
                    tableauContainer.webkitRequestFullscreen();
                } else if (tableauContainer.msRequestFullscreen) {
                    tableauContainer.msRequestFullscreen();
                }
                fullscreenBtn.innerHTML = '<i class="bi bi-fullscreen-exit"></i> Exit Fullscreen';
            } else {
                if (document.exitFullscreen) {
                    document.exitFullscreen();
                }
                fullscreenBtn.innerHTML = '<i class="bi bi-arrows-fullscreen"></i> Fullscreen';
            }
        });

        document.addEventListener('fullscreenchange', function () {
            if (!document.fullscreenElement) {
                fullscreenBtn.innerHTML = '<i class="bi bi-arrows-fullscreen"></i> Fullscreen';
            }
        });
    }

    // Reload iframe trigger
    const reloadBtn = document.getElementById('btn-reload-viz');
    const vizFrame = document.getElementById('tableau-frame');

    if (reloadBtn && vizFrame) {
        reloadBtn.addEventListener('click', function () {
            const currentSrc = vizFrame.src;
            vizFrame.src = '';
            setTimeout(function () {
                vizFrame.src = currentSrc;
            }, 150);
        });
    }

    // Copy Tableau URL to clipboard helper
    const copyUrlBtn = document.getElementById('btn-copy-url');
    if (copyUrlBtn) {
        copyUrlBtn.addEventListener('click', function () {
            const url = this.getAttribute('data-url');
            if (url) {
                navigator.clipboard.writeText(url).then(function () {
                    const originalText = copyUrlBtn.innerHTML;
                    copyUrlBtn.innerHTML = '<i class="bi bi-check2"></i> Copied!';
                    setTimeout(function () {
                        copyUrlBtn.innerHTML = originalText;
                    }, 2000);
                }).catch(function (err) {
                    console.error('Failed to copy: ', err);
                });
            }
        });
    }
});

