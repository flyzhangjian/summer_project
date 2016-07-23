function add_comment(id)
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
    user_id = arr[1];
    token = arr[0].split('=')[1];
    xmlhttp.onreadystatechange = function()
        {
            if (xmlhttp.readyState == 4 && xmlhttp.status == 200)
            {
                response=JSON.parse(xmlhttp.responseText);
                if(response)
                {
                    add__comment(response);
                }
                else
                {
                    alert("there is no comments on it");
                }
            }
        }
            xmlhttp.open("POST","comment",true);
            xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
            xmlhttp.send("user_id="+user_id+'&token='+token+"&id_to="+id);
}

function add__comment(response)
{
    var i = 0;
    for(i=0;i<response.length;i++)
    {
        s = response[i].article_id.toString();
        user_to_id = response[i].coment_to_id.toString();
        comment_to_id = response[i].comment_id.toString();
        user_article = response[i].user_article.toString();
        comment_from_id = response[i].coment_from_id.toString();
        var li = document.getElementById("li"+s);
        var div = document.createElement("div");
        div.setAttribute("id","div"+s);
        li.appendChild(div);
        var div_ = document.getElementById("div"+s);
        var span = document.createElement("span");
        span.setAttribute("id","spanfrom_"+s+"_"+user_to_id+"_"+comment_to_id);
        span.setAttribute("onclick","comment_back(this.id)");
        span.innerHTML = response[i].comment_from_name;
        div_.appendChild(span);
        var span = document.createElement("span");
        span.innerHTML = "@"
        div_.appendChild(span)
        var span = document.createElement("span");
        span.setAttribute("id","spanto_"+s+"_"+user_to_id+"_"+comment_to_id);
        span.innerHTML = response[i].comment_to_name;
        div_.appendChild(span);
        var span = document.createElement("span");
        span.setAttribute("id","pcoment_"+s+"_"+user_to_id+'_'+comment_to_id);
        span.innerHTML = "    "+response[i].comment_body
        div_.appendChild(span);
        var button = document.createElement("button");
        button.setAttribute("id","button_"+s+"_"+user_to_id+"_"+comment_to_id+"_"+user_article+"_"+comment_from_id);
        button.setAttribute("onclick","comment_back(this.id)");
        button.innerHTML = "back";
        div_.appendChild(button);
        var br = document.createElement("br");
        div_.appendChild(br);
   }
}

