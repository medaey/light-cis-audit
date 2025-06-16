def to_markdown(results):
    """
    Convertit la liste de résultats en rapport Markdown.
    """
    lines = ["# Rapport d'audit light-cis-audit\n"]

    for res in results:
        status_emoji = {
            "PASS": "✅",
            "FAIL": "❌",
            "WARN": "⚠️",
            "ERROR": "🚨"
        }.get(res["result"], "ℹ️")

        lines.append(f"## {res['id']} {status_emoji}")
        lines.append(f"**Description:** {res['description']}")
        lines.append(f"**Statut:** {res['result']}")
        lines.append(f"**Détails:**\n```\n{res['details']}\n```")
        lines.append("---\n")

    return "\n".join(lines)
