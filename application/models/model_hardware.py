import web
import config

db = config.db


def get_all_hardware():
    try:
        return db.select('hardware')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_hardware(id_hardware):
    try:
        return db.select('hardware', where='id_hardware=$id_hardware', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_hardware(id_hardware):
    try:
        return db.delete('hardware', where='id_hardware=$id_hardware', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_hardware(modelo,almacenamiento,memoria):
    try:
        return db.insert('hardware',modelo=modelo,
almacenamiento=almacenamiento,
memoria=memoria)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_hardware(id_hardware,modelo,almacenamiento,memoria):
    try:
        return db.update('hardware',id_hardware=id_hardware,
modelo=modelo,
almacenamiento=almacenamiento,
memoria=memoria,
                  where='id_hardware=$id_hardware',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
