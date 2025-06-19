import os
import stat
import pwd
import grp

def check_file_permissions():
    results = []

    FILES_TO_CHECK = [
        {
            "path": "/etc/passwd",
            "expected_mode": 0o644,
            "expected_user": "root",
            "expected_group": "root",
            "id": "PERM-001",
            "description": "Check permissions and ownership of /etc/passwd"
        },
        {
            "path": "/etc/shadow",
            "expected_mode": 0o640,
            "expected_user": "root",
            "expected_group": "shadow",
            "id": "PERM-002",
            "description": "Check permissions and ownership of /etc/shadow"
        },
        {
            "path": "/etc/group",
            "expected_mode": 0o644,
            "expected_user": "root",
            "expected_group": "root",
            "id": "PERM-003",
            "description": "Check permissions and ownership of /etc/group"
        },
        {
            "path": "/etc/gshadow",
            "expected_mode": 0o640,
            "expected_user": "root",
            "expected_group": "shadow",
            "id": "PERM-004",
            "description": "Check permissions and ownership of /etc/gshadow"
        },
        {
            "path": "/etc/sudoers",
            "expected_mode": 0o440,
            "expected_user": "root",
            "expected_group": "root",
            "id": "PERM-005",
            "description": "Check permissions and ownership of /etc/sudoers"
        }
    ]

    for file in FILES_TO_CHECK:
        result = {
            "id": file["id"],
            "description": file["description"],
            "result": "FAIL",
            "details": ""
        }

        path = file["path"]
        if not os.path.exists(path):
            result["result"] = "ERROR"
            result["details"] = f"File {path} does not exist."
            results.append(result)
            continue

        try:
            stat_info = os.stat(path)
            actual_mode = stat.S_IMODE(stat_info.st_mode)
            actual_user = pwd.getpwuid(stat_info.st_uid).pw_name
            actual_group = grp.getgrgid(stat_info.st_gid).gr_name

            mode_ok = actual_mode == file["expected_mode"]
            user_ok = actual_user == file["expected_user"]
            group_ok = actual_group == file["expected_group"]

            if mode_ok and user_ok and group_ok:
                result["result"] = "PASS"
                result["details"] = f"{path} has correct permissions and ownership"
            else:
                problems = []
                if not mode_ok:
                    problems.append(f"permissions {oct(actual_mode)} (expected {oct(file['expected_mode'])})")
                if not user_ok:
                    problems.append(f"user '{actual_user}' (expected '{file['expected_user']}')")
                if not group_ok:
                    problems.append(f"group '{actual_group}' (expected '{file['expected_group']}')")
                result["details"] = f"{path} has incorrect " + ", ".join(problems)

        except Exception as e:
            result["result"] = "ERROR"
            result["details"] = f"Exception while checking {path}: {str(e)}"

        results.append(result)

    return results
