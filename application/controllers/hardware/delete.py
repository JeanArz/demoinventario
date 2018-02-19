import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    
    def GET(self, id_hardware, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_hardware) # call GET_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_hardware, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_hardware) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    
    @staticmethod
    def GET_DELETE(id_hardware, **k):
        message = None # Error message
        id_hardware = config.check_secure_val(str(id_hardware)) # HMAC id_hardware validate
        result = config.model.get_hardware(int(id_hardware)) # search  id_hardware
        result.id_hardware = config.make_secure_val(str(result.id_hardware)) # apply HMAC for id_hardware
        return config.render.delete(result, message) # render delete.html with user data

    @staticmethod
    def POST_DELETE(id_hardware, **k):
        form = config.web.input() # get form data
        form['id_hardware'] = config.check_secure_val(str(form['id_hardware'])) # HMAC id_hardware validate
        result = config.model.delete_hardware(form['id_hardware']) # get hardware data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_hardware = config.check_secure_val(str(id_hardware))  # HMAC user validate
            id_hardware = config.check_secure_val(str(id_hardware))  # HMAC user validate
            result = config.model.get_hardware(int(id_hardware)) # get id_hardware data
            result.id_hardware = config.make_secure_val(str(result.id_hardware)) # apply HMAC to id_hardware
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/hardware') # render hardware delete.html 
