import web
import config
import json


class Api_software:
    def get(self, id_software):
        try:
            # http://0.0.0.0:8080/api_software?user_hash=12345&action=get
            if id_software is None:
                result = config.model.get_all_software()
                software_json = []
                for row in result:
                    tmp = dict(row)
                    software_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(software_json)
            else:
                # http://0.0.0.0:8080/api_software?user_hash=12345&action=get&id_software=1
                result = config.model.get_software(int(id_software))
                software_json = []
                software_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(software_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            software_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(software_json)

# http://0.0.0.0:8080/api_software?user_hash=12345&action=put&id_software=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, nombre,no_serie,precio):
        try:
            config.model.insert_software(nombre,no_serie,precio)
            software_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(software_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_software?user_hash=12345&action=delete&id_software=1
    def delete(self, id_software):
        try:
            config.model.delete_software(id_software)
            software_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(software_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_software?user_hash=12345&action=update&id_software=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_software, nombre,no_serie,precio):
        try:
            config.model.edit_software(id_software,nombre,no_serie,precio)
            software_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(software_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            software_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(software_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_software=None,
            nombre=None,
            no_serie=None,
            precio=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_software=user_data.id_software
            nombre=user_data.nombre
            no_serie=user_data.no_serie
            precio=user_data.precio
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_software)
                elif action == 'put':
                    return self.put(nombre,no_serie,precio)
                elif action == 'delete':
                    return self.delete(id_software)
                elif action == 'update':
                    return self.update(id_software, nombre,no_serie,precio)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
