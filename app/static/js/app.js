postData(
    document.querySelector('#calculateIndexForm'),
    document.querySelector('#indexResult'),
    document.querySelector('#error'),
)

postData(
    document.querySelector('#updatePasswordForm'),
    document.querySelector('#updatePasswordSuccess'),
    document.querySelector('#updatePasswordError'),
)

function postData(form, outputSelector, outputSelectorError) {
    if (form) {
        form.addEventListener('submit', async function (e) {
            e.preventDefault();
            let data = {};
            new FormData(form).forEach(function (value, key) {
                data[key] = value;
            });
            console.log(JSON.stringify(data));
            let response = await fetch(form.getAttribute('action'), {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });
            const json = await response.json();
            if (json.response) {
                outputSelector.innerHTML = json.response;
            }
            if (json.error) {
                outputSelectorError.innerHTML = json.error;
                outputSelectorError.style.display = 'block';
                setTimeout(function () {
                    outputSelectorError.style.display = 'none';
                }, 2000)
            }
        })
    }
}