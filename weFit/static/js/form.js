function validation(){
    if(document.Formfill.username.value == ""){
        document.getElementById("result").innerHTML="Enter Username*";
        return false;
    }
    else if(document.Formfill.email.value == ""){
        document.getElementById("result").innerHTML="Enter your Email*";
        return false;
    }
    else if(document.Formfill.weight.value == ""){
        document.getElementById("result").innerHTML="Enter your weight*";
        return false;
    }
    else if(document.Formfill.height.value == ""){
        document.getElementById("result").innerHTML="Enter your height*";
        return false;
    }
    else if(document.Formfill.dob.value == ""){
        document.getElementById("result").innerHTML="Enter your birth date*";
        return false;
    }
    else if(document.Formfill.password.value == ""){
        document.getElementById("result").innerHTML="Enter a password*";
        return false;
    }
    else if(document.Formfill.password.value.length < 6){
        document.getElementById("result").innerHTML="Password must be atleast 6 characters*";
        return false;
    }
    else if(document.Formfill.password.value !== document.Formfill.confirm-password.value){
        document.getElementById("result").innerHTML="Password does not match*";
        return false;
    }
    else if(document.Formfill.password.value == document.Formfill.confirm-password.value){
        popup.classList.add("open-slide")
        return false;
    }
}
var popup = document.getElementById('popup');