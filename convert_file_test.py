import matlab.engine

LUMOMAT_PATH = './lumomat-1.8.0'    
LUMO_FILE = 'ExampleData/Example1/Example1_VisualCortexEccentricity.LUMO'
OUTPUT_SNIRF_FILE = 'tmpdir/tmp.snirf'

def main():
    eng = matlab.engine.start_matlab()

    eng.addpath(eng.genpath(LUMOMAT_PATH))
    eng.eval("data = LumoData('{}'); data.write_SNIRF('{}');".format(LUMO_FILE, OUTPUT_SNIRF_FILE), nargout=0)

if __name__ == '__main__':
    main()
