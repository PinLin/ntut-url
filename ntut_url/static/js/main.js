'use strict'

let domain = (new URL(location.href)).origin

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

        refreshView(res.results)

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

const refreshView = (urls) => {
    let view = $('#urlBox .urls')

    view.empty()

    view.append(newTitle())

    urls.forEach((url) => {
        view.append(newUrl(url))
    })

    view.append(newUrlAdder())
}

const newTitle = () => {
    return $(`
        <div class="url row">
            <h3 class="text-center col-sm-6">Name</h3>
            <h3 class="text-center col-sm-6">Target</h3>
        </div>
    `)
}

const newUrl = (data) => {
    return $(`
        <div class="url row">
            <a class="text-center col-sm-6" href="/${data.name}" target="_blank">${data.name}</a>
            <a class="text-center col-sm-6" href="${data.target}" target="_blank">${data.target}</a>
        </div>
    `)
}

const newUrlAdder = () => {
    return $(`
        <div class="url row">
            <input class="name text-center col-sm-6" name="name" type="text" placeholder="Enter the name.">
            <input class="target text-center col-sm-6" name="target" type="text" placeholder="Enter the target.">
            <a class="btn btn-primary col-12" href="javascript:" onclick="createUrl()">Create</a>
        </div>
    `)
}

const createUrl = async () => {
    let secret = $('#loginBox .secret input')[0].value
    let name = $('#urlBox .name')[0].value
    let target = $('#urlBox .target')[0].value

    if (!secret) {
        alert("Verification failed.")
        return
    }

    if (!name || !target) {
        alert("Please enter url information.")
        return
    }

    try {
        let res = await callCreate(secret, name, target)
        console.log(res)

        res = await callBrowse(secret)
        console.log(res)

        refreshView(res.results)
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

const callCreate = (secret, name, target) => {
    return new Promise((resolve, reject) => {
        $.ajax({
            type: 'POST',
            dataType: 'json',
            url: `${domain}/api/create`,
            headers: { Secret: secret },
            data: JSON.stringify({ name, target }),
            processData: false,
            contentType: 'application/json; charset=UTF-8',
            success: (res) => { resolve(res) },
            error: (err) => { reject(err) }
        })

    })
}
