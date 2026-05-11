from .supabase_client import supabase, supabase_auth


def register_user(email, password):
    return supabase_auth.auth.sign_up({
        "email": email,
        "password": password,
        "options": {
            "email_redirect_to": None,
        },
    })


def create_confirmed_user(email, password):
    return supabase.auth.admin.create_user({
        "email": email,
        "password": password,
        "email_confirm": True,
    })


def create_profile(profile_data):
    return supabase.table("profiles").insert(profile_data).execute()


def login_user(email, password):
    return supabase_auth.auth.sign_in_with_password({
        "email": email,
        "password": password
    })
