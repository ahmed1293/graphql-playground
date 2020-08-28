from graphql import GraphQLError


def update_instance(instance, model_form, data):
    if not instance:
        raise GraphQLError("Object with given ID not found")

    form_data = {}
    for field in model_form.Meta.fields:
        form_data[field] = data.get(field, getattr(instance, field))
    form = model_form(data=form_data, instance=instance)

    if form.is_valid():
        form.save()
    return instance


def delete_instance(instance):
    if not instance:
        raise GraphQLError("Object with given ID not found")

    instance.delete()
    return instance
