from django.template.defaultfilters import slugify


def slug_generator(sender, instance, *args, **kwargs):
   ''' capitalize first letter of each word and generates slug '''

   instance.name = instance.name.title()
   slug = slugify(instance.name)
   exists = sender.objects.filter(slug=slug).exists()
   if not exists:
      instance.slug = slug
   else:
      instance.slug = "%s-%s" % (slug, instance.id)

