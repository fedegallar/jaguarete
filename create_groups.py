from django.contrib.auth.models import Group, Permission, ContentType

def create_groups():
    moderaror = Group.objects.get_or_create(name="Moderador")
    cliente = Group.objects.get_or_create(name="Usuario")
    if moderaror:
        print("Se ha creado el grupo moderador.")
    if cliente:
        print("Se ha creado el grupo Cliente.")

create_groups()

