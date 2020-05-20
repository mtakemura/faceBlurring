from logs import logDecorator as lD
import jsonref

config = jsonref.load(open('../config/config.json'))
logBase = config['logging']['logBase'] + '.lib.argParsers.config'

@lD.log(logBase + '.parsersAdd')
def addParsers(logger, parser):
    '''add argument parsers specific to the ``config/config.json`` file
    
    This function is kgoing to add argument parsers specific to the 
    ``config/config.json`` file. This file has several options for 
    logging data. This information will be 
    
    Parameters
    ----------
    logger : {logging.Logger}
        The logger used for logging error information
    parser : {argparse.ArgumentParser instance}
        An instance of ``argparse.ArgumentParser()`` that will be
        used for parsing the command line arguments specific to the 
        config file
    
    Returns
    -------
    argparse.ArgumentParser instance
        The same parser argument to which new CLI arguments have been
        appended
    '''
    
    parser.add_argument("--module1_input", 
        type = path,
        help = "the path to the input image file")
 

    return parser

@lD.log(logBase + '.decodeParser')
def decodeParser(logger, args):
    '''generate a dictionary from the parsed args
    
    The parsed args may/may not be present. When they are
    present, they are pretty hard to use. For this reason,
    this function is going to convert the result into
    something meaningful.
    
    Parameters
    ----------
    logger : {logging.Logger}
        The logger used for logging error information
    args : {args Namespace}
        parsed arguments from the command line
    
    Returns
    -------
    dict
        Dictionary that converts the arguments into something
        meaningful
    '''


    values = {
    }
    
    try:
        if args.module1_input is not None:
            values['input'] = args.module1_input
    except Exception as e:
        logger.error('Unable to decode the argument logging_specs_logstash_port :{}'.format(
            e))
    
    return values

