from audit.ssh import check_ssh_root_login
import json

def main():
    result = check_ssh_root_login()
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
