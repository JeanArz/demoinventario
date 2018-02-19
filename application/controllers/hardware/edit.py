import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass


    def GET(self, id_hardware, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_hardware) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/hardware') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_hardware, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_hardware) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/hardware') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    
    @staticmethod
    def GET_EDIT(id_hardware, **k):
        message = None # Error message
        id_hardware = config.check_secure_val(str(id_hardware)) # HMAC id_hardware validate
        result = config.model.get_hardware(int(id_hardware)) # search for the id_hardware
        result.id_hardware = config.make_secure_val(str(result.id_hardware)) # apply HMAC for id_hardware
        return config.render.edit(result, message) # render hardware edit.html

    @staticmethod
    def POST_EDIT(id_hardware, **k):
        form = config.web.input()  # get form data
        form['id_hardware'] = config.check_secure_val(str(form['id_hardware'])) # HMAC id_hardware validate
        # edit user with new data
        result = config.model.edit_hardware(
            form['id_hardware'],form['modelo'],form['almacenamiento'],form['memoria'],
        )
        if result == None: # Error on udpate data
            id_hardware = config.check_secure_val(str(id_hardware)) # validate HMAC id_hardware
            result = config.model.get_hardware(int(id_hardware)) # search for id_hardware data
            result.id_hardware = config.make_secure_val(str(result.id_hardware)) # apply HMAC to id_hardware
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/hardware') # render hardware index.html
