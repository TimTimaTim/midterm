# A URL is generally written like: scheme://host/path... where the scheme is something like http or https, then ://, then a host (domain or IP), and optionally a path/query after that

def is_valid_url(url):
    # 1) Must start with a known scheme + ://
    if not (url.startswith("http://") or url.startswith("https://")):
        return False


    # 2) After scheme:// we must have a host (at least something before next /)
    # Split once on "://"
    parts = url.split("://")
    if len(parts) != 2:
        return False


    after = parts[1]  # host + path
    if after == "":
        return False


    # host ends at first "/" (if any)
    slash_pos = after.find("/")
    if slash_pos == -1:
        host = after
    else:
        host = after[:slash_pos]


    # 3) Host must not be empty and must not start/end with a dot
    if host == "":
        return False
    if host.startswith(".") or host.endswith("."):
        return False


    # 4) Very basic host check:
    # allow letters, digits, dots and hyphens (common in domains)
    allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-"
    for ch in host:
        if ch not in allowed:
            return False


    # 5) Host should contain at least one dot (like example.com)
    # (simple rule, not perfect for localhost)
    if "." not in host:
        return False


    return True




# quick tests
print(is_valid_url("https://google.com"))          # True
print(is_valid_url("http://example.com/path"))     # True
print(is_valid_url("ftp://example.com"))           # False (scheme not allowed here)
print(is_valid_url("https://"))                    # False (no host)
print(is_valid_url("https://exa mple.com"))        # False (space in host)