from cryptography.fernet import Fernet

key = Fernet.generate_key()


def pseudonymize_names(names):
    f = Fernet(key)

    return [f.encrypt(name.encode()) for name in names]


def restore_names(encrypted):
    f = Fernet(key)
    decrypted_names = [f.decrypt(name).decode() for name in encrypted]
    return decrypted_names