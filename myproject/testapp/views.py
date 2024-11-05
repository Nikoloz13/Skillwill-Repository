import logging
from django.http import HttpResponse

logger = logging.getLogger('myproject')

def error_view(request):
    logger.debug("Debugging error_view function.")
    logger.info("Attempting to divide by zero.")
    try:
        result = 1 / 0  # I have created error to test the debugging system (divide by zero)
    except ZeroDivisionError as e:
        logger.error("Error occurred in error_view: %s", e)
    return HttpResponse("This view has an intentional error.")


