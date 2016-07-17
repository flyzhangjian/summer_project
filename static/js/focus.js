window.onload = add_focus()

function add_focus()
{
    var xmlhttp,response;
    if (window.XMLHttpRequest)
        {
            xmlhttp = new XMLHttpRequest();
        }
    else
        {
            xmlhttp = new ActiveXObject();
        }
    var arr = document.cookie.split(' ');
    var i = 0;
    user_id = arr[1]
    token = arr[0].split('=')[1]
    xmlhttp.onreadystatechange = function()
        {
            if (xmlhttp.readyState == 4 && xmlhttp.status == 200)
            {
                response=JSON.parse(xmlhttp.responseText);
                if(response)
                {
                        alert("successful");
                }
                else
                {
                    alert("you have transit it");
                }
            }
        }
            xmlhttp.open("POST","check_focus",true);
            xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
            xmlhttp.send("user_id="+user_id+'&token='+token);
}

