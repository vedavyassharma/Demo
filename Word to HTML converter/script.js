document.getElementById('uploadForm').addEventListener('submit', function (event) {
    event.preventDefault();
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
        .then(response => response.text())
        .then(htmlContent => {
            displayResult({ value: htmlContent });
        })
        .catch(handleError);
});

function displayResult(result) {
    const htmlOutput = document.getElementById('htmlOutput');
    htmlOutput.innerHTML = result.value;

    const navigation = document.getElementById('navigation');
    navigation.innerHTML = "";

    const boldTexts = result.value.match(/<strong>(.*?)<\/strong>/gi);

    if (!boldTexts || boldTexts.length === 0) {
        const noBoldTextsMessage = document.createElement('li');
        noBoldTextsMessage.textContent = "No bold texts found in the document.";
        navigation.appendChild(noBoldTextsMessage);
    } else {
        boldTexts.forEach((boldText, index) => {
            const boldTextContent = boldText.replace(/<[^>]+>/g, '').trim();
            const boldTextId = `boldText${index + 1}`;

            htmlOutput.innerHTML = htmlOutput.innerHTML.replace(boldText, `<a id="${boldTextId}" class="highlight-target"></a>${boldText}`);

            const link = document.createElement('a');
            link.textContent = boldTextContent;
            link.href = `#${boldTextId}`;
            link.classList.add('block', 'py-1', 'px-2', 'hover:bg-gray-300', 'rounded');
            link.onclick = scrollToAnchor;
            navigation.appendChild(link);
        });
    }
}

function scrollToAnchor(event) {
    event.preventDefault();
    const targetId = this.getAttribute('href').substring(1);
    const targetElement = document.getElementById(targetId);

    if (targetElement) {
        const highlightedElements = document.querySelectorAll('.highlight');
        highlightedElements.forEach(el => el.classList.remove('highlight'));

        targetElement.classList.add('highlight');
        const actualBoldText = targetElement.nextElementSibling;
        if (actualBoldText) {
            actualBoldText.classList.add('highlight');
        }

        window.scrollTo({
            top: targetElement.offsetTop - document.getElementById('content').offsetTop,
            behavior: 'smooth'
        });
    }
}

function handleError(err) {
    console.error(err);
    document.getElementById('htmlOutput').innerHTML = "Error occurred while converting the document.";
}
