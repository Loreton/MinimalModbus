
import Source as Prj
import LnLib as Ln

# from LnLib.Common.Exit      import Exit     as LnExit
from LnLib.Common.LnColor   import LnColor; C=LnColor()
#######################################################
# PROGRAM POSITIONAL parameters
#######################################################
def positionalParameters(myParser, paramName):
    global positionalParametersDict
    # mandatory = cPrint.getMagentaH('is MANDATORY - ') if required else cPrint.getCyanH('is OPTIONAL - ')

    posizARGS = 1
    positionalParametersDict  =  {
        'rs485_usb'     : "send/receive  Ln-RS485 protocol via USB_RS485_pen",
        'rs485_relay'   : "send/receive  Ln-RS485 protocol via Arduino Relay",
        'rs485_monitor' : "monitoring    Ln-RS485 protocol via USB_RS485_pen",
        'raw'           : "send/receive  Ln-RS485 protocol on USB port",
    }

    cmdList = []
    cmdList.append(C.getColored(color=C.magentaH, text='\n      Primary MANDATORY Parameters... enter one of them'))
    for key, val in positionalParametersDict.items():
        keyColor = C.getColored(color=C.yellowH, text=key)
        valColor = C.getColored(color=C.yellow, text=val)
        cmdList.append('\n')
        cmdList.append('          {0:<20} : {1}'.format(key, valColor))



        # -------------------------------------------------------
        # - con nargs viene tornata una lista con nArgs
        # - deve prendere il comando primario e poi il sottocomando
        # -------------------------------------------------------
    myParser.add_argument(paramName,
                metavar=''.join(cmdList),
                type=_checkPositionaParam,
                nargs=posizARGS,
                help='')
        #         help=C.getColored(color=C.yellowH, text='''
        # immettere uno dei comandi sopra elencati'''))



####################################
# # _checkPositionaParam()
####################################
def _checkPositionaParam(value):
    # print (type(value),value)

    if not value.lower() in positionalParametersDict.keys():
        errMsg = '{VALUE} - is NOT a valid MANDATORY parameter'.format(VALUE=value)
        C.printColored(color=C.cyanH, text=errMsg, tab=4)
        Ln.Exit(2, errMsg, printStack=False)


    return value
