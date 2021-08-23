from django.db import models
from django.db.models.deletion import CASCADE

class Compo(models.Model):

    type_of_compo = models.CharField(max_length=50)
    val = models.CharField(max_length=50)
    style = models.CharField(max_length=50)
    nodes = models.CharField(max_length=50, default="systems")

    def save(self, *args, **kwargs):
        self.nodes = "system"
        super(Compo, self).save(*args, **kwargs)

    def __str__(self):
        return self.type_of_compo+"  "+self.val+"  "+self.style

class Page(models.Model):

    compo = models.ManyToManyField(Compo, through='PageCompoMap')
    name = models.CharField(max_length=50, default= 'welcome')

    def __str__(self):
       return "page name="+self.name

class PageCompoMap(models.Model):
    page = models.ForeignKey(Page, on_delete=CASCADE)
    compo = models.ForeignKey(Compo, on_delete=CASCADE)
    prefix = models.CharField(max_length=100)
    
    def __str__(self):
        return "{}_{}".format(self.page.__str__(), self.compo.__str__())


