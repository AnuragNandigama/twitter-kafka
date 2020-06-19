
def delete_attribute(obj, key_list):
    attribute_none = [k for k,v in obj.__dict__.items() if v is None]
    attribute_deleted = [delattr(obj, a) for a in attribute_none]
    return obj