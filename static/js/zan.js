$(document).ready(function () {
    $(".col-md-2").dblclick(function () {
        window.location.href="/blogapp/comeon/"
    })
})

$(document).ready(function () {
    $(".fa-thumbs-up").click(function () {
        num = $(this).attr('id');
        $.ajax({
            url:"/blogapp/addzan/"+num+"/",
            success:function (result) {
                $(".fa-thumbs-up").html('&nbsp;'+result)

            }
        })
    })
})
$(document).ready(function () {
    $(".fa-thumbs-down").click(function () {
        num = $(this).attr('id');
        $.ajax({
            url:"/blogapp/addlow/"+num+"/",
            success:function (result) {
                $(".fa-thumbs-down").html('&nbsp;'+result)

            }
        })
    })
})
$(document).ready(function () {
    $('#but').click(function () {
        txt=$('#blogtxt').val();
        nums=$(this).attr('name');
        $.ajax({type:"POST",url:"/addpin/"+nums+"/", data: {txt:txt},
            success:function(result) {
                $("#blogtxt").val(result);
                alert("评论成功！")
            }
        })
    })
})