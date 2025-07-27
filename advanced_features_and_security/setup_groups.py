from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from accounts.models import Article# assuming models.py and setup_groups.py in same folder

# Get content type for Article model
content_type = ContentType.objects.get_for_model(Article)

# Define permissions
permissions = {
    "can_view": Permission.objects.get(codename="can_view", content_type=content_type),
    "can_create": Permission.objects.get(codename="can_create", content_type=content_type),
    "can_edit": Permission.objects.get(codename="can_edit", content_type=content_type),
    "can_delete": Permission.objects.get(codename="can_delete", content_type=content_type),
}

# Create groups and assign permissions
group_permissions = {
    "Viewers": ["can_view"],
    "Editors": ["can_view", "can_create", "can_edit"],
    "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
}

for group_name, perms in group_permissions.items():
    group, created = Group.objects.get_or_create(name=group_name)
    group.permissions.set([permissions[perm] for perm in perms])
    group.save()

print("Groups and permissions created successfully.")                                            
