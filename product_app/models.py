import os, random, datetime
from django.db import models
from django.utils.translation import gettext_lazy as _
from PIL import Image


def photo_path(instance, filename):
    basefilename, file_extension= os.path.splitext(filename)
    date = datetime.datetime.now()
    return f'product_pics/{instance.prod_code}/{date}-{instance.prod_code}{file_extension}'

# class Category(models.Model):
#     """
#     Manage Product Category
#     """
#     categ_name = models.CharField(max_length=30)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.categ_name


PRODUCT_CATEGORY = [
    (0, _('Sofa')),
    (1, _('Sponge Sofa')),
    (2, _('Table')),
    (3, _('Chair')),
    (4, _('Curtain')),
    (5, _('Back Rest')),
    (6, _('Arm Rest')),
    (7, _('Pillow')),
]


class Product(models.Model):
    """
    Manage Product Information
    """
    prod_code = models.CharField(max_length=255, unique=True)
    category = models.IntegerField(choices=PRODUCT_CATEGORY, default=0)
    unit_price = models.PositiveIntegerField()
    updated_on = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.png', upload_to = photo_path)

    def __str__(self):
        return self.prod_code

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 600 or img.width > 800:
            output_size = (600, 800)
            img.thumbnail(output_size)
            img.save(self.image.path)
