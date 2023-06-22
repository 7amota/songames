def slugify(slug:str) ->str:
    slug = slug.lower()
    slug.replace(' ', '_')
    return slug
def get_key(request):
    req: dict = request.POST
    listquery = [str(x) for x in req.keys()]
    return listquery[1]