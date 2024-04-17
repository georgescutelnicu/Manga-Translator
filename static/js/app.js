// Sets up custom dropdown behavior for all select wrappers
document.addEventListener("DOMContentLoaded", () => {
    const selectWrappers = document.querySelectorAll('.select-wrapper');

    selectWrappers.forEach(wrapper => {
        const selectBox = wrapper.querySelector('.custom-select');
        const selectedText = selectBox.querySelector('.selected');
        const options = selectBox.querySelector('.options');
        const optionList = selectBox.querySelectorAll('.option');

        const defaultOption = optionList[0];
        selectedText.textContent = defaultOption.textContent;
        defaultOption.classList.add('selected');

        // Toggle options display on select box click
        selectBox.addEventListener('click', () => {
            options.style.display = options.style.display === 'block' ? 'none' : 'block';
            selectBox.classList.toggle('open');
        });

        // Update selected option and hide options on option click
        optionList.forEach(option => {
            option.addEventListener('click', () => {
                selectedText.textContent = option.textContent;
                optionList.forEach(opt => opt.classList.remove('selected'));
                option.classList.add('selected');
            });
        });

        // Hide options when clicking outside the select box
        window.addEventListener('click', e => {
            if (!wrapper.contains(e.target)) {
                options.style.display = 'none';
                selectBox.classList.remove('open');
            }
        });
    });
});

// Handles file upload change event
document.getElementById('file-upload').addEventListener('change', function() {
    const fileName = this.files[0].name;
    const truncatedFileName = truncateFileName(fileName, 20);
    document.querySelector('.file').innerText = truncatedFileName;
});

// Truncates file name if it exceeds the maximum length
function truncateFileName(fileName, maxLength) {
    return fileName.length <= maxLength ? fileName : fileName.substr(0, maxLength - 3) + '...';
}

// Updates hidden input fields with selected options
function updateHiddenInputs() {
    const selectedLanguage = document.querySelector("#language .selected").innerText;
    const selectedTranslator = document.querySelector("#translator .selected").innerText;
    const selectedFont = document.querySelector("#font .selected").innerText;

    document.getElementById("selected_language").value = selectedLanguage;
    document.getElementById("selected_translator").value = selectedTranslator;
    document.getElementById("selected_font").value = selectedFont;

    document.querySelector('form').style.display = 'none';
    document.getElementById('loading-img').style.display = 'block';
    document.getElementById('loading-p').style.display = 'block';
}
