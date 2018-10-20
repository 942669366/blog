$(document).ready(function () {
    $('#addbut').click(function () {
        window.location.href="/blogapp/add/"
    })
})
$(document).ready(function () {
    $('#delbut').click(function () {
        num = $(this).attr('name');
        window.location.href="/blogapp/dele/"+num+"/"
    })
})


