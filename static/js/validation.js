function addcart(url,id)
{
    if(window.XMLHttpRequest)
    {
        xmlhttp = new XMLHttpRequest();
    }else
    {
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
        xmlhttp.onreadystatechange = function()
    {
        if(xmlhttp.readyState==4 && xmlhttp.status==200)
        {
        document.getElementById(id).innerHTML = xmlhttp.responseText;
        }
    }
xmlhttp.open("GET",url,true);
xmlhttp.send();
}
       function get_department(url,idVal,idTarget)
        {
            var value = document.getElementById(idVal).value;
            var url_loaded = url+"?"+"value="+value;
            //alert(url_loaded);
            document.getElementById(idTarget).innerHTML = "<option>Loading....</option>" 
            addcart(url_loaded,idTarget)
        }
        function validate_code(url,idVal,msg3)
        {
            var value = document.getElementById(idVal).value;
            var url_loaded = url+"?"+"value="+value;
            //alert(url_loaded);
            document.getElementById(msg3).innerHTML = "<span style:'color:#CCCCCC'></span>";
            addcart(url_loaded,msg3)
        }
        function validate_user(url,idVal,msg4)
        {
            var value = document.getElementById(idVal).value;
            var url_loaded = url+"?"+"value="+value;
            //alert(url_loaded);
            document.getElementById(msg4).innerHTML = "<span style:'color:#CCCCCC'></span>";
            addcart(url_loaded,msg4)
        }

        function validate(url,idVal,idTarget)
        {
            var value = document.getElementById(idVal).value;
            var url_loaded = url+"?"+"value="+value;
            //alert(url_loaded);
            document.getElementById(idTarget).innerHTML = "<option>Loading....</option>" 
            addcart(url_loaded,idTarget)
        }

    function verify_password(){
        var password = document.getElementById('password1').value;
        var confirm_password = document.getElementById('password2').value;
        if(confirm_password != ""){
            if(password != confirm_password){
                document.getElementById("msg").innerHTML = "<span style='color:brown; font-size:15px; font:italic'>Password not verified yet &nbsp;&nbsp;<i class=\"fa fa-close\" aria-hidden=\"true\"></i></span>";
            }
            else{
                document.getElementById("msg").innerHTML = "<span style='color:green; font-size:15px; font:italic'>Password Confirmed &nbsp;&nbsp; <i class=\"fa fa-check\" aria-hidden=\"true\"></i></span>";
            }
        }
    }
    function check_password_length(){
        var password = document.getElementById('password1').value;
        if(password.length < 6){
            document.getElementById("msg2").innerHTML = "<span style='color:brown; font-size:15px; font:italic'>Password length is weak &nbsp;&nbsp;<i class=\"fa fa-close\" aria-hidden=\"true\"></i></span>";
        }
        else if(password.length < 8){
            document.getElementById("msg2").innerHTML = "<span style='color:blue; font-size:15px; font:italic'>Password length is fair &nbsp;&nbsp;<i class=\"fa fa-check-square-o\" aria-hidden=\"true\"></i></span>";
        }
        else{
            document.getElementById("msg2").innerHTML = "<span style='color:green; font-size:15px; font:italic'>Password length is Good &nbsp;&nbsp;<i class=\"fa fa-check\"></i><i class=\"fa fa-check\"></i></span>";
        }
    }
    $("#password1").keyup(function(){
		var password = $("password1").val();
        if(password.length < 6){
            $("#msg2").innerHTML = "<span style='color:brown; font-size:15px; font:italic'>Password length is weak &nbsp;&nbsp;<i class=\"fa fa-close\" aria-hidden=\"true\"></i></span>";
        }
        else{
            $("#msg2").innerHTML = "<span style='color:green; font-size:15px; font:italic'>Password length is Good &nbsp;&nbsp;<i class=\"fa fa-close\" aria-hidden=\"true\"></i></span>"; 
        }
	});
    function confirmExeat(username){
        var conf;
        conf = confirm("Are you sure you want to confirm this Exeat? (NB: This cannot be reversed)");
        if(conf == true){
            $("#dataTables-example").load('confirm_exeat.php?username='+username);
        }
    }
    // Using checkbox
    function viewPassword(){
        let passView = document.getElementById("show").checked;
        let password = document.getElementById("pass");
        if(passView === true){
            password.setAttribute("type", "text");
            document.getElementById("chek").innerHTML = "<span>Hide Password<span>";
        }
        else{
            password.setAttribute("type", "password");
            document.getElementById("chek").innerHTML = "<span>Show Password<span>";
        }
    }
    // Using icon
    let passViews = false;
    function changePassView(){
        let password = document.getElementById("password");
        if(passViews === false){
            password.setAttribute("type", "text");
            passViews = true;
        }
        else{
            password.setAttribute("type", "password");
            passViews = false;
            // document.getElementById("show").innerHTML = "<i class=\"fa fa-eye-slash fa-lg\"></i>";
        }
    }