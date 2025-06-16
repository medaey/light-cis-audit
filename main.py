import argparse
import json

from audit.ssh import check_ssh_root_login
from audit.users import check_users_without_password
from reports.markdown import to_markdown

AVAILABLE_CHECKS = {
    "ssh": [check_ssh_root_login],
    "users": [check_users_without_password],
}

def parse_args():
    parser = argparse.ArgumentParser(description="light-cis-audit: Audit système léger")
    parser.add_argument(
        "--check",
        nargs="+",
        help="Liste des modules à auditer (ex: ssh users). Par défaut, tous.",
        choices=AVAILABLE_CHECKS.keys(),
        default=None
    )
    parser.add_argument(
        "--output",
        choices=["json", "markdown"],
        default="json",
        help="Format de sortie (json par défaut)"
    )
    parser.add_argument(
        "--output-file",
        type=str,
        help="Chemin du fichier pour sauvegarder la sortie"
    )
    return parser.parse_args()

def main():
    args = parse_args()
    selected_checks = args.check if args.check else AVAILABLE_CHECKS.keys()

    results = []
    for check_group in selected_checks:
        checks = AVAILABLE_CHECKS.get(check_group, [])
        for check in checks:
            results.append(check())

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
