window.onload = add_article()
var parent_id = '0'
var user_to_article = '0'

function add_li(article)
{
    var ul = document.getElementById("the_idea");
    var i = 0;
    for(i=0;i<article.length;i++)
        {
            var s = article[i].article_id.toString();
            var user_id = article[i].user_id.toString();
            var li = document.createElement("li");
            li.setAttribute("id","li"+s);
            ul.appendChild(li);
            var li_parent = document.getElementById("li"+s);
            var p = document.createElement("span");
            p.setAttribute("id","pusername_"+s+"_"+user_id);
            p.innerHTML = article[i].user_name;
            li_parent.appendChild(p);
            var button = document.createElement("button");
            button.setAttribute("id","fbutton_"+s+'_'+user_id);
            button.setAttribute("onclick","focus_my(this.id)");
            button.innerHTML = "focus";
            li_parent.appendChild(button);
            var p = document.createElement("p");
            p.setAttribute("id","particle_"+s);
            p.innerHTML = article[i].article;
            li_parent.appendChild(p);
            var button = document.createElement("button");
            button.setAttribute("id","tbutton_"+s+'_'+user_id);
            button.setAttribute("onclick","transmit(this.id)");
            button.innerHTML = "transmit";
            li_parent.appendChild(button);
            var button = document.createElement("button");
            button.setAttribute("id","cbutton_"+s+'_'+user_id);
            button.setAttribute("onclick","collect(this.id)");
            button.innerHTML = "collect it";
            li_parent.appendChild(button)
            var button = document.createElement('button');
            button.setAttribute("id","cmbutton_"+s+'_'+user_id)
            button.setAttribute("onclick","add_comment(this.id)");
            button.innerHTML = "check comments"
            li_parent.appendChild(button)
            var p = document.createElement("p");
            p.setAttribute("id","ptime_"+s);
            p.innerHTML = article[i].time;
            li_parent.appendChild(p);
            var input = document.createElement("input");
            input.setAttribute("id","input_"+s+"_"+user_id);
            li_parent.appendChild(input);
            var button = document.createElement("button");
            button.setAttribute("id","pbutton_"+s+'_'+user_id);
            button.setAttribute("onclick","post_comment(this.id)");
            button.innerHTML = "submit";
            li_parent.appendChild(button);
        }
}

function comment_back(id)
{
    parent_id = id.split('_')[3];
    user_to_article = id.split('_')[5];
    var user_article = id.split('_')[4];
    var s = id.split('_')[1];
    var user_to_id = id.split('_')[2];
    var txt = document.getElementById("spanfrom_"+s+"_"+user_to_id+"_"+parent_id).innerHTML;
    var input = document.getElementById("input_"+s+'_'+user_article);
    input.placeholder = "@"+txt;
}
function post()
{
    var xmlhttp,response;
    var user_id,token,ideas;
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
    ideas = document.getElementById("my_thoughts").value;
    if (ideas == '')
        {
            alert("you have written the empty data");
        }
    else
        {
            xmlhttp.onreadystatechange = function()
            {
                if (xmlhttp.readyState == 4 && xmlhttp.status == 200)
                {
                    response=JSON.parse(xmlhttp.responseText);
                    if(response.result)
                    {
                        location.href = "log_in.html";
                    }
                }
            }
            xmlhttp.open("POST","my_thoughts",true);
            xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
            xmlhttp.send("user_id="+user_id+'&token='+token+'&article='+ideas);
        }
}

function add_article()
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
                        add_li(response);
                    }
                }
            }
            xmlhttp.open("POST","get_my_thoughts",true);
            xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
            xmlhttp.send("user_id="+user_id+'&token='+token);
}

function focus_my(id)
{
    var xmlhttp,response;
    var id_to;
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
                if(response.result)
                {
                        alert("successful");
                }
                else
                {
                    alert("you have focused on him");
                }
            }
        }
            xmlhttp.open("POST","focus",true);
            xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
            xmlhttp.send("user_id="+user_id+'&token='+token+'&id_to='+id);
}

function transmit(id)
{
    var xmlhttp,response;
    var id_to;
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
                if(response.result)
                {
                        alert("successful");
                }
                else
                {
                    alert("you have transit it");
                }
            }
        }
            xmlhttp.open("POST","transmit",true);
            xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
            xmlhttp.send("user_id="+user_id+'&token='+token+'&id_to='+id);
}

function collect(id)
{
    var xmlhttp,response;
    var id_to;
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
                if(response.result)
                {
                        alert("successful");
                }
                else
                {
                    alert("you have transit it");
                }
            }
        }
            xmlhttp.open("POST","collect",true);
            xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
            xmlhttp.send("user_id="+user_id+'&token='+token+'&id_to='+id);
}

function post_comment(id)
{
    var xmlhttp,response;
    var id_to;
    var id_temp = id.split('_');
    var comment_body;
    comment_body = document.getElementById('input_'+id_temp[1]+'_'+id_temp[2]).value;
    if(parent_id == '0')
        ;
    else
    {
        id = id_temp[0]+'_'+id_temp[1]+"_"+user_to_article;
    }
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
    if(comment_body == '')
    {
        alert('please input :');
    }
    else
    {
        xmlhttp.onreadystatechange = function()
        {
            if (xmlhttp.readyState == 4 && xmlhttp.status == 200)
            {
                response=JSON.parse(xmlhttp.responseText);
                if(response.result)
                {
                    location.href = 'log_in.html';
                }
                else
                {
                    alert("failure");
                }
                parent_id = '0';
                user_to_article = '0';
            }
        }
        xmlhttp.open("POST","post_comment",true);
        xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
        xmlhttp.send("user_id="+user_id+'&token='+token+'&id_to='+id+'&parent_id='+parent_id+'&comment_body='+comment_body);
    }
}

