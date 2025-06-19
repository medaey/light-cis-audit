# Rapport d'audit light-cis-audit

## SSH-001 ✅
**Description:** SSH root login must be disabled (PermitRootLogin no)
**Statut:** PASS
**Détails:**
```
PermitRootLogin is set to no
```
---

## USER-001 ✅
**Description:** No user account should have an empty password
**Statut:** PASS
**Détails:**
```
All accounts have non-empty password fields
```
---

## PERM-001 ✅
**Description:** Check permissions and ownership of /etc/passwd
**Statut:** PASS
**Détails:**
```
/etc/passwd has correct permissions and ownership
```
---

## PERM-002 ✅
**Description:** Check permissions and ownership of /etc/shadow
**Statut:** PASS
**Détails:**
```
/etc/shadow has correct permissions and ownership
```
---

## PERM-003 ✅
**Description:** Check permissions and ownership of /etc/group
**Statut:** PASS
**Détails:**
```
/etc/group has correct permissions and ownership
```
---

## PERM-004 ✅
**Description:** Check permissions and ownership of /etc/gshadow
**Statut:** PASS
**Détails:**
```
/etc/gshadow has correct permissions and ownership
```
---

## PERM-005 ✅
**Description:** Check permissions and ownership of /etc/sudoers
**Statut:** PASS
**Détails:**
```
/etc/sudoers has correct permissions and ownership
```
---
