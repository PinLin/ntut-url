'use strict'

let domain = (new URL(location.href)).origin

const refreshView = (url) => {
    let view = $('#urlBox .urls')

    view.append(newUrl(url))
}

const newUrl = (data) => {
    return $(`
        <div class="url row">
            <a class="text-center col-sm-6" href="/${data.name}" target="_blank">${data.name}</a>
            <a class="text-center col-sm-6" href="${data.target}" target="_blank">${data.target}</a>
        </div>
    `)
}

const createUrl = async () => {
    let name = $('#urlBox .name')[0].value || null
    let target = $('#urlBox .target')[0].value

    if (!target) {
        alert("Please enter url.")
        return
    }

    try {
        let res = await callCreate(name, target)
        console.log(res)
        refreshView(res.result)
    }
    catch (err) {
        console.log(err)

        if (err.status == 403) {
            alert("The alias was used!")
            return
        }

        alert("Unable to establish connection.")
    }
}

const callCreate = (name, target) => {
    return new Promise((resolve, reject) => {
        $.ajax({
            type: 'POST',
            dataType: 'json',
            url: `${domain}/api/create`,
            data: JSON.stringify({ name, target }),
            processData: false,
            contentType: 'application/json; charset=UTF-8',
            success: (res) => { resolve(res) },
            error: (err) => { reject(err) }
        })

    })
}
