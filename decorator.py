#decorators in python

def login_required(f1):
    def wrapperr(name, is_login):  #this  function will be repeating in below function instead of writing seperately we have wrapped.
        if is_login == False:  #if this condition gets  false it returns to the f1 
            print('kindly login')
            return
        return f1(name, is_login)
    return wrapperr
    
@login_required 
def home(name, is_login):
    print('welcoem to home page of our website')

@login_required
def orders(name, is_login):
    print('welcoem to orders page of our website')
    

def about():
    print('welcome to about section of our website')
home('azhar', True)
orders('azhar', False)
about()