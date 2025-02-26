from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    prep_time = models.PositiveIntegerField()
    cook_time = models.PositiveIntegerField()
    servings = models.PositiveIntegerField()

    def __str__(self):
        return self.name


"""
What makes a RESTful API RESTful?

SOAP - XML ... bespoke 
<soap>
    <field> 
    </field>
</soap>

GET     /recipes  - all the recipes (paginated ... )
POST    /recipes  - create a new recipe

GET    /recipes/id  - get the particular one
PATCH  /recipes/id  - partially update a particular one
DELETE /recipes/id  - delete a particular
PUT    /recipes/id  - replace a particular
"""