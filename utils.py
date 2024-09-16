import matlab.engine
from snirf import Snirf, validateSnirf

LUMOMAT_PATH = './lumomat-1.8.0'    

def LUMO_to_SNIRF(lumo_file_name, output_snirf_file_name):
    eng = matlab.engine.start_matlab()

    eng.addpath(eng.genpath(LUMOMAT_PATH))
    eng.eval("data = LumoData('{}'); data.write_SNIRF('{}');".format(lumo_file_name, output_snirf_file_name), nargout=0)


def verify_SNIRF(snirf_file_name):
    snirf = Snirf(snirf_file_name, 'r')
    result = validateSnirf(snirf)

    result.display(severity=3)
    assert result, 'Invalid SNIRF file!\n' + result.display()  # Crash and display issues if the file is invalid.