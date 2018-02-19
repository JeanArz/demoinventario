import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    
    def GET(self, id_software, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_software) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/software') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_software, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_software) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/software') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    

    @staticmethod
    def GET_EDIT(id_software, **k):
        message = None # Error message
        id_software = config.check_secure_val(str(id_software)) # HMAC id_software validate
        result = config.model.get_software(int(id_software)) # search for the id_software
        result.id_software = config.make_secure_val(str(result.id_software)) # apply HMAC for id_software
        return config.render.edit(result, message) # render software edit.html


    @staticmethod
    def POST_EDIT(id_software, **k):
        form = config.web.input()  # get form data
        form['id_software'] = config.check_secure_val(str(form['id_software'])) # HMAC id_software validate
        # edit user with new data
        result = config.model.edit_software(
            form['id_software'],form['nombre'],form['no_serie'],form['precio'],
        )
        if result == None: # Error on udpate data
            id_software = config.check_secure_val(str(id_software)) # validate HMAC id_software
            result = config.model.get_software(int(id_software)) # search for id_software data
            result.id_software = config.make_secure_val(str(result.id_software)) # apply HMAC to id_software
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/software') # render software index.html
