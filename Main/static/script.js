const body = document.getElementById("body");
const login = document.getElementById("btn_login");
const signup = document.getElementById("btn_signup");
const closelogin = document.getElementById("closelogin");
const closesignup = document.getElementById("closesignup");

const login_form = document.getElementById("login_form");
const signup_form = document.getElementById("signup_form");
const signin_signup = document.getElementById("signin_signup");

const loginFormFunction = () => {
    if (login_form.style.display === "none") {
        login_form.style.display = "block";
        signin_signup.style.display = "none";

    } else {
        login_form.style.display = "none";
        signin_signup.style.display = "block";
    }
} 

const signupFormFunction = () => {
    if (signup_form.style.display === "none") {
        signup_form.style.display = "block";
        signin_signup.style.display = "none";

    } else {
        signup_form.style.display = "none";
        signin_signup.style.display = "block";
    }
} 

const closeFunction = () =>{
	login_form.style.display = "none";
	signup_form.style.display = "none";
	signin_signup.style.display = "block";
}

// const resetF = () =>{
// 	x.style.display = "block";
// 	signin_signup.style.display = "block";
// }

login.addEventListener("click",loginFormFunction);
signup.addEventListener("click",signupFormFunction);
closelogin.addEventListener("click",closeFunction);
closesignup.addEventListener("click",closeFunction);
 //body.addEventListener("click",resetF);