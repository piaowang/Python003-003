def attrs(**kwds):
    def decorate(f):
        for k in kwds:
            setattr(f, k, kwds[k])
        print(hasattr(f,"versionadded"))
        return f
    return decorate

@attrs(versionadded="2.2", author="Guido van Rossum")
class test():
    name = "xiaohua"
    def run(self):
     return "HelloWord"
t = test()
print(t.run())
setattr(t, "age", "18")
print(t.age)
m  = test()
print(m.run())
print(hasattr(m,"versionadded"))
print(hasattr(m,"author"))