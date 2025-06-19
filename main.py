import argparse
import json

from audit.ssh import check_ssh_root_login
from audit.users import check_users_without_password
from audit.permissions import check_file_permissions
from reports.markdown import to_markdown


AVAILABLE_CHECKS = {
    "ssh": [check_ssh_root_login],
    "users": [check_users_without_password],
    "permissions": [check_file_permissions],
}

def parse_args():
    parser = argparse.ArgumentParser(description="light-cis-audit: Audit système léger")

    parser.add_argument(
        "--check",
        nargs="+",
        choices=AVAILABLE_CHECKS.keys(),
        default=None,
        help="Liste des modules à auditer (ex: ssh users). Par défaut, tous les modules sont audités."
    )

    parser.add_argument(
        "--output",
        choices=["json", "markdown"],
        default="json",
        help="Format de sortie du rapport (json par défaut)."
    )

    parser.add_argument(
        "--output-file",
        type=str,
        help="Chemin du fichier pour sauvegarder le rapport. Si non spécifié, le rapport est affiché dans la console."
    )

    return parser.parse_args()

def main():
    args = parse_args()
    selected_checks = args.check if args.check else AVAILABLE_CHECKS.keys()

    results = []
    for check_group in selected_checks:
        checks = AVAILABLE_CHECKS.get(check_group, [])
        for check in checks:
            res = check()
            if isinstance(res, list):
                results.extend(res)
            else:
                results.append(res)

    if args.output == "markdown":
        output_data = to_markdown(results)
    else:
        output_data = json.dumps(results, indent=2)

    if args.output_file:
        try:
            with open(args.output_file, "w", encoding="utf-8") as f:
                f.write(output_data)
            print(f"Rapport sauvegardé dans {args.output_file}")
        except Exception as e:
            print(f"Erreur lors de la sauvegarde du fichier : {e}")
    else:
        print(output_data)

if __name__ == "__main__":
    main()
