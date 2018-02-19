import web
import config

db = config.db


def get_all_software():
    try:
        return db.select('software')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_software(id_software):
    try:
        return db.select('software', where='id_software=$id_software', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_software(id_software):
    try:
        return db.delete('software', where='id_software=$id_software', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_software(nombre,no_serie,precio):
    try:
        return db.insert('software',nombre=nombre,
no_serie=no_serie,
precio=precio)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_software(id_software,nombre,no_serie,precio):
    try:
        return db.update('software',id_software=id_software,
nombre=nombre,
no_serie=no_serie,
precio=precio,
                  where='id_software=$id_software',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
