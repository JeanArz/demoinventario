import web
import config
import json


class Api_hardware:
    def get(self, id_hardware):
        try:
            # http://0.0.0.0:8080/api_hardware?user_hash=12345&action=get
            if id_hardware is None:
                result = config.model.get_all_hardware()
                hardware_json = []
                for row in result:
                    tmp = dict(row)
                    hardware_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(hardware_json)
            else:
                # http://0.0.0.0:8080/api_hardware?user_hash=12345&action=get&id_hardware=1
                result = config.model.get_hardware(int(id_hardware))
                hardware_json = []
                hardware_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(hardware_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            hardware_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(hardware_json)

# http://0.0.0.0:8080/api_hardware?user_hash=12345&action=put&id_hardware=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, modelo,almacenamiento,memoria):
        try:
            config.model.insert_hardware(modelo,almacenamiento,memoria)
            hardware_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(hardware_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_hardware?user_hash=12345&action=delete&id_hardware=1
    def delete(self, id_hardware):
        try:
            config.model.delete_hardware(id_hardware)
            hardware_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(hardware_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_hardware?user_hash=12345&action=update&id_hardware=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_hardware, modelo,almacenamiento,memoria):
        try:
            config.model.edit_hardware(id_hardware,modelo,almacenamiento,memoria)
            hardware_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(hardware_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            hardware_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(hardware_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_hardware=None,
            modelo=None,
            almacenamiento=None,
            memoria=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_hardware=user_data.id_hardware
            modelo=user_data.modelo
            almacenamiento=user_data.almacenamiento
            memoria=user_data.memoria
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_hardware)
                elif action == 'put':
                    return self.put(modelo,almacenamiento,memoria)
                elif action == 'delete':
                    return self.delete(id_hardware)
                elif action == 'update':
                    return self.update(id_hardware, modelo,almacenamiento,memoria)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
