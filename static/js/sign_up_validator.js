document.getElementById("sign_up_btn").addEventListener("click", sign_up);

function sign_up(){
    first_name = document.getElementById("first_name").value
    last_name = document.getElementById("last_name").value
    phone_numebr = document.getElementById("phone_number").value
    email_address = document.getElementById("email").value
    passowrd = document.getElementById("password").value
    conf_password = document.getElementById("conf_password").value

    if (validate_email(email_address) && validate_phone_numebr(phone_numebr) && is_pasword_matching(passowrd, conf_password)){
        new_user = {
            first_name: this.first_name,
            last_name: this.last_name,
            phone_numebr: this.phone_numebr,
            email_address: this.email_address,
            passowrd: this.passowrd,
            conf_password: this.conf_password
        }

        console.log("Done sign up")
        return new_user
    } else {
        console.log();
        return (false)
    }

}

function validate_email(email_address){
    if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email_address))
        return (true)
    else 
        return (false)
}

function validate_phone_numebr(phone_numebr){
    if (/^(010|011|015|012)([0-9]{8})/.test(phone_numebr))
        return (true)
    else 
        return (false)

}

function is_pasword_matching(passowrd, conf_password){
    if (passowrd == conf_password)
        return true
    else 
        return false
}