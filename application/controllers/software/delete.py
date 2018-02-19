import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass


    def GET(self, id_software, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_software) # call GET_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_software, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_software) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    
    @staticmethod
    def GET_DELETE(id_software, **k):
        message = None # Error message
        id_software = config.check_secure_val(str(id_software)) # HMAC id_software validate
        result = config.model.get_software(int(id_software)) # search  id_software
        result.id_software = config.make_secure_val(str(result.id_software)) # apply HMAC for id_software
        return config.render.delete(result, message) # render delete.html with user data

    @staticmethod
    def POST_DELETE(id_software, **k):
        form = config.web.input() # get form data
        form['id_software'] = config.check_secure_val(str(form['id_software'])) # HMAC id_software validate
        result = config.model.delete_software(form['id_software']) # get software data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_software = config.check_secure_val(str(id_software))  # HMAC user validate
            id_software = config.check_secure_val(str(id_software))  # HMAC user validate
            result = config.model.get_software(int(id_software)) # get id_software data
            result.id_software = config.make_secure_val(str(result.id_software)) # apply HMAC to id_software
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/software') # render software delete.html 
