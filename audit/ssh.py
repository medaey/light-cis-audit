import re

def check_ssh_root_login():
    result = {
        "id": "SSH-001",
        "description": "SSH root login must be disabled (PermitRootLogin no)",
        "result": "FAIL",
        "details": "Unable to parse sshd_config or root login is allowed"
    }

    try:
        with open("/etc/ssh/sshd_config", "r") as f:
            lines = f.readlines()

        for line in lines:
            line = line.strip()
            if line.startswith("#"):
                continue
            match = re.match(r'^PermitRootLogin\s+(\S+)', line, re.IGNORECASE)
            if match:
                value = match.group(1).lower()
                if value == "no":
                    result["result"] = "PASS"
                    result["details"] = "PermitRootLogin is set to no"
                else:
                    result["details"] = f"PermitRootLogin is set to '{value}'"
                break
        else:
            result["details"] = (
                "PermitRootLogin directive not present — OpenSSH will use its default "
                "(often 'yes' — consider adding this directive explicitly)"
            )
            result["result"] = "WARN"


    except Exception as e:
        result["details"] = f"Error reading sshd_config: {str(e)}"
        result["result"] = "ERROR"

    return result
