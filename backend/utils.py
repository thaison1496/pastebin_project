import secrets

def generate_random_paste_id():
    # Sample output: 580730cbddc4e65dfb971bc3
    # Need to find method to produce shorter id, and run faster, while have unique property
    return secrets.token_hex(12)


def shorten_paste_content(content: str):
    if len(content) > 20:
        return content[:20] + ' ...'
    return content