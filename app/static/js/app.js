let form = document.querySelector('#calculateIndexForm');
if (form) {
    form.addEventListener('submit', async function (e) {
        e.preventDefault();
        let data = {};
        new FormData(form).forEach(function (value, key) {
            data[key] = value;
        });

        let response = await fetch(form.getAttribute('action'), {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        const json = await response.json();
        if (json.index) {
            document.querySelector('#indexResult').innerHTML = json.index;
        }
        if (json.error) {
            document.querySelector('#error').innerHTML = json.error;
                document.querySelector('#error').style.display = 'block';
            setTimeout(function () {
                document.querySelector('#error').style.display = 'none';
            }, 2000)
        }
    })
}