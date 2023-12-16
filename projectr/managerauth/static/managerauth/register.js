const register_form = document.getElementById("register-form");

register_form.addEventListener("submit", (e) => {
    const form_data = new FormData(register_form);

    const name = form_data.get("register-name");
    const email = form_data.get("register-email");
    const password = form_data.get("register-password");
    const confirmation = form_data.get("register-confirmation");

    if (password != confirmation) {
        e.preventDefault();
        alert("Password and confirmation does not match!");
    }
    else {
        hash = password.hashCode();
        // alert(hash)
        document.getElementById("register-password").value = hash;
    }
});