# Permissions and Groups Setup

This module demonstrates the implementation of custom permissions and groups in Django.

## Custom Permissions

In the `Article` model (`models.py`), we defined the following permissions:

- `can_view`: Can view articles
- `can_create`: Can create articles
- `can_edit`: Can edit articles
- `can_delete`: Can delete articles

## Groups and Permissions

We created the following groups:

- **Viewers**: Has `can_view` permission
- **Editors**: Has `can_view`, `can_create`, `can_edit` permissions
- **Admins**: Has all permissions including `can_delete`

## Views and Permission Enforcement

In `views.py`, the `@permission_required` decorator ensures users can only access views they have permission for.

## Testing

To test:
1. Create users via Django Admin.
2. Assign them to the appropriate group.
3. Log in and confirm their access is limited or permitted correctly.

## Setup Script

Use the provided `setup_groups.py` script to automatically create groups and assign permissions.

Run with:
```bash
python manage.py shell < advanced_features_and_security/setup_groups.py
