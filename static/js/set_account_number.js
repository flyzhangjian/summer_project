function check()
{
    var xmlhttp,response;
    var account_number,password,name,confirm_it;
    if (window.XMLHttpRequest)
        {
            xmlhttp = new XMLHttpRequest();
        }
    else
        {
            xmlhttp = new ActiveXObject();
        }
    account_number = document.getElementById("account_number").value;
    password = document.getElementById("password").value;
    name = document.getElementById("name").value;
    confirm_it = document.getElementById("confirm_it").value;
    if (account_number == '' || password==''||name==''||confirm_it=='')
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
                        location.href = "zhuye.html";
                }
            }
            xmlhttp.open("POST","/set/set_account_number",true);
            xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
            xmlhttp.send("account_number="+account_number+'&password='+password+'&confirm_it='+confirm_it+'&name='+name);
        }
}
