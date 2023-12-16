const login_form = document.getElementById("login-form");

login_form.addEventListener("submit", (e) => {
    const form_data = new FormData(login_form);

    const email = form_data.get("login-email");
    const password = form_data.get("login-password");
    
    hash = password.hashCode();
    document.getElementById("login-password").value = hash;
});