def check_users_without_password():
    result = {
        "id": "USER-001",
        "description": "No user account should have an empty password",
        "result": "PASS",
        "details": []
    }

    try:
        with open("/etc/shadow", "r") as f:
            lines = f.readlines()

        flagged_users = []

        for line in lines:
            parts = line.strip().split(":")
            if len(parts) < 2:
                continue  # ligne malformée
            username, passwd = parts[0], parts[1]

            if passwd == "":
                flagged_users.append(username)

        if flagged_users:
            result["result"] = "FAIL"
            result["details"] = f"Users with empty passwords: {', '.join(flagged_users)}"
        else:
            result["details"] = "All accounts have non-empty password fields"

    except Exception as e:
        result["result"] = "ERROR"
        result["details"] = f"Error reading /etc/shadow: {str(e)}"

    return result
