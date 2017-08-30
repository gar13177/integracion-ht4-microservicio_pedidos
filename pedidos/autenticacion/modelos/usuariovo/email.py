class EmailError(Exception):
    def __init__(self):#, errors):
        message = "email no tiene un formato valido"
        super(EmailError, self).__init__(message)
        #self.errors = errors


class Email(object):
    def __init__(self, email_string):
        """if not ('@' in email_string):
            raise EmailError()
        
        if len(email_string) <= 1:
            raise EmailError()
        
        email_array = email_string.split('@')

        if len(email_array[0]) <= 0 or len(email_array[1]) <= 0:
            raise EmailError()

        self.user = email_array[0]
        self.domain = email_array[1]"""
        self.user = email_string
        self.domain = 'app.com'

    def __str__(self):
        return str(self.user)+"@"+str(self.domain)

    def usuario(self):
        return self.user 

    def dominio(self):
        return self.domain
