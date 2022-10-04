class Form:
    
    def to_dict(self):
        raise NotImplementedError
    
    def get_validation_attrs(self):
        attrs = []
        for attr in dir(self):
            if attr.startswith("validate_"):
                attrs.append(attr)
        return attrs

    def is_valid(self):
        l = []
        for attr in self.get_validation_attrs():
            if hasattr(self, attr):
                fn = getattr(self, attr)
                l.append(fn())
        return all(l)
