document.getElementById("sign_up_btn").addEventListener("click", sign_up);

function sign_up(){
    first_name = document.getElementById("first_name").value
    last_name = document.getElementById("last_name").value
    phone_number = document.getElementById("phone_number").value
    email_address = document.getElementById("email").value
    password = document.getElementById("password").value
    conf_password = document.getElementById("conf_password").value

    if (first_name.length == 0 || last_name.length == 0 || phone_number.length == 0 || email_address.length == 0 || password == 0 || conf_password == 0 ){
        return (false)
    } else {
            if (validate_email(email_address) && validate_phone_number(phone_number) && is_password_matching(password, conf_password)){
                new_user = {
                    first_name: this.first_name,
                    last_name: this.last_name,
                    phone_number: this.phone_number,
                    email_address: this.email_address,
                    password: this.password,
                    conf_password: this.conf_password
                }

                alert("Check your email to activate your account.")
                $.ajax({
                    type: "GET",
                      url: "/signup.py",
                      data: { param: new_user}
                })
                return new_user
            } else {
                alert("Invalid inputs")
                return (false)
            }
    }
}

function validate_email(email_address){
    if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email_address))
        return (true)
    else 
        return (false)
}

function validate_phone_number(phone_number){
    if (/^(010|011|015|012)([0-9]{8})/.test(phone_number))
        return (true)
    else 
        return (false)

}

function is_password_matching(password, conf_password){
    if (password == conf_password)
        return true
    else 
        return false
}