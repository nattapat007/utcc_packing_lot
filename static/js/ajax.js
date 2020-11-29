$(document).ready(function () {
    let csrf = $("")

    $("#checkin").on('click', 'li', function () {
        $.ajax({
            url: 'http://localhost:8000/api/checkin/',
            type: 'post',
            data: {
                face_login: "",
                plate: "",
            },
            success: function (res) {
                console.log(res)
            }
        })
    })
})