'use strict'

let domain = (new URL(location.href)).origin

const loadPage = async () => {
    let data = localStorage.getItem('profile')
    if (data) {
        let profile = JSON.parse(data)

        $('#loginBox .secret input')[0].value = profile.secret

        await loginSystem()
    }
}

const loginSystem = async () => {
    let secret = $('#loginBox .secret input')[0].value

    if (!secret) {
        alert("Secret field is empty.")
        return
    }

    try {
        let res = await callBrowse(secret)
        console.log(res)

        localStorage.setItem('profile', JSON.stringify({ secret }))

        // refreshView(res.results)

        $('#urlLine').removeClass(['d-none'])
        $('#urlBox').removeClass(['d-none'])
    }
    catch (err) {
        console.log(err)

        if (err.status == 401) {
            alert("Verification failed.")
            return
        }

        alert("Unable to establish connection.")
    }
}

const callBrowse = (secret) => {
    return new Promise((resolve, reject) => {
        $.ajax({
            type: 'GET',
            url: `${domain}/api/browse`,
            headers: { Secret: secret },
            success: (res) => { resolve(res) },
            error: (err) => { reject(err) }
        })
    })
}