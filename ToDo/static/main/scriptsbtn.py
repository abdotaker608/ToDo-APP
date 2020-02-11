from ToDo.main.models import ToDo


def delete(del_id):
    obj = ToDo.objects.get(id=del_id)
    obj.delete()