// script to show/hide the anime tags in the user anime list
document.querySelectorAll('.tags-cell').forEach(function(cell) {
    let tags = cell.querySelectorAll('.tag');
    let showAllBtn = cell.querySelector('.show-all-btn');
    let hideBtn = cell.querySelector('.hide-btn');

    tags.forEach(function(tag) {
        tag.style.display = 'none';
    });

    showAllBtn.addEventListener('click', function() {
        tags.forEach(function(tag) {
            tag.style.display = 'inline-block';
        });
        showAllBtn.style.display = 'none';
        hideBtn.style.display = 'inline-block';
    });

    hideBtn.addEventListener('click', function() {
        tags.forEach(function(tag) {
            tag.style.display = 'none';
        });
        hideBtn.style.display = 'none';
        showAllBtn.style.display = 'inline-block';
    });
});

document.querySelectorAll('.tags-cell-detail-view').forEach(function(cell) {
    let tags = cell.querySelectorAll('.tag');
    let showAllBtn = cell.querySelector('.show-all-btn');
    let hideBtn = cell.querySelector('.hide-btn');

    tags.forEach(function(tag, index) {
        // Display only the first four tags, hide the rest
        if (index < 4) {
            tag.style.display = 'inline-block';
        } else {
            tag.style.display = 'none';
        }
    });

    showAllBtn.addEventListener('click', function() {
        tags.forEach(function(tag) {
            tag.style.display = 'inline-block';
        });
        showAllBtn.style.display = 'none';
        hideBtn.style.display = 'inline-block';
    });

    hideBtn.addEventListener('click', function() {
        // Display only the first four tags, hide the rest
        tags.forEach(function(tag, index) {
            if (index < 4) {
                tag.style.display = 'inline-block';
            } else {
                tag.style.display = 'none';
            }
        });
        hideBtn.style.display = 'none';
        showAllBtn.style.display = 'inline-block';
    });
    });