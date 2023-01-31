# Copyright © 2023, Mike Vermeer & Guido Erdtsieck, All rights reserved.

# Checks if the user is authenticated
def AuthCheck(request):
    if (request.user.is_authenticated):
        return("true")
    else:
        return("false")