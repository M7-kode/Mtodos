# Fonctionalités

- Lister le titre des notes à la page d'acceuil.  
    [x]Apres que l'utilisateur ai cliquer dessus cela redirige a une autres page.  
    [x]Page de présentation de  la note est présenter.
   

- Modifier ou supprimer la note :  
    [x]Suprimer le contenu de la note.  
    [x]Modifier le contenu de la note.


# Models

- NoteModel
    - titre = CharField() max-length = 100
    - slug = SlugField() slugify(self.name)
    - description = TextField()
    - date = DateTimeField()

# project so finished
