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
                    add_li_two(response);
                }
                else
                {
                    alert("you have no friends you have focused on!!!");
                }
            }
        }
            xmlhttp.open("POST","check_focus",true);
            xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
            xmlhttp.send("user_id="+user_id+'&token='+token);
}

function add_li_two(focus_who)
{
    var ul = document.getElementById("the_idea");
    var i = 0;
    for(i=0;i<focus_who.length;i++)
    {
        var s = focus_who[i].focus_to.toString();
        var li = document.createElement("li");
        li.setAttribute("id","li" + s);
        ul.appendChild(li);
        var li_parent = document.getElementById("li"+s);
        var span = document.createElement("span");
        span.setAttribute("id","span_" + s);
        span.innerHTML = focus_who[i].user_name;
        li_parent.appendChild(span);
        var button = document.createElement("button");
        button.setAttribute("id","button_"+s);
        button.setAttribute("onclick","check_person(this.id)")
        button.innerHTML = "check"
        li_parent.appendChild(button);
    }
}

function check_person(id)
{
    var xmlhttp,response;
    var user_id,token;
    if(window.XMLHttpRequest)
    {
        xmlhttp = new XMLHttpRequest();
    }
    else
    {
        xmlhttp = new ActiveXObject();
    }
    var arr = document.cookie.split(' ');
    user_id = arr[1]
    token = arr[0].split('=')[1]
    xmlhttp.onreadystatechange = function()
    {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200)
        {
            response = JSON.parse(xmlhttp.responseText);
            if(response)
            {
                document.getElementById("the_idea").innerHTML = '';
                add_li(response);
            }
        }
    }
    xmlhttp.open("POST","check_person",true);
    xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xmlhttp.send("user_id="+user_id+"&token="+token+"&check_id="+id);
}
