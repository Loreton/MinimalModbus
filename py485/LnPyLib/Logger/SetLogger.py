
import os
import inspect
import sys, logging

class LnClass(): pass

from . LnLogger_Class import LnLogger


# ====================================================================================
# - dal package passato come parametro cerchiamo di individuare se la fuzione/modulo
# - è tra quelli da fare il log.
# - Il package mi server per verficare se devo loggare il modulo o meno
# ====================================================================================
def SetLogger(package, exiting=False, offsetSL=0):

    pointers = LnLogger.static_getMainPointers()
        # importante prendere questo pointer in quanto mi porta dietro anche i .info, .debug, ...
    logger = pointers.ClassInstance

    fDEBUG = False
    if fDEBUG:
        print('     rootName      = ', logger._name)
        print('     realLogger    = ', logger._realLogger)
        print('     ClassInstance = ', logger)
        print('     LnFilter      = ', logger._LnFilter)
        print('     modulesToLog  = ', logger._modulesToLog)
        print('     logLevel      = ', logger._logLevel)
        print('     nullLogger    = ', logger._nullLogger)


    caller_01 = GetCaller(1)


        # ---------------------------------
        # - individuiamo se è un modulo
        # - da tracciare o meno
        # ---------------------------------
    fullPkg = (package + '.' + caller_01._funcname)
    if '!ALL!' in logger._modulesToLog:
        LOG_LEVEL = logger._logLevel

    else:
        fullPkg_LOW = fullPkg.lower()
        LOG_LEVEL = None
        for moduleStr in logger._modulesToLog:
            if moduleStr.lower() in fullPkg_LOW:
                LOG_LEVEL = logger._logLevel


    if fDEBUG:
        print ('fullPkg   :', fullPkg )
        print ('LOG_LEVEL :', LOG_LEVEL )


    if not LOG_LEVEL:
        logger._logEnabled = False   #  by Loreto:  22-01-2018 09.15.02
        return logger  # in fase di verifica  #  by Loreto:  22-01-2018 09.14.58
        # return _nullLogger

    logger.setLevel(LOG_LEVEL)
    logger._LnFilter.addStack(1+offsetSL)    # cambio lo stackNum
    caller_03 = GetCaller(3)


    if exiting:
        logger.info('.... exiting\n')
    else:
        logger.info('.... entering called by: {CALLER}'.format(CALLER=caller_03._fullcaller))

    return logger



###############################################
#
###############################################
def GetCaller(stackLevel=0):
    retCaller = LnClass()
    retCaller._rcode  = 0

    try:
        dummy, programFile, lineNumber, funcName, lineCode, rest = inspect.stack()[stackLevel]

    except Exception as why:
        retCaller._fullcaller  = str(why)
        retCaller._rcode  = 1
        return retCaller   # potrebbe essere out of stack ma ritorniamo comunque la stringa


    if funcName == '<module>': funcName = '__main__'

    retCaller._funcname   = funcName
    retCaller._linecode   = lineCode
    retCaller._lineno     = lineNumber
    retCaller._fullfname  = programFile

    fname                 = os.path.basename(programFile).split('.')[0]
    retCaller._fname      = fname
    retCaller._fullcaller = "[{0}.{1}:{2}]".format(fname, funcName, lineNumber)

    return retCaller

